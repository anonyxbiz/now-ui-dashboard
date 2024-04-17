from bottle import Bottle, route, run, request, static_file, response, post, get, put, delete, template
from json import dump, dumps, load, loads
from dashboard import user_dashboard

p = print 

app = Bottle()

@route('/')
def index():
    return template('examples/dashboard')

@route('/assets/<filename:path>')
def static(filename):
    return static_file(filename, root='./assets')

@route('/api/v1/analytics/artist', method='POST')
def dashboard_api():
    try:
        data = loads(request.body.getvalue().decode('utf-8'))
        username = data['username']
        return user_dashboard(username)
        
    except Exception as e:
        p(e)
        return {"detail": 403, "error": e}
        
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        origin = request.headers.get('Origin')
        if origin:
            response.headers['Access-Control-Allow-Origin'] = origin
        else:
            response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
        return fn(*args, **kwargs)
    return _enable_cors

for route in app.routes:
    route['callback'] = enable_cors(route['callback'])

if __name__ == '__main__':
    run(host='localhost', port=9000, debug=True, reloader=True)
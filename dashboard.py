from datetime import datetime as dt
from cryptography.fernet import Fernet
from json import load, dump
from random import randint as rd

p = print

def spotify(user):
    pass
    
def user_dashboard(user):
    user_data = {
        "username": user,
        "analytics": [rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), 90, 150, 160, 120, 140, rd(200,10000), rd(200,10000)],
        "analytics_labels": ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"],
        "analytics_label": "Streams",
        "email_stats_label": "Stats",
        "email_stats_labels": ["12pm", "3pm", "6pm", "9pm", "12am", "3am", "6am", "9am"],
        "email_stats": [rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000)],
        "latest_releases_data": [rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000), rd(200,10000)],
        "latest_releases_labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "latest_releases_label": "release_name",
        "statements": "<tr><td>30/03/2024</td><td>January</td><td>${},{}</td><td class=\"text-right\">Processing</td></tr>".format(rd(1,100), rd(100,1000))
    }
    return user_data

if __name__ == "__main__":
    a = user_dashboard("breeder_lw")
    p(a)
from datetime import datetime as dt
from cryptography.fernet import Fernet
from json import load, dump

p = print

def spotify(user):
    pass
    
def user_dashboard(user):
    user_data = {
        "username": user,
        "analytics": [200, 150, 100, 190, 130, 90, 150, 160, 120, 140, 190, 95],
        "analytics_labels": ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"],
        "analytics_label": "Streams",
        "email_stats_label": "Stats",
        "email_stats_labels": ["12pm,", "3pm", "6pm", "9pm", "12am", "3am", "6am", "9am"],
        "email_stats": [40, 500, 650, 700, 1200, 1250, 1300, 1900],
        "latest_releases_data": [542, 480, 430, 550, 530, 453, 380, 434, 568, 610, 700, 630],
        "latest_releases_labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "latest_releases_label": "release_name",
        "statements": "<tr><td>30/03/2024</td><td>January</td><td>$36,738</td><td class=\"text-right\">Processing</td></tr>"
    }
    return user_data

if __name__ == "__main__":
    a = user_dashboard("breeder_lw")
    p(a)
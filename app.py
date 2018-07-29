from flask import Flask, send_from_directory, request
from flask_cors import CORS
from redis_server import redis_server
from rq import Queue
from rq_scheduler import Scheduler
from datetime import datetime, timedelta
from pytz import timezone, utc
from sms.test import order_ready, subscription, get_number
from random import randint

scheduler = Scheduler(connection=redis_server)


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/message', methods=["POST"])
def message():
    phone = request.form['phone']
    phone = get_number(phone)
    if phone:
        subscription(phone)
        scheduler.enqueue_in(timedelta(seconds=10), order_ready, phone)
        return send_from_directory('static', 'subscribed.html')
    return send_from_directory('static', 'failed_index.html')

#
# def convertToUTC(time):
#     tz = timezone("America/New_York")
#     local_dt = tz.localize(time, is_dst=is_dst(tz))
#     return local_dt.astimezone(utc)
#
#
# def is_dst(tz):
#     now = utc.localize(datetime.utcnow())
#     return now.astimezone(tz).dst() != timedelta(0)


if __name__ == '__main__':
    app.run(debug=True)

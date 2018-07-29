from flask import Flask, send_from_directory, request
from flask_cors import CORS
from test.test import tmessage


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/message', methods=["POST"])
def message():
    tmessage(request)
    return send_from_directory('static', 'index.html')

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

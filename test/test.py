from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler
from datetime import datetime, timedelta
from pytz import timezone, utc
from test2.t2 import test

scheduler = Scheduler(connection=Redis())


def tmessage(request):
    print(request.form['phone'])
    # time = datetime.now() + timedelta(seconds=10)
    # print(time)
    # time = convertToUTC(time)
    # print(time)
    scheduler.enqueue_in(timedelta(seconds=10), test)
    print(scheduler.get_jobs(with_times=True))

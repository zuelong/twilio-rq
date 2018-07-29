from redis_server import redis_server
from twilio.rest import Client
from config.config import TWILIO_ACCOUNT, TWILIO_KEY, TWILIO_PHONE
from random import randint

client = Client(TWILIO_ACCOUNT, TWILIO_KEY)


def order_ready(phone):
    order = redis_server.get(phone).decode("utf-8")
    client.messages.create(
        to=phone,
        from_=TWILIO_PHONE,
        body="Order #{} is now ready for pick-up!".format(order))
    print('{}: {}'.format(phone, order))


def subscription(phone):
    order = randint(1000000, 9999999)
    redis_server.set(phone, order)
    message = client.messages.create(
        to=phone,
        from_=TWILIO_PHONE,
        body="Thank you for shopping with Tyler's CCG's!  Your order number is: {}".format(order))
    print(message)


def get_number(phone):
    try:
        number = client.lookups.phone_numbers(phone).fetch()
        print(number)
        return number.phone_number
    except:
        print('INVALID NUMBER {}'.format(phone))
        return


import asyncio

from flask import Flask
from flask_restful import Resource, Api, reqparse

from config import USER_ID
from loader import bot, botEventLoop

server = Flask(__name__)
api = Api(server)


async def send(message):
    await bot.send_message(USER_ID, message)


class Notifications(Resource):

    def get(self):
        asyncio.run_coroutine_threadsafe(bot.send_message(USER_ID, 'message'), botEventLoop).result()

        return 'success'

    def post(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('packageName', required=True)  # add arguments
        parser.add_argument('text', required=True)

        args = parser.parse_args()

        asyncio.run_coroutine_threadsafe(bot.send_message(USER_ID, args['text']), botEventLoop).result()

        return f"{args['text']}", 200


api.add_resource(Notifications, '/notification')

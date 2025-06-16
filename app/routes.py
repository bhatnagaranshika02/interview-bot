from flask import Flask
from app.views.api import LoginView, OTPView
from flask_restful import Api

def initialize_v1_routes(api: Api):
    """ Initialized all the routes related to Wallet. """
    api.prefix = '/resume-bot/v1'

    api.add_resource(OTPView, '/send-otp')
    api.add_resource(LoginView, '/login')

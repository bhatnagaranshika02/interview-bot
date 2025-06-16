from app.routes import initialize_v1_routes
from flask_restful import Api
from flask import Flask

application = Flask(__name__)

api = Api(application)
initialize_v1_routes(api)

if __name__ == '__main__':
    application.run(port=5000)
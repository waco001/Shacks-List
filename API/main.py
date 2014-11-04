from flask import Flask
from flask.ext import restful
import requests, datetime, logging
from requests.auth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
app = Flask(__name__)
api = restful.Api(app)

if __name__ == '__main__':
    app.run(debug=True)
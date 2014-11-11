from flask import Flask, session
from flask.ext import restful
import requests, datetime
from requests.auth import HTTPBasicAuth
from account import AccountRegister, AccountLogin, AccountLogout, Account
from listing import viewAllListingsByUser, addNewListing, getAllListings
import dataset
import config
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    api = restful.Api(app)
    api.add_resource(AccountRegister, '/account/register')
    api.add_resource(AccountLogin, '/account/login')
    api.add_resource(AccountLogout, '/account/logout')
    api.add_resource(Account, '/account/')
    api.add_resource(addNewListing, '/listing/add')
    api.add_resource(viewAllListingsByUser, '/account/listing/viewall/')
    api.add_resource(getAllListings, '/listing')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,host='0.0.0.0')
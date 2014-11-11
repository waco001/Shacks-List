from flask.ext import restful
from flask import render_template, Response, request, config, session, jsonify
from flask.ext.restful import reqparse
from functools import wraps
import dataset
import json
import config
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('logged_in') is None:
            return json.dumps({"error":"Not Logged In"})
        return f(*args, **kwargs)
    return decorated_function

class viewAllListingsByUser(restful.Resource):
    @login_required
    def get(self):
        db=dataset.connect(config.DATABASE_URL)
        table=db.get_table('listing')
        _listings=table.find(owner=request.form['username'])
        _jsonlistings = jsonify(_listings)
        return(_jsonlistings)
class addNewListing(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        args = parser.parse_args()
        db=dataset.connect(config.DATABASE_URL)
        table=db.get_table('listing')
        _newlisting=dict(name=args['name'], description=args['description'], owner="waco001")
        table.insert(_newlisting)
        return {"message":"Alread Logged In"}
class getAllListings(restful.Resource):
    def get(self):
        db=dataset.connect(config.DATABASE_URL)
        table=db.get_table('listing')
        _listings=table.all()
        _listingslist = []
        for i in _listings:
            _listingslist.append(i)
        return {'data':_listingslist}

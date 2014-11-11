from flask.ext import restful
from flask import render_template, Response, request, config, session
import dataset
import config
import hashlib
class AccountRegister(restful.Resource):
    def get(self):
        return Response(render_template("account/register.html"), mimetype="text/html")
    def post(self):
        _message=""
        db=dataset.connect(config.DATABASE_URL)
        table=db.get_table('users')
        same_usernames=table.find_one(username=request.form['username'])
        same_email=table.find_one(email=request.form['email'])

        if same_email != None or same_usernames != None:
            _message="You Already Have An Account"
            return Response(render_template("account/register.html",message=_message), mimetype="text/html")
        if request.form['password'] != request.form['confirmpassword']:
            _message="Passwords Do Not Match"
            return Response(render_template("account/register.html",message=_message), mimetype="text/html")
        _newuser=dict(username=request.form['username'],password=hashlib.md5(request.form['password'].encode('utf-8')).hexdigest(),
            email=request.form['email'],firstname=request.form['firstname'],
            lastname=request.form['lastname'],)
        table.insert(_newuser)
        return Response(render_template("account/register.html",message="Succesfully Registered"), mimetype="text/html")
class AccountLogin(restful.Resource):
    def get(self):
        if session['logged_in'] == True:
            return {"message":"Alread Logged In"}
        else:
            return Response(render_template("account/login.html"),mimetype="text/html")
    def post(self):
        db=dataset.connect(config.DATABASE_URL)
        table=db.get_table('users')
        _message=""
        _username=request.form['username']
        _password=hashlib.md5(request.form['password'].encode('utf-8')).hexdigest()
        same_usernames=table.find_one(username=_username)
        if (same_usernames == None) or (same_usernames['password'] != _password) :
            _message="Username or password is incorrect!"
        else:
            session['logged_in'] = True
            session['current_user']=_username
            _message="Sucessfully Logged In"
        return Response(render_template("account/login.html",message=_message), mimetype="text/html")
class AccountLogout(restful.Resource):
    def get(self):
        session['username'] = None
        session['logged_in'] = False
        return {"message":"Successfully Logged Out"}
class Account(restful.Resource):
    def get(self):
        if(session['logged_in']==True):
            return {"status":1}
        else:
            return {"status":0}

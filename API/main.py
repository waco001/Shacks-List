from flask import Flask
from flask.ext import restful
import requests, datetime
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
api = restful.Api(app)
sinchapplicationkey = "678aec4a-15dc-422a-894a-8daaf40dc3cf"
sinchappsecret = "VQAtORFpzUyt4jP7bb/qtw=="
class SendSMS(restful.Resource):
    def get(self):
        url = 'https://messagingApi.sinch.com/v1/sms/+46700000000'
        payload = {
        "Message" : "Shaks List Dude!",
        "From" : "+46000000001"
        }
        header = {
        "Content-Type": "text/json",
        "X-Timestamp" : str(datetime.datetime.utcnow()).replace(" ","T")+"Z"
        }
        basic_auth=HTTPBasicAuth('Application' + sinchapplicationkey, sinchapplicationkey)
        r = requests.post(url, data=payload, headers=header, verify=True,auth=basic_auth)
        return r.text

api.add_resource(SendSMS, '/')

if __name__ == '__main__':
    app.run(debug=True)
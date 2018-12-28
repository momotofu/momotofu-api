from flask import Flask, Blueprint, request, make_response
from flask_restful import Api, Resource, url_for, reqparse
import requests
import os, json

blog_bp = Blueprint('blog', __name__)
api = Api(blog_bp)


class HelloWorld(Resource):
    def get(self, id=1):
        response = make_response(json.dumps({ 'hello' : 'world %s ' % id }))
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

class ContactForm(Resource):
    def post(self):
        json = request.get_json(force=True)
        response = requests.post(
            "https://api.mailgun.net/v3/%s/messages" % os.getenv('EMAIL_DOMAIN'),
            auth=("api", os.getenv('EMAIL_API_KEY')),
            data={"from": "FROM BLOG: <%s>" % json['email'],
                  "to": [os.getenv('EMAIL_RECIPIENT')],
                  "subject": "Message from %s" % json['name'],
                  "text": json['message']})

        return response.status_code, {'Access-Control-Allow-Origin': '*'}


api.add_resource(ContactForm, '/receiveForm')
api.add_resource(HelloWorld, '/', '/hello/<int:id>')

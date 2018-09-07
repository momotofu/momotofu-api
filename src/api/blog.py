from flask import Flask, Blueprint, request
from flask_restful import Api, Resource, url_for, reqparse
import os

blog_bp = Blueprint('blog', __name__)
api = Api(blog_bp)

class HelloWorld(Resource):
    def get(self, id=1):
        return { 'hello' : 'world %s ' % id }

class ContactForm(Resource):

    def post(self):
        import yagmail
        if 'EMAIL' in os.environ.keys() and 'EMAIL_PW' in os.environ.keys():
            yag = yagmail.SMTP(os.environ['EMAIL'], os.environ['EMAIL_PW'])
        else:
            yag = yagmail.SMTP()

        json = request.get_json(force=True)
        contents = [json['name'], json['message']]
        yag.send('mrkita.reece@gmail.com', 'FROM BLOG: %s' % json['email'],
                contents)

        return json, 201, {'Access-Control-Allow-Origin': '*'}


api.add_resource(ContactForm, '/recieveForm')
api.add_resource(HelloWorld, '/', '/hello/<int:id>')

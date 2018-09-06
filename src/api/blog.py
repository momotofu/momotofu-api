from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for, reqparse

blog_bp = Blueprint('blog', __name__)
api = Api(blog_bp)

class HelloWorld(Resource):
    def get(self, id=1):
        return { 'hello' : 'world %s ' % id }

class ContactForm():
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('message', type=str)
        args = parser.parse_args()

api.add_resource(ContactForm, '/recieveForm')
api.add_resource(HelloWorld, '/', '/hello/<int:id>')

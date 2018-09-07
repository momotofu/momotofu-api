from flask import Flask, Blueprint, request
from flask_restful import Api, Resource, url_for, reqparse

blog_bp = Blueprint('blog', __name__)
api = Api(blog_bp)

class HelloWorld(Resource):
    def get(self, id=1):
        return { 'hello' : 'world %s ' % id }

class ContactForm(Resource):
    def post(self):
        json = request.get_json(force=True)

        return json, 201, {'Access-Control-Allow-Origin': '*'}





api.add_resource(ContactForm, '/recieveForm')
api.add_resource(HelloWorld, '/', '/hello/<int:id>')

from flask import Flask, Blueprint
from flask_restful import Api, Resource, url_for

blog_bp = Blueprint('blog', __name__)
api = Api(blog_bp)

class HelloWorld(Resource):
    def get(self, id=1):
        return { 'hello' : 'world %s ' % id }

api.add_resource(HelloWorld, '/', '/hello/<int:id>')

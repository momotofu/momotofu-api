from flask import Flask, Blueprint, request, make_response
from flask_restful import Api, Resource, url_for, reqparse
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
        import yagmail
        if os.getenv('EMAIL') and os.getenv('EMAIL_PW'):
            yag = yagmail.SMTP(os.getenv('EMAIL'), os.getenv('EMAIL_PW'))
        else:
            yag = yagmail.SMTP()

        json = request.get_json(force=True)
        contents = [json['name'], json['message']]
        yag.send('mrkita.reece@gmail.com', 'FROM BLOG: %s' % json['email'],
                contents)

        return 201, {'Access-Control-Allow-Origin': '*'}


api.add_resource(ContactForm, '/receiveForm')
api.add_resource(HelloWorld, '/', '/hello/<int:id>')

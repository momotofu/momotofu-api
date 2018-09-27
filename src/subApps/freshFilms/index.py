from flask import Flask, Blueprint, send_from_directory
# from ...app import app
import os

films_bp = Blueprint('films_bp', __name__)

@films_bp.route('/fresh_films')
def getPage():
    filepath = os.path.dirname(os.path.realpath(__file__)) + '/public'
    return send_from_directory(filepath, 'index.html')

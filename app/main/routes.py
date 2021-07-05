from flask import Blueprint

main_api = Blueprint('main_api', __name__)

@main_api.route('/')
def hello():
    return {"hello": "world"}
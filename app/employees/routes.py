from flask import Blueprint

employees_api = Blueprint('employees_api', __name__)

@employees_api.route('/employees', methods=['GET'])
def hello():
    return "This is the employees"
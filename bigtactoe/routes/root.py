from flask import Blueprint

root_blueprint = Blueprint('root_api', __name__)

@root_blueprint.route('/')
def hello_world():
    return 'HELLO WORLD'

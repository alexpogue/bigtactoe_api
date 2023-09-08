from .board import board_blueprint
from .root import root_blueprint

def init_app(app):
    app.register_blueprint(board_blueprint, url_prefix='/board')
    app.register_blueprint(root_blueprint, url_prefix='/')

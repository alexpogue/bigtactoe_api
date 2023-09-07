from .board import board_blueprint

def init_app(app):
    app.register_blueprint(board_blueprint, url_prefix='/board')

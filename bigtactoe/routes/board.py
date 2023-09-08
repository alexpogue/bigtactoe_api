from flask import Blueprint, request, jsonify
from flask_cors import CORS
from ..models.board import Board, board_schema, boards_schema
from ..models.base import db
from .util import get_by_id, ensure_json_or_die

board_blueprint = Blueprint('board_blueprint', __name__)

# Allows CORS on all board_blueprint routes
CORS(board_blueprint)


@board_blueprint.route('/')
def list_boards():
    all_boards = Board.query.all()
    return jsonify({'data': boards_schema.dump(all_boards)})


@board_blueprint.route('/<int:board_id>')
def get_board(board_id):
    board = get_by_id(Board, board_id, board_schema)
    return jsonify({'data': board})

@board_blueprint.route('/', methods=['POST'])
def new_board():
    ensure_json_or_die()
    request_data = request.get_json()

    board_contents = request_data['contents']
    board = Board(contents=board_contents)

    db.session.add(board)
    db.session.commit()
    return jsonify({'data': 'success'})

@board_blueprint.route('/<int:board_id>', methods=['PUT'])
def update_board(board_id):
    ensure_json_or_die()
    request_data = request.get_json()

    board = Board.query.get(board_id)
    if board is None:
        abort(404)

    new_contents = request_data.get('contents')
    if new_contents is not None:
        board.contents = new_contents

    db.session.commit()
    return jsonify({'data': 'success'})

@board_blueprint.route('/<int:board_id>', methods=['DELETE'])
def delete_board(board_id):
    board = Board.query.get(board_id)
    if board is None:
        abort(404)

    db.session.delete(board)
    db.session.commit()
    return jsonify({'data': 'success'})

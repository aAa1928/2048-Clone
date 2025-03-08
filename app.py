from game import Board

from dotenv import load_dotenv
from flask import Flask, render_template, request, session, jsonify

from os import environ
from pprint import pp
from secrets import token_hex
from types import NoneType

load_dotenv()
app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY', token_hex(16))

board: Board | NoneType = None

@app.before_request
def initialize_session():
    global board

    if 'grid' not in session:
        # Initialize a new game
        session['score'] = 0
        session['moves'] = 0
        board = Board()  # Create Board instance
        session.permanent = True
        session['grid'] = board.grid  # Store the grid (list) in session
    if board is None:
        board = Board(session['grid'])


@app.route('/')
def index():
    print('index()')
    update()
    return render_template('index.html', 
                          grid=session['grid'], 
                          score=session['score'], 
                          moves=session['moves'], 
                          game_over=session['game_over'],
                          best_score = session.get('best_score', 0))

@app.route('/update')
def update():
    print('update()')
    print(board)

@app.route('/move/<direction>', methods=['POST'])
def move(direction: str):
    print('move()')
    print(board)
    print(direction)
    session['grid'] = board.move(direction)
    session['moves'] += 1

    board.add_tile()

    print(board)

    return jsonify({'grid': session['grid']})

@app.route('/new_game', methods=['GET'])
def new_game():
    print('new_game()')

    # session['board'] = Board()
    session['grid'] = Board().grid
    board = Board(session['grid'])

    print(board)

    return jsonify({'grid': session['grid']})


if __name__ == '__main__':
    app.run(debug=True)
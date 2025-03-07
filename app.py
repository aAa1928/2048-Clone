from game import Board

from dotenv import load_dotenv
from flask import Flask, render_template, request, session, jsonify

from os import environ
from pprint import pp
from secrets import token_hex

load_dotenv()
app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY', token_hex(16))

@app.before_request
def initialize_session():
    if 'board' not in session:
        # Initialize a new game
        session['score'] = 0
        session['moves'] = 0
        board = Board()  # Create Board instance
        session.permanent = True
        session['board'] = board.grid  # Store the grid (list) in session


@app.route('/')
def index():
    print('index()')
    update()
    return render_template('index.html', 
                          board=session['board'], 
                          score=session['score'], 
                          moves=session['moves'], 
                          game_over=session['game_over'],
                          best_score = session.get('best_score', 0))

@app.route('/update')
def update():
    print('update()')
    print(*[row for row in session['board']], sep='\n')

@app.route('/move/<direction>', methods=['POST'])
def move(direction):
    print('move()')
    print(direction)
    update()
    return jsonify({'board': session['board']})

@app.route('/new_game', methods=['GET'])
def new_game():
    print('new_game()')

    session['board'] = Board().grid  # Create a new board

    print(*[row for row in session['board']], sep='\n')

    # session['score'] = 0
    # session['moves'] = 0
    # return jsonify({'board': session['board'], 'score': session['score'], 'moves': session['moves']})
    return jsonify({'board': session['board']})


if __name__ == '__main__':
    app.run(debug=True)
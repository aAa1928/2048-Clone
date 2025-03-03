from game import Board

from dotenv import load_dotenv
from flask import Flask, render_template, request, session, jsonify

from os import environ
from secrets import token_hex

load_dotenv()
app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY', token_hex(16))

@app.before_request
def initialize_session():
    if 'board' not in session:
        # Initialize a new game
        session['game_over'] = False
        session['score'] = 0
        session['moves'] = 0
        board = Board()  # Create Board instance
        session.permanent = True
        session['board'] = board.grid  # Store the grid (list) in session


@app.route('/')
def index():
    # Pass current game state to the template
    return render_template('index.html', 
                          board=session['board'], 
                          score=session['score'], 
                          moves=session['moves'], 
                          game_over=session['game_over'],
                          best_score = session.get('best_score', 0))

@app.route('/new_game', methods=['POST'])
def new_game():
    session['game_over'] = False
    session['best_score'] = session.get(max(session['score'], session['best_score']))
    session['score'] = 0
    session['moves'] = 0
    session['board'] = Board().grid  # Create a new board
    return jsonify({'board': session['board'], 'score': session['score'], 'moves': session['moves']})

if __name__ == '__main__':
    app.run(debug=True)
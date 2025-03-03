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
        session['board'] = board.grid  # Store the grid (list) in session
        session.permanent = True

@app.route('/')
def index():
    # Pass current game state to the template
    return render_template('index.html', 
                          board=session['board'], 
                          score=session['score'], 
                          moves=session['moves'], 
                          game_over=session['game_over'])

@app.route('/update-board', methods=['POST'])
def update_board():
    pass

@app.route('/reset', methods=['POST'])
def reset_game():
    pass

if __name__ == '__main__':
    app.run(debug=True)
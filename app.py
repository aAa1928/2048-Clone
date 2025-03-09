from game import Board

from dotenv import load_dotenv
from flask import Flask, render_template, request, session, jsonify, g

from os import environ
from pprint import pp
from secrets import token_hex
from types import NoneType

load_dotenv()
app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY', token_hex(16))

@app.before_request
def initialize_session():
    if 'grid' not in session:
        session['score'] = 0
        session['moves'] = 0
        g.board = Board()
        session.permanent = True
        session['grid'] = g.board.grid
    else:
        g.board = Board(session['grid'])

@app.route('/')
def index():
    print('index()')
    print(f'{g.board.is_game_over()=}')
    return render_template('index.html', 
                          grid=session['grid'], 
                          score=session['score'], 
                          moves=session['moves'], 
                          game_over=g.board.is_game_over(),
                          best_score=session.get('best_score', 0))

@app.route('/update')
def update():
    print('update()')
    print(g.board)

@app.route('/move/<direction>', methods=['POST'])
def move(direction: str):
    print('move()')
    print(g.board)
    print(direction)
    session['grid'] = g.board.move(direction)
    session['moves'] += 1
    print(g.board)
    return jsonify({'grid': session['grid'], 'game_over': g.board.is_game_over()})

@app.route('/new_game', methods=['GET'])
def new_game():
    print('new_game()')
    g.board = Board()
    session['grid'] = g.board.grid
    return jsonify({'grid': session['grid']})

@app.route('/game_over', methods=['GET'])
def game_over():
    return jsonify({'is_game_over': g.board.is_game_over()})

if __name__ == '__main__':
    app.run(debug=True)
# 2048 Clone

A web-based implementation of the popular puzzle game 2048. This project features a clean, responsive interface and smooth gameplay.

## Description

2048 is a single-player sliding block puzzle game. The game's objective is to slide numbered tiles on a grid to combine them and create a tile with the number 2048.

## Features

- Classic 2048 gameplay
- Responsive design works on desktop and mobile
- Score tracking with best score persistence
- Game over detection
- 2048 tile achievement recognition with option to continue playing
- Keyboard controls (arrow keys and WASD)

## How to Play

1. Use your **arrow keys** or **WASD** keys to move all tiles in one direction
2. When two tiles with the same number touch, they **merge into one** with their combined value
3. After each move, a new tile appears (usually a 2, sometimes a 4)
4. Keep combining tiles until you reach the 2048 tile
5. The game ends when there are no more moves possible

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/2048-Clone.git
   cd 2048-Clone
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Project Structure

```
2048-Clone/
├── app.py              # Flask application main file
├── game.py             # Game logic implementation
├── static/             # Static assets
│   ├── css/            # CSS styles
│   │   └── style.css   # Main stylesheet
│   └── js/             # JavaScript files
│       └── script.js   # Game interaction script
├── templates/          # HTML templates
│   └── index.html      # Main game page
└── requirements.txt    # Project dependencies
```

## Technologies Used

- **Backend**: Python with Flask
- **Frontend**: JavaScript, HTML5, CSS3
- **Session Management**: Flask session for game state persistence

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Risheet Lenka

---

Enjoy the game and try to reach 2048!

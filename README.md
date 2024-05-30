# Ping Pong game

This is a simple Ping Pong game written in Python using the `turtle` module.

## Author
- Muhammad Yousaf
- Email: yousafsahiwal3@gmail.com

## Description
This project is a basic implementation of the classic Pong game. It features two paddles and a ball. Two players can control the paddles to keep the ball in play. The game keeps track of the score for both players.

## Installation
1. Ensure you have Python installed on your system. This game was developed using Python 3.11.
2. No additional libraries are required as it uses the built-in `turtle` module.

## How to Run
1. Save the script as `main.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where `main.py` is located.
4. Run the script using the following command:
   ```bash
   python main.py
   

## Controls
- Player A (Left Paddle): 
  - Move Up: Press `W`
  - Move Down: Press `S`
- Player B (Right Paddle):
  - Move Up: Press `Up Arrow`
  - Move Down: Press `Down Arrow`

## Game Rules
- The ball will bounce off the top and bottom edges of the window.
- If the ball goes past a paddle, the opposite player scores a point.
- The game continues indefinitely, or until you close the window.

## Code Overview
- `screen`: The game window setup.
- `a`: Paddle for Player A.
- `b`: Paddle for Player B.
- `boll`: The ball that moves around the screen.
- `pen`: The turtle object used to display the score.
- Movement functions for paddles and collision detection for the ball.

Enjoy the game!

## License
This project is licensed under the MIT License.

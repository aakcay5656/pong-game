# Pong Game

This project includes a Pong game developed using the Turtle module in the Python programming language. The game is played with one player and an opponent controlled by an artificial intelligence.

## Game Controls

- **Player:** The 'Up' key provides up movement, the 'Down' key provides down movement.
- **Artificial Intelligence (Opponent):** `W` key provides up movement, `S` key provides down movement.

The main aim of the game is to score points by passing the ball into the opponent's court.

## Basic Artificial Intelligence Development

The AI ​​moves intelligently depending on the ball's position and speed. As the ball approaches or moves away from the opponent's territory, the artificial intelligence reacts more sensitively.

```python
def move_player2():
    if ball.xcor() < -100 and ball.xcor() > -350:
        if ball.ycor() > p2.ycor():
            p2.up()
        elif ball.ycor() < p2.ycor():
            p2.down()
    else:
        if p2.ycor() < 250:
            p2.up()
        elif p2.ycor() > -250:
            p2.down()
```
<img src="img/img1.PNG" width=600 height=300></img> 
## Dependencies

This project needs these dependencies:

- [Turtle](https://docs.python.org/3/library/turtle.html)

You can follow the steps below to install these dependencies:

1. **Turtle Library:** Turtle library is one of Python's standard libraries. It's usually included with Python, so you don't need to install it separately.

After downloading the project files, if Python is not installed, you should download and install Python from [Python's official website](https://www.python.org/downloads/).

I hope you have an enjoyable time!

import pyglet
from pyglet import shapes
import random
from pyglet.window import key

SNAKE_SIZE = 20
FIELD_WIDTH = 400
FIELD_HEIGHT = 200

window = pyglet.window.Window(FIELD_WIDTH, FIELD_HEIGHT, 'snake')

snake_x = 50
snake_y = 50
direction = 'LEFT'
snake_color = (255, 0, 0)

@window.event
def on_draw():
    global snake_x, snake_y, snake_color

    window.clear()

    snake = shapes.Rectangle(snake_x, snake_y, SNAKE_SIZE, SNAKE_SIZE, color=snake_color)
    snake.draw()

    #line = shapes.Line(0, 0, 300, 200, 5, color=(255, 0, 0))
    #line.draw()

@window.event
def on_key_press(symbol, modifiers):
    global direction

    if symbol ==  key.LEFT:
        direction = 'LEFT'
    elif symbol ==  key.RIGHT:
        direction = 'RIGHT'
    elif symbol == key.UP:
        direction = 'UP'
    elif symbol == key.DOWN:
        direction = 'DOWN'


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def update(dt):
    global snake_x, snake_y, direction, snake_color

    if direction == 'RIGHT':
        snake_x = snake_x + SNAKE_SIZE
    elif direction == 'LEFT':
        snake_x = snake_x - SNAKE_SIZE
    elif direction == 'UP':
        snake_y = snake_y + SNAKE_SIZE
    elif direction == 'DOWN':
        snake_y -= SNAKE_SIZE
    
    if snake_x >= FIELD_WIDTH - SNAKE_SIZE:
        direction = 'LEFT'
        snake_color = random_color()
    elif snake_x <= SNAKE_SIZE:
        direction = 'RIGHT'
        snake_color = random_color()
    elif snake_y <= SNAKE_SIZE:
        direction = 'UP'
        snake_color = random_color()
    elif snake_y >= FIELD_HEIGHT - SNAKE_SIZE:
        direction = 'DOWN'
        snake_color = random_color()


pyglet.clock.schedule_interval(update, 0.3)
pyglet.app.run()
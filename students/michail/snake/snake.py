import pyglet
from pyglet import shapes
import random
from pyglet.window import key

SNAKE_SIZE = 5
FIELD_WIDTH = 200
FIELD_HEIGHT = 200

window = pyglet.window.Window(FIELD_WIDTH, FIELD_HEIGHT, 'snake')

snake_x = 10
snake_y = 10
direction = 'RIGHT'
snake_color = (56, 255, 0)
apple_color = (255, 0, 0)

APPLE_SIZE = 5
apple_x = random.randint(20, 180)// 10*10
apple_y = random.randint(20, 180)// 10*10

@window.event
def on_draw():
    global snake_x, snake_y, snake_color, apple_x, apple_y, APPLE_SIZE, SNAKE_SIZE

    window.clear()

    snake = shapes.Rectangle(snake_x, snake_y, SNAKE_SIZE, SNAKE_SIZE, color=snake_color)
    snake.draw()

    #line = shapes.Line(0, 0, 300, 200, 5, color=(255, 0, 0))
    #line.draw()

    apple = shapes.Rectangle(apple_x, apple_y, APPLE_SIZE, APPLE_SIZE, color=apple_color)
    apple.draw()

    while snake_x == apple_x and snake_y == apple_y :
        print("1 apple eaten")
        apple_x = random.randint(20, 180)// 10*10
        apple_y = random.randint(20, 180)// 10*10
        apple = shapes.Rectangle(apple_x, apple_y, APPLE_SIZE, APPLE_SIZE, color=apple_color)
        apple.draw()
        
    list1 = [(snake_y, snake_x)]
    
    for snake_y, snake_x in list1:
        snakeback = shapes.Rectangle(snake_x, snake_y, SNAKE_SIZE, SNAKE_SIZE, color=snake_color)
        snakeback.draw()
        
        
        

@window.event
def on_key_press(symbol, modifiers):
    global direction

    if symbol ==  key.A:
        direction = 'LEFT'
    elif symbol ==  key.D:
        direction = 'RIGHT'
    elif symbol == key.W:
        direction = 'UP'
    elif symbol == key.S:
        direction = 'DOWN'


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def update(dt):
    global snake_x, snake_y, apple_x, apple_y, direction, snake_color

    if direction == 'RIGHT':
        snake_x = snake_x + SNAKE_SIZE
    elif direction == 'LEFT':
        snake_x = snake_x - SNAKE_SIZE
    elif direction == 'UP':
        snake_y = snake_y + SNAKE_SIZE
    elif direction == 'DOWN':
        snake_y = snake_y - SNAKE_SIZE
    
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

    if snake_x >= FIELD_WIDTH - SNAKE_SIZE:
        snake_x = 50
        snake_y = 50
        print("1 time failed")

    elif snake_x <= SNAKE_SIZE:
        snake_x = 50
        snake_y = 50
        print("1 time failed") 

    elif snake_y >= FIELD_HEIGHT - SNAKE_SIZE:
        snake_y = 50
        snake_x = 50
        print("1 time failed")

    elif snake_y <= SNAKE_SIZE:
        snake_y = 50
        snake_x = 50
        print("1 time failed")

        

pyglet.clock.schedule_interval(update, 0.3)
pyglet.app.run()

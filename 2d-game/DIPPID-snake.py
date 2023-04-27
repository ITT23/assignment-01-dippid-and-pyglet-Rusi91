from pyglet import app, image, clock
from pyglet.window import Window

from DIPPID import SensorUDP
from time import sleep

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

# window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# snake characteristics
SNAKE_COLOR = (197,220,224,0) # byte blue
SNAKE_CELL_SIZE = 15

# snake position
snake_x_pos = WINDOW_WIDTH / 2
snake_y_pos = WINDOW_HEIGHT / 2

# snake movement
snake_x_movement = 0.0
snake_y_movement = 0.0

def handle_accelerometer(data):
    if(sensor.has_capability('accelerometer')):
        global snake_x_movement, snake_y_movement
        # print only one accelerometer axis x
        snake_x_movement = sensor.get_value('accelerometer')['x']
        snake_y_movement = sensor.get_value('accelerometer')['y']
        print(snake_x_movement)
    

sensor.register_callback('accelerometer', handle_accelerometer)

# create game window
window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

@window.event
def on_draw():
    # clear window
    window.clear()
    # draw snake
    draw_snake()
    
# draw snake
def draw_snake():
    # snake snakehead characteristics
    snake_img = image.create(SNAKE_CELL_SIZE, SNAKE_CELL_SIZE, image.SolidColorImagePattern(SNAKE_COLOR))
    # draw the snakehead in a specific point of the window
    snake_img.blit(snake_x_pos, snake_y_pos)
    
def update_snake_pos(dt):
    global snake_x_movement, snake_y_movement, snake_x_pos, snake_y_pos
    
    snake_x_pos += snake_y_movement * 10
    snake_y_pos += snake_x_movement 

# set update interval
clock.schedule_interval(update_snake_pos, 0.5)















# run game
app.run()


    
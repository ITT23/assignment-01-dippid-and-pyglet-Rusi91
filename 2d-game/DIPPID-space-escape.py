from pyglet import app, image, clock
from pyglet.window import Window
import numpy as np

from DIPPID import SensorUDP
from time import sleep

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

# window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# ship characteristics
#SNAKE_COLOR = (197,220,224,0) # byte blue
SHIP_WIDTH = 20
SHIP_HEIGHT = 40
SHIP_Y_POS = SHIP_HEIGHT / 2

# snake position
ship_x_pos = WINDOW_WIDTH / 2

# snake movement
ship_x_movement = 0.0
#snake_y_movement = 0.0
ship_speed_multiplier = 5

# enemies
ROCKET_WIDTH = 10
ROCKET_HEIGHT = 20
ROCKET_COLOR = (255, 0, 0, 0) # red

rocket_1_x_pos = np.random.randint(0, WINDOW_WIDTH - ROCKET_WIDTH)
rocket_2_x_pos = np.random.randint(0, WINDOW_WIDTH - ROCKET_WIDTH)
rocket_3_x_pos = np.random.randint(0, WINDOW_WIDTH - ROCKET_WIDTH)

rocket_1_y_pos = WINDOW_HEIGHT - ROCKET_HEIGHT
rocket_2_y_pos = WINDOW_HEIGHT - ROCKET_HEIGHT
rocket_3_y_pos = WINDOW_HEIGHT - ROCKET_HEIGHT


def handle_accelerometer(data):
    global ship_x_movement
    #snake_x_movement = data['x']
    ship_x_movement = data['y']
    

sensor.register_callback('accelerometer', handle_accelerometer)

# create game window
window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

@window.event
def on_draw():
    # clear window
    window.clear()
    # draw snake
    draw_ship()
    
# draw snake
def draw_ship():
    global rocket_arr
    # snake snakehead characteristics
    #snake_img = image.create(SNAKE_CELL_SIZE, SNAKE_CELL_SIZE, image.SolidColorImagePattern(SNAKE_COLOR))
    ship_img = image.create(SHIP_WIDTH, SHIP_HEIGHT, image.SolidColorImagePattern(get_random_ship_color()))
    
    rocket_1 = image.create(ROCKET_WIDTH, ROCKET_HEIGHT, image.SolidColorImagePattern(ROCKET_COLOR))
    rocket_2 = image.create(ROCKET_WIDTH, ROCKET_HEIGHT, image.SolidColorImagePattern(ROCKET_COLOR))
    rocket_3 = image.create(ROCKET_WIDTH, ROCKET_HEIGHT, image.SolidColorImagePattern(ROCKET_COLOR))
    
    # draw the snakehead in a specific point of the window
    ship_img.blit(ship_x_pos, SHIP_Y_POS)
    
    rocket_1.blit(rocket_1_x_pos, rocket_1_y_pos)
    rocket_2.blit(rocket_2_x_pos, rocket_2_y_pos)
    rocket_3.blit(rocket_3_x_pos, rocket_3_y_pos)
    # draw rockets
    
    
def update_ship_pos(dt):
    global ship_x_movement, ship_x_pos
    
    if ship_x_pos >= WINDOW_WIDTH:
        ship_x_pos = SHIP_WIDTH
    if ship_x_pos <= 0:
        ship_x_pos = WINDOW_WIDTH - SHIP_WIDTH
    else:
        ship_x_pos -= ship_x_movement * ship_speed_multiplier
        #snake_y_pos += snake_y_movement * snake_speed_multiplier
        print(ship_x_movement)
        
    
def get_random_ship_color():
    # avoid black (0,0,0,0) because of black background
    r = np.random.randint(50,255)
    g = np.random.randint(50,255)
    b = np.random.randint(50,255)
    
    return (r,g,b,0)

def get_random_rocket_x_pos():
    return np.random.randint(ROCKET_WIDTH, WINDOW_WIDTH - ROCKET_WIDTH)

# set update interval
clock.schedule_interval(update_ship_pos, 0.1)















# run game
app.run()


    
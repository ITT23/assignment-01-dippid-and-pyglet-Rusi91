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

rockets_number = 10
rockets_arr = []

for x in range(rockets_number):
    rockets_arr.append([])
    rockets_arr[x].append(np.random.randint(0, WINDOW_WIDTH - ROCKET_WIDTH))
    rockets_arr[x].append(WINDOW_HEIGHT - ROCKET_HEIGHT)
    rockets_arr[x].append(np.random.randint(1,10))


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
    
    draw_rockets()
    
# draw snake
def draw_ship():
    global rocket_arr
    # snake snakehead characteristics
    #snake_img = image.create(SNAKE_CELL_SIZE, SNAKE_CELL_SIZE, image.SolidColorImagePattern(SNAKE_COLOR))
    ship_img = image.create(SHIP_WIDTH, SHIP_HEIGHT, image.SolidColorImagePattern(get_random_ship_color()))
    
    # draw the snakehead in a specific point of the window
    ship_img.blit(ship_x_pos, SHIP_Y_POS)
    # draw rockets
    
def draw_rockets():
    for x in range(rockets_number):
        rocket = image.create(ROCKET_WIDTH, ROCKET_HEIGHT, image.SolidColorImagePattern(ROCKET_COLOR))
        rocket.blit(rockets_arr[x][0], rockets_arr[x][1])
    
    
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
        
def update_rockets_pos(dt):
    
    for x in range(rockets_number):
        if rockets_arr[x][1] <= 0:
            rockets_arr[x][0] = get_random_rocket_x_pos()
            rockets_arr[x][1] = WINDOW_HEIGHT - ROCKET_HEIGHT
            rockets_arr[x][2] = get_random_rocket_speed_multiplier()
        else:
            rockets_arr[x][1] -= 0.5 * rockets_arr[x][2]
        
    
def get_random_ship_color():
    # avoid black (0,0,0,0) because of black background
    r = np.random.randint(50,255)
    g = np.random.randint(50,255)
    b = np.random.randint(50,255)
    
    return (r,g,b,0)

def get_random_rocket_x_pos():
    return np.random.randint(ROCKET_WIDTH, WINDOW_WIDTH - ROCKET_WIDTH)

def get_random_rocket_speed_multiplier():
    return np.random.randint(1, 10)

# set update interval
clock.schedule_interval(update_ship_pos, 0.1)
clock.schedule_interval(update_rockets_pos, 0.1)















# run game
app.run()


    
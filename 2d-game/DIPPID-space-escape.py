from pyglet import app, image, clock
from pyglet.window import Window
import pyglet
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

rocket_speed_difficulty_low_end = 1
rocket_speed_difficulty_high_end = 10

rockets_number = 15
rockets_arr = []

for x in range(rockets_number):
    rockets_arr.append([])
    rockets_arr[x].append(np.random.randint(0, WINDOW_WIDTH - ROCKET_WIDTH))
    rockets_arr[x].append(WINDOW_HEIGHT - ROCKET_HEIGHT)
    rockets_arr[x].append(np.random.randint(rocket_speed_difficulty_low_end, rocket_speed_difficulty_high_end))
    

# health potion
HEALTH_POTION_WIDTH = 10
HEALTH_POTION_HEIGHT = 20
HEALTH_POTION_COLOR = (0,255,0,0)
health_potion_x_pos = np.random.randint(0, WINDOW_WIDTH - HEALTH_POTION_WIDTH)
health_potion_y_pos = WINDOW_HEIGHT - HEALTH_POTION_HEIGHT

# speed buff
SPEED_BUFF_WIDTH = 10
SPEED_BUFF_HEIGHT = 20
SPEED_BUFF_COLOR = (0,0,255,0)
speed_buff_x_pos = np.random.randint(0, WINDOW_WIDTH - SPEED_BUFF_WIDTH)
speed_buff_y_pos = WINDOW_HEIGHT - SPEED_BUFF_HEIGHT

# bonus points
BONUS_POINTS_WIDTH = 10
BONUS_POINTS_HEIGHT = 20
bonus_points_x_pos = np.random.randint(0, WINDOW_WIDTH - BONUS_POINTS_WIDTH)
bonus_points_y_pos = WINDOW_HEIGHT - BONUS_POINTS_HEIGHT
    
player_lifes_remaining = 5
player_lifes_max = 10

player_points = 0

game_over = False


def handle_accelerometer(data):
    global ship_x_movement
    #snake_x_movement = data['x']
    ship_x_movement = data['y']
    
    if data['z'] < -0.8:
        global ship_x_pos, ship_speed_multiplier, health_potion_x_pos, health_potion_y_pos, \
            speed_buff_x_pos, speed_buff_y_pos, bonus_points_x_pos, bonus_points_y_pos, \
                player_lifes_remaining, player_points, game_over, \
                    rocket_speed_difficulty_low_end, rocket_speed_difficulty_high_end
        if game_over:
            ship_x_pos = WINDOW_WIDTH / 2
            ship_x_movement = 0.0
            ship_speed_multiplier = 5
            rockets_arr = []

            for x in range(rockets_number):
                rockets_arr.append([])
                rockets_arr[x].append(np.random.randint(0, WINDOW_WIDTH - ROCKET_WIDTH))
                rockets_arr[x].append(WINDOW_HEIGHT - ROCKET_HEIGHT)
                rockets_arr[x].append(np.random.randint(1,10))
                
            health_potion_x_pos = np.random.randint(0, WINDOW_WIDTH - HEALTH_POTION_WIDTH)
            health_potion_y_pos = WINDOW_HEIGHT - HEALTH_POTION_HEIGHT

            speed_buff_x_pos = np.random.randint(0, WINDOW_WIDTH - SPEED_BUFF_WIDTH)
            speed_buff_y_pos = WINDOW_HEIGHT - SPEED_BUFF_HEIGHT
            
            rocket_speed_difficulty_low_end = 1
            rocket_speed_difficulty_high_end = 10

            bonus_points_x_pos = np.random.randint(0, WINDOW_WIDTH - BONUS_POINTS_WIDTH)
            bonus_points_y_pos = WINDOW_HEIGHT - BONUS_POINTS_HEIGHT
                
            player_lifes_remaining = 5

            player_points = 0
            game_over = False
        
    

sensor.register_callback('accelerometer', handle_accelerometer)

# create game window
window = Window(WINDOW_WIDTH, WINDOW_HEIGHT)

@window.event
def on_draw():
    global game_over
    if player_lifes_remaining <= 0:
        game_over = True

    # clear window
    window.clear()
    # draw snake
    if game_over:
        draw_game_over_screen()
        
    else:
        draw_ship()
    
        draw_rockets()
        
        draw_lifes()
        
        draw_points()
        
        draw_health_potion()
        
        draw_speed_buff()
        
        draw_bonus_points_obj()
        
    
# draw snake
def draw_ship():
    global rocket_arr
    # snake snakehead characteristics
    #snake_img = image.create(SNAKE_CELL_SIZE, SNAKE_CELL_SIZE, image.SolidColorImagePattern(SNAKE_COLOR))
    ship = image.create(SHIP_WIDTH, SHIP_HEIGHT, image.SolidColorImagePattern(get_random_color()))
    
    # draw the snakehead in a specific point of the window
    ship.blit(ship_x_pos, SHIP_Y_POS)
    # draw rockets
    
def draw_rockets():
    for x in range(rockets_number):
        rocket = image.create(ROCKET_WIDTH, ROCKET_HEIGHT, image.SolidColorImagePattern(ROCKET_COLOR))
        rocket.blit(rockets_arr[x][0], rockets_arr[x][1])
        
def draw_lifes():
    player_lifes = pyglet.text.Label(str(player_lifes_remaining),
                          font_name='Times New Roman',
                          font_size=40,
                          x = WINDOW_WIDTH - WINDOW_WIDTH / 20, y = WINDOW_HEIGHT - WINDOW_HEIGHT / 20,
                          anchor_x='center', anchor_y='center')
    
    player_lifes.draw()
    
def draw_points():
    
    player_points_count = pyglet.text.Label("points: " + str(player_points),
                          font_name='Times New Roman',
                          font_size=20,
                          x = WINDOW_WIDTH / 10, y = WINDOW_HEIGHT / 20,
                          anchor_x='center', anchor_y='center')
    
    player_points_count.draw()
    
def draw_health_potion():
    global health_potion_x_pos, health_potion_y_pos
    # snake snakehead characteristics
    #snake_img = image.create(SNAKE_CELL_SIZE, SNAKE_CELL_SIZE, image.SolidColorImagePattern(SNAKE_COLOR))
    health_potion = image.create(HEALTH_POTION_WIDTH, HEALTH_POTION_HEIGHT, image.SolidColorImagePattern(HEALTH_POTION_COLOR))
    
    # draw the snakehead in a specific point of the window
    health_potion.blit(health_potion_x_pos, health_potion_y_pos)
    
def draw_speed_buff():
    global speed_buff_x_pos, speed_buff_y_pos
    # snake snakehead characteristics
    #snake_img = image.create(SNAKE_CELL_SIZE, SNAKE_CELL_SIZE, image.SolidColorImagePattern(SNAKE_COLOR))
    speed_buff = image.create(SPEED_BUFF_WIDTH, SPEED_BUFF_HEIGHT, image.SolidColorImagePattern(SPEED_BUFF_COLOR))
    
    # draw the snakehead in a specific point of the window
    speed_buff.blit(speed_buff_x_pos, speed_buff_y_pos)
    
def draw_bonus_points_obj():
    global bonus_points_x_pos, bonus_points_y_pos
    # snake snakehead characteristics
    #snake_img = image.create(SNAKE_CELL_SIZE, SNAKE_CELL_SIZE, image.SolidColorImagePattern(SNAKE_COLOR))
    bonus_points_obj = image.create(BONUS_POINTS_WIDTH, BONUS_POINTS_HEIGHT, image.SolidColorImagePattern(get_random_color()))
    
    # draw the snakehead in a specific point of the window
    bonus_points_obj.blit(bonus_points_x_pos, bonus_points_y_pos)

def draw_game_over_screen():
    game_over_points = pyglet.text.Label("Your Points: " + str(player_points),
                          font_name='Times New Roman',
                          font_size=40,
                          x = WINDOW_WIDTH / 2, y = WINDOW_HEIGHT / 1.5,
                          anchor_x='center', anchor_y='center')
    
    game_over_new_game = pyglet.text.Label("Turn your phone face down to start a new game.",
                          font_name='Times New Roman',
                          font_size=20,
                          x = WINDOW_WIDTH / 2, y = WINDOW_HEIGHT / 3,
                          anchor_x='center', anchor_y='center')
    
    game_over_points.draw()
    game_over_new_game.draw()
    
    
    
def update_ship_pos(dt):
    global ship_x_movement, ship_x_pos
    
    if ship_x_pos >= WINDOW_WIDTH:
        ship_x_pos = SHIP_WIDTH
    if ship_x_pos <= 0:
        ship_x_pos = WINDOW_WIDTH - SHIP_WIDTH
    else:
        ship_x_pos += ship_x_movement * ship_speed_multiplier
        #snake_y_pos += snake_y_movement * snake_speed_multiplier
        print(ship_x_movement)
        
def update_rockets_pos(dt):
    
    for x in range(rockets_number):
        global player_lifes_remaining, player_points
        if rockets_arr[x][1] <= 0:
            reset_rocket(x)
            player_points += 1
        if rockets_arr[x][0] >= ship_x_pos and rockets_arr[x][0] <= ship_x_pos + SHIP_WIDTH and rockets_arr[x][1] <= SHIP_Y_POS + SHIP_HEIGHT:
            player_lifes_remaining -= 1
            reset_rocket(x)
        else:
            rockets_arr[x][1] -= 0.5 * rockets_arr[x][2]
            
def update_health_potion_pos(dt):
    
    
    global health_potion_y_pos, health_potion_x_pos, player_lifes_remaining
    if health_potion_y_pos <= 0:
        reset_health_potion()
    if health_potion_x_pos >= ship_x_pos and health_potion_x_pos <= ship_x_pos + SHIP_WIDTH and health_potion_y_pos <= SHIP_Y_POS + SHIP_HEIGHT:
        if player_lifes_remaining + 1 <= player_lifes_max:
            player_lifes_remaining += 1
        reset_health_potion()
        
    else:
        health_potion_y_pos -= 1 
        
def update_speed_buff_pos(dt):
    
    
    global speed_buff_y_pos, speed_buff_x_pos, ship_speed_multiplier
    if speed_buff_y_pos <= 0:
        reset_speed_buff_object()
    if speed_buff_x_pos >= ship_x_pos and speed_buff_x_pos <= ship_x_pos + SHIP_WIDTH and speed_buff_y_pos <= SHIP_Y_POS + SHIP_HEIGHT:
        ship_speed_multiplier += 1
        reset_speed_buff_object()
        
    else:
        speed_buff_y_pos -= 4
        
def update_bonus_points_pos(dt):
    
    
    global bonus_points_y_pos, bonus_points_x_pos, player_points
    if bonus_points_y_pos <= 0:
        reset_bonus_points_object()
    if bonus_points_x_pos >= ship_x_pos and bonus_points_x_pos <= ship_x_pos + SHIP_WIDTH and \
        bonus_points_y_pos <= SHIP_Y_POS + SHIP_HEIGHT:
        player_points += 100
        reset_bonus_points_object()
        
    else:
        bonus_points_y_pos -= np.random.randint(1,10)
        
    
def get_random_color():
    # avoid black (0,0,0,0) because of black background
    r = np.random.randint(50,255)
    g = np.random.randint(50,255)
    b = np.random.randint(50,255)
    
    return (r,g,b,0)

def get_random_x_pos():
    return np.random.randint(ROCKET_WIDTH, WINDOW_WIDTH - ROCKET_WIDTH)

def get_random_rocket_speed_multiplier():
    return np.random.randint(rocket_speed_difficulty_low_end, rocket_speed_difficulty_high_end)

def reset_rocket(rocket_index):
    rockets_arr[rocket_index][0] = get_random_x_pos()
    rockets_arr[rocket_index][1] = WINDOW_HEIGHT - ROCKET_HEIGHT
    rockets_arr[rocket_index][2] = get_random_rocket_speed_multiplier()
    
def reset_health_potion():
    global health_potion_x_pos, health_potion_y_pos
    health_potion_x_pos = get_random_x_pos()
    health_potion_y_pos = WINDOW_HEIGHT - ROCKET_HEIGHT

def reset_speed_buff_object():
    global speed_buff_x_pos, speed_buff_y_pos
    speed_buff_x_pos = get_random_x_pos()
    speed_buff_y_pos = WINDOW_HEIGHT - SPEED_BUFF_HEIGHT
    
def reset_bonus_points_object():
    global bonus_points_x_pos, bonus_points_y_pos
    bonus_points_x_pos = get_random_x_pos()
    bonus_points_y_pos = WINDOW_HEIGHT - BONUS_POINTS_HEIGHT
    
def set_up_difficulty(dt):
    global rocket_speed_difficulty_low_end, rocket_speed_difficulty_high_end
    if rocket_speed_difficulty_low_end < 18:
        rocket_speed_difficulty_low_end += 1
        rocket_speed_difficulty_high_end += 1

# set update interval
clock.schedule_interval(update_ship_pos, 0.1)
clock.schedule_interval(update_rockets_pos, 0.1)
clock.schedule_interval(update_health_potion_pos, 0.1)
clock.schedule_interval(update_speed_buff_pos, 0.1)
clock.schedule_interval(update_bonus_points_pos, 0.1)
clock.schedule_interval(set_up_difficulty, 20)















# run game
app.run()


    
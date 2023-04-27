from pyglet import app, image
from pyglet.window import Window

# window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# snake characteristics
SNAKE_COLOR = (197,220,224,0) # byte blue
SNAKE_CELL_SIZE = 15

# snake position
snake_x_pos = WINDOW_WIDTH / 2
snake_y_pos = WINDOW_HEIGHT / 2

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

















# run game
app.run()


    
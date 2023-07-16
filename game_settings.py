import random
import pygame as pg
import pathlib


vector=pg.math.Vector2
FPS=60
CELL_SIZE=40


BOARD_COLOR=(100,92,92)
BG_COLOR=(51,25,0)
BOARD_SIZE=BOARD_WIDTH,BOARD_HEIGHT=10,20
BOARD_RESOLUTION=BOARD_WIDTH*CELL_SIZE*1.8,BOARD_HEIGHT*CELL_SIZE
BOARD_RESOLUTION2=BOARD_WIDTH*CELL_SIZE,BOARD_HEIGHT*CELL_SIZE

NEXT_SHAPE_RES=BOARD_WIDTH*CELL_SIZE*1.8-BOARD_WIDTH*CELL_SIZE, BOARD_HEIGHT*CELL_SIZE
NEXT_POSITION=vector(BOARD_WIDTH*1.35, BOARD_HEIGHT/2)
NEXT_POSITIONRECT=vector(BOARD_WIDTH*1.30, BOARD_HEIGHT/2)
INITIALIZE_POSITION = vector(BOARD_WIDTH / 2-1, 0) #TU ZMIANA
MOVEMENTS={"left": vector(-1,0), "right": vector(1, 0), "down": vector(0,1)}
TETROMINOS={
    'T':[(0,0), (-1,0), (1,0), (0,-1)],
    'NIESTANDARDOWY':[(0,0), (1,0), (0,-1)],
    'O':[(0,0), (0,-1), (1,0), (1,-1)],
    'J':[(0,0), (-1,0), (0,-1), (0,-2)],
    'L':[(0,0), (1,0), (0,-1), (0,-2)],
    'I':[(0,0), (0,1), (0,-1), (0,-2)],
    'S':[(0,0), (-1,0), (0,-1), (1,-1)],
    'Z':[(0,0), (1,0), (0,-1), (-1,-1)],
    'NIESTANDARDOWY2':[(0,0), (1,0)]
}
COLORS=["blue", "pink", "yellow", "green"]
# Ładowanie zdjec menu głownego
background=pg.image.load('images/tetris_background.jpg')
background_scaled=pg.transform.scale(background, BOARD_RESOLUTION)

#przyciski
play_game_btn=pg.image.load('images/playgame_btn.png')
play_game_clicked=pg.image.load('images/play_game_clicked.png')
play_game_rect=play_game_btn.get_rect()
play_game_rect.center= (365, 280)


scoreboard_btn=pg.image.load('images/scoreboard_btn.png')
scoreboard_clicked=pg.image.load('images/scoreboard_clicked.png')
scoreboard_rect=scoreboard_btn.get_rect()
scoreboard_rect.center=(360, 380)

hard_btn=pg.image.load('images/hard_lvl_btn.png')
hard_clicked=pg.image.load('images/hard_clicked.png')
hard_rect=hard_btn.get_rect()
hard_rect.center=(350,250)

medium_btn=pg.image.load('images/medium_lvl_btn.png')
medium_clicked=pg.image.load('images/medium_clicked.png')
medium_rect=medium_btn.get_rect()
medium_rect.center=(350,350)

easy_btn=pg.image.load('images/easy_lvl_btn.png')
easy_clicked=pg.image.load('images/easy_clicked.png')
easy_rect=easy_btn.get_rect()
easy_rect.center=(350,450)

quit_game_btn=pg.image.load('images/quitgame_btn.png')
quitgame_clicked=pg.image.load('images/quitgame_clicked.png')
quit_game_rect=quit_game_btn.get_rect()
quit_game_rect.center=(600, (BOARD_HEIGHT * CELL_SIZE-50))

back_btn=pg.image.load('images/back_btn.png')
back_clicked=pg.image.load('images/back_clicked.png')
back_rect=back_btn.get_rect()
back_rect.center=(350, 750)

control_btn=pg.image.load('images/controls_btn.png')
control_clicked=pg.image.load('images/controls_clicked.png')
control_rect=control_btn.get_rect()
control_rect.center=(365, 480)

menu_btn=pg.image.load('images/menu_btn.png')
menu_clicked=pg.image.load('images/menu_btn_clicked.png')
menu_rect=menu_btn.get_rect()
menu_rect.center=(350, 750)

cursor=pg.image.load('images/arrow.png')
cursor_scaled=pg.transform.scale(cursor, (25, 25))
# Ładowanie zdjec menu
tetris_logo=pg.image.load('images/Tetris_logo.png')
scaled_logo=pg.transform.scale(tetris_logo, (BOARD_WIDTH*CELL_SIZE, BOARD_HEIGHT/2*CELL_SIZE))
next_shape_img=pg.image.load('images/game.png')
scaled_next_shape=pg.transform.scale(next_shape_img, (BOARD_WIDTH*CELL_SIZE*0.8,BOARD_HEIGHT*CELL_SIZE))

key_up=pg.image.load("images/keys/arrow_up.png")
key_down=pg.image.load("images/keys/arrow_down.png")
key_left=pg.image.load("images/keys/arrow_left.png")
key_right=pg.image.load("images/keys/arrow_right.png")

key_up_resized=pg.transform.scale(key_up, (50,50))
key_down_resized=pg.transform.scale(key_down, (50,50))
key_left_resized=pg.transform.scale(key_left, (50,50))
key_right_resized=pg.transform.scale(key_right, (50,50))




# Ładowanie zdjec klocków
BLOCK_PATH='images/blocks'

def load_images():
    blocks = [item for item in pathlib.Path(BLOCK_PATH).glob('*.png')]
    images = [pg.image.load(block)for block in blocks]
    images = [pg.transform.scale(block, (CELL_SIZE, CELL_SIZE)) for block in images]
    return images


BLOCK_IMAGES=load_images()
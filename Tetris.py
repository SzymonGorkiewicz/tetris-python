from game_settings import *
from Tetromino import Tetromino
from scoreboard import Scoreboard


class Tetris(Scoreboard):

    def __init__(self, game, window):
        super().__init__(game, window, self)
        self.font=pg.font.Font('AFriendInDeed-3GEz.ttf',50)
        self.game = game
        self.window=window
        self.sprite_grp=pg.sprite.Group()
        self.tetromino = Tetromino(self)
        self.next_shape= Tetromino(self, current=False)
        self.list_of_tetrominos=[[0 for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]
        self.score=0
        self.score_add=0
        self.speed_up=False
        self.animation_time=0
        self.clear_board_sound=pg.mixer.Sound('sounds/clear_board.wav')
        self.place_block_sound=pg.mixer.Sound('sounds/place_block.wav')
        self.game_over_sound= pg.mixer.Sound('sounds/game_over.wav')

    def add_tetromino_tolist(self):
        for block in self.tetromino.blocks:
            x,y = int(block.position.x), int(block.position.y)
            self.list_of_tetrominos[y][x]=block

    def game_over(self):
        if self.tetromino.blocks[0].position.y==INITIALIZE_POSITION[1]:
            self.game_over_sound.set_volume(0.2)
            self.game_over_sound.play()
            return True

    def clear_board(self):
        self.list_of_tetrominos = [[0 for i in range(BOARD_WIDTH)] for j in range(BOARD_HEIGHT)]

    def add_to_map(self):
        if self.tetromino.add_to_map:
            self.speed_up=False
            if self.game_over():

                self.game.inputbool = True
                self.game.running = False

            else:
                self.add_tetromino_tolist()
                self.place_block_sound.set_volume(0.2)
                self.place_block_sound.play()
                self.next_shape.current=True
                self.tetromino=self.next_shape
                self.next_shape=Tetromino(self, current=False)

    def draw_board_grid(self):
        for i in range(BOARD_WIDTH):
            for j in range(BOARD_HEIGHT):
                pg.draw.rect(self.game.window, "black", (i*CELL_SIZE, j*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    def check_for_full_lines(self):

        row=BOARD_HEIGHT-1

        for i in range(BOARD_HEIGHT-1, -1, -1):
            for j in range(BOARD_WIDTH):
                self.list_of_tetrominos[row][j]=self.list_of_tetrominos[i][j]

                if self.list_of_tetrominos[i][j]:
                    self.list_of_tetrominos[row][j].position=vector(j, i)

            if sum(map(bool, self.list_of_tetrominos[i]))<BOARD_WIDTH:
                row-=1

            else:
                for j in range(BOARD_WIDTH):
                    self.list_of_tetrominos[row][j].alive=False
                    self.list_of_tetrominos[row][j]=0
                self.score+=self.score_add
                self.clear_board_sound.set_volume(0.2)
                self.clear_board_sound.play()

    def printing_score(self):
        score_text=self.font.render("SCORE {0}".format(self.score), True, (255,255,255))
        next_shape_text=self.font.render("NEXT SHAPE", True, (255, 255, 255))
        self.window.blit(score_text, (440,700))
        self.window.blit(next_shape_text, (460, 250))

    def controls(self, pressed_key):
        if pressed_key==pg.K_LEFT:
            self.tetromino.move("left")
        elif pressed_key==pg.K_RIGHT:
            self.tetromino.move("right")
        elif pressed_key==pg.K_UP:
            self.tetromino.rotate()
        elif pressed_key==pg.K_DOWN:
            self.speed_up=True

    def update(self):
        trigger=[self.game.animation, self.game.fast_animation][self.speed_up]
        if trigger:
            self.check_for_full_lines()
            self.tetromino.update()
            self.add_to_map()
        self.sprite_grp.update()
        pg.display.update()

    def draw(self):
        self.draw_board_grid()
        self.sprite_grp.draw(self.game.window)
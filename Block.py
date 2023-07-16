from game_settings import *


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, position):
        self.tetromino=tetromino
        self.position=vector(position)+INITIALIZE_POSITION
        self.next_pos=vector(position)+NEXT_POSITION
        self.next_posrect = vector(position) + NEXT_POSITIONRECT
        self.alive=True
        super().__init__(tetromino.tetris.sprite_grp)
        self.image=tetromino.color
        self.rect=self.image.get_rect()

        self.image_copy=self.image.copy()
        self.image_copy.set_alpha(110)
        self.image_speed=random.uniform(0.2, 0.6)
        self.image_cycles=random.randrange(6, 8)
        self.cycle_counter=0

    def animation_end(self):
        if self.tetromino.tetris.game.animation:
            self.cycle_counter+=2
            if self.cycle_counter>self.image_cycles:
                self.cycle_counter=0
                return True

    def animation_run(self):
        self.image=self.image_copy
        self.position.y-=self.image_speed
        self.image=pg.transform.rotate(self.image, pg.time.get_ticks()*self.image_speed)

    def checking_alive(self):
        if not self.alive:
            if not self.animation_end():
                self.animation_run()
            else:
                self.kill()

    def collision(self, position):
        x,y=int(position.x), int(position.y)
        if 0<=x<BOARD_WIDTH and y <BOARD_HEIGHT and (y<0 or not self.tetromino.tetris.list_of_tetrominos[y][x]):
            return False
        return True

    def rotate(self, rotate_point):
        point=self.position-rotate_point
        rotated=point.rotate(90)
        return rotated+rotate_point

    def set_position(self):
        if self.tetromino.shape!="O":
            position=[self.next_pos, self.position][self.tetromino.current]
        else:
            position = [self.next_posrect, self.position][self.tetromino.current]
        self.rect.topleft = position * CELL_SIZE

    def update(self):
        self.checking_alive()
        self.set_position()


from game_settings import *
from Block import Block


class Tetromino:
    def __init__(self, tetris, current=True):
        self.tetris=tetris
        self.shape=random.choice(list(TETROMINOS.keys()))
        self.color = random.choice(BLOCK_IMAGES)
        self.blocks=[Block(self, pos) for pos in TETROMINOS[self.shape]]
        self.add_to_map=False
        self.current=current

    def rotate(self):
        if self.shape!="O":
            rotate_point=self.blocks[0].position
            new_position=[block.rotate(rotate_point) for block in self.blocks]

            if not self.collision(new_position):
                for i, block in enumerate(self.blocks):
                    block.position=new_position[i]

    def move(self, direction):
        move_direction=MOVEMENTS[direction]
        new_position=[block.position+move_direction for block in self.blocks]

        is_collide=self.collision(new_position)
        if not is_collide:
            for block in self.blocks:
                block.position+=move_direction
        elif direction=="down":
            self.add_to_map=True

    def update(self):
        self.move("down")

    def collision(self, block_position):
        return any(map(Block.collision, self.blocks, block_position))
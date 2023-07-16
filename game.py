import time
from game_settings import *
from Tetris import Tetris
from scoreboard import Scoreboard


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Tetris")
        self.window=pg.display.set_mode(BOARD_RESOLUTION)
        self.clock=pg.time.Clock()
        self.tetris=Tetris(self, self.window)
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.animation = False
        self.fast_animation=False
        self.game_menu=True
        self.levels=False
        self.scorebool=False
        self.running=False
        self.inputbool=False
        self.FAST_ANIM_TIME = 1
        self.controls=False

    def clear_board(self):
        self.tetris.clear_board()

    def timer(self, animation_time):
        pg.time.set_timer(self.user_event, animation_time)
        pg.time.set_timer(self.fast_user_event, self.FAST_ANIM_TIME)

    def enlarge_button(self, rect, button, resized_button):
        mouse_x, mouse_y=pg.mouse.get_pos()
        if rect[2]<mouse_x<rect[2]+rect[0] and rect[3]<mouse_y<rect[3]+rect[1]:
            button=resized_button
            self.window.blit(button, rect)
        else:
            button=button
            self.window.blit(button, rect)

    def mouse_cursor(self):
        pg.mouse.set_visible(False)
        mouse_pos = pg.mouse.get_pos()
        self.window.blit(cursor_scaled, mouse_pos)

    def draw(self):
        self.window.fill(color=BG_COLOR)
        self.window.fill(color=BOARD_COLOR, rect=(0, 0, *BOARD_RESOLUTION2))
        self.window.blit(scaled_next_shape, (400, 0))
        self.tetris.draw()
        self.window.blit(scaled_logo, (BOARD_WIDTH*CELL_SIZE*0.9, -100))
        self.tetris.printing_score()

    def main_menu(self):
        self.window.blit(background_scaled, (0, 0))
        self.window.blit(play_game_btn, play_game_rect)
        self.window.blit(quit_game_btn, quit_game_rect)
        self.window.blit(control_btn, control_rect)
        self.window.blit(scoreboard_btn, scoreboard_rect)
        self.window.blit(tetris_logo, (95, -100))

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def check_events_menu(self):
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if play_game_rect.collidepoint(mouse_pos):
                    self.game_menu=False
                    self.levels=True
                    self.running=True
                elif scoreboard_rect.collidepoint(mouse_pos):
                    self.game_menu = False
                    self.scorebool=True
                elif control_rect.collidepoint(mouse_pos):
                    self.game_menu=False
                    self.controls=True
                elif quit_game_rect.collidepoint(mouse_pos):
                    pg.quit()

        if play_game_rect.collidepoint(mouse_pos):
            self.enlarge_button(play_game_rect, play_game_btn, play_game_clicked)
        elif scoreboard_rect.collidepoint(mouse_pos):
            self.enlarge_button(scoreboard_rect, scoreboard_btn, scoreboard_clicked)
        elif quit_game_rect.collidepoint(mouse_pos):
            self.enlarge_button(quit_game_rect, quit_game_btn,quitgame_clicked)
        elif control_rect.collidepoint(mouse_pos):
            self.enlarge_button(control_rect, control_btn,control_clicked)

    def check_events(self):
        self.animation=False
        self.fast_animation=False
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
            elif event.type==pg.KEYDOWN:
                self.tetris.controls(event.key)
                if event.key==pg.K_ESCAPE:
                    pg.quit()
            elif event.type==self.user_event:
                self.animation=True
            elif event.type==self.fast_user_event:
                self.fast_animation=True

    def run(self):
        self.check_events()
        self.draw()
        self.update()











                


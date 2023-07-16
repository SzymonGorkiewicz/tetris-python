import re
import time
import json
from game_settings import *
import re


class Scoreboard:
    def __init__(self, window, game, tetris):
        self.window=window
        self.game=game
        self.userinput=""
        self.tetris=tetris
        self.font2 = pg.font.Font("AFriendInDeed-3GEz.ttf", 50)
        self.font3 = pg.font.Font("AFriendInDeed-3GEz.ttf", 70)
        self.font4 = pg.font.Font("AFriendInDeed-3GEz.ttf", 30)
        self.text_font=pg.font.SysFont('comicsansms', 20, bold=True)
        self.pattern_length=r'^.{4,12}$'
        self.pattern_special_characters=r'^[A-Za-z0-9_]*$'
        self.is_false=False
        self.x_pos=130
        self.y_pos=180
        self.inputbool=False
        self.regex_bool=False
        self.colors_for_breathing=[255,153,204]
        self.directions_of_breathing=[0.7,0.7,0.7]
        self.y_pos_controls = 450

    def level_background(self):
        self.window.blit(background_scaled, (0,0))
        self.window.blit(hard_btn, hard_rect)
        self.window.blit(medium_btn, medium_rect)
        self.window.blit(easy_btn, easy_rect)
        self.window.blit(back_btn, back_rect)

    def check_events_level(self):
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
            elif event.type==pg.MOUSEBUTTONDOWN:
                if hard_rect.collidepoint(mouse_pos):
                    self.game.levels=False
                    self.game.runninng=True
                    self.tetris.__init__(self.game, self.window)
                    self.tetris.animation_time=400
                    self.tetris.score_add=120
                    self.game.timer(self.tetris.animation_time)
                elif medium_rect.collidepoint(mouse_pos):
                    self.game.levels = False
                    self.game.runninng = True
                    self.tetris.__init__(self.game, self.window)
                    self.tetris.animation_time = 500
                    self.tetris.score_add = 50
                    self.game.timer(self.tetris.animation_time)
                elif easy_rect.collidepoint(mouse_pos):
                    self.game.levels = False
                    self.game.runninng = True
                    self.tetris.__init__(self.game, self.window)
                    self.tetris.score_add = 20
                    self.tetris.animation_time = 600
                    self.game.timer(self.tetris.animation_time)
                elif back_rect.collidepoint(mouse_pos):
                    self.game.levels=False
                    self.game.game_menu=True
                    self.game.running=False
                    
        if hard_rect.collidepoint(mouse_pos):
            self.game.enlarge_button(hard_rect, hard_btn, hard_clicked)
        elif medium_rect.collidepoint(mouse_pos):
            self.game.enlarge_button(medium_rect, medium_btn, medium_clicked)
        elif easy_rect.collidepoint(mouse_pos):
            self.game.enlarge_button(easy_rect, easy_btn, easy_clicked)
        elif back_rect.collidepoint(mouse_pos):
            self.game.enlarge_button(back_rect, back_btn, back_clicked)

    def checking_events_input(self):
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
            elif event.type==pg.KEYDOWN:
                if event.key==pg.K_BACKSPACE:
                    self.userinput=self.userinput[:-1]
                elif event.key==pg.K_RETURN:
                    if self.regex_matching_length() and self.regex_matching_special_characters():
                        self.adding_to_scoreboard(self.userinput)
                        self.game.inputbool=False
                        self.game.scorebool=True
                    else:
                        self.regex_bool=True
                elif len(self.userinput)<=15:
                    self.userinput += event.unicode

            elif event.type==pg.MOUSEBUTTONDOWN:
                if menu_rect.collidepoint(mouse_pos):
                    self.game.inputbool=False
                    self.game.game_menu=True

        if menu_rect.collidepoint(mouse_pos):
            self.game.enlarge_button(menu_rect, menu_btn, menu_clicked)

    def regex_matching_length(self):
        if re.match(self.pattern_length, self.userinput):
            return True
        else:
            self.window.blit(self.font4.render("INCORRECT USERNAME (4-12 characters)", True, 'red'), (150, 320))

    def regex_matching_special_characters(self):
        if re.search(self.pattern_special_characters, self.userinput):
            return True
        else:
            self.window.blit(self.font4.render("NO SPECIAL CHARACTERS", True, 'red'), (220, 350))

    def input(self):
        self.window.blit(background_scaled, (0, 0))
        self.window.blit(self.font3.render("GAME OVER!", True, (0, 0, 0)), (220,70))
        self.window.blit(self.font3.render(f"SCORE: {self.tetris.score}", True, (0, 0, 0)), (250, 150))
        self.window.blit(self.font3.render("PROVIDE YOUR USERNAME", True, (0, 0, 0)), (60, 450))
        self.window.blit(menu_btn, menu_rect)
        input_rect = pg.Rect(170, 350, 380, 60)
        pg.draw.rect(self.window, "black", input_rect, border_radius=5)
        pg.draw.rect(self.window, "purple", input_rect, 6, border_radius=5)
        if len(self.userinput) >= 1:
            self.window.blit(self.tetris.font.render(self.userinput, True,  self.colors_for_breathing), (180, 355))
        self.color_breathing(self.colors_for_breathing, self.directions_of_breathing)

    def adding_to_scoreboard(self, user_nickname):
        new_dict={
            "name": user_nickname,
            "score": self.tetris.score
        }
        with open("scoreboard.json", "r") as plik:
            data=json.load(plik)
            data.append(new_dict)
        with open("scoreboard.json", 'w') as plik:
            json.dump(data, plik, indent=4)
        self.userinput = ''
        self.is_false=True

    def check_events_scoreboard(self):
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
            elif event.type==pg.MOUSEBUTTONDOWN:
                mouse_pouse=pg.mouse.get_pos()
                if back_rect.collidepoint(mouse_pouse):
                    self.game.game_menu=True
                    self.game.scorebool=False
        if back_rect.collidepoint(mouse_pos):
            self.game.enlarge_button(back_rect, back_btn, back_clicked)

    def color_breathing(self, color, direction):
        col_spd=0.1
        minimum=150
        maximum=255
        for i in range(3):
            color[i] += col_spd*direction[i]
            if color[i]>=maximum or color[i]<=minimum:
                direction[i]*=-1
            if color[i]>=maximum:
                color[i]=maximum
            elif color[i]<=minimum:
                color[i]=minimum

    def print_scoreboard(self):
        self.window.blit(background_scaled, (0, 0))
        self.window.blit(back_btn,  back_rect)
        input_rect = pg.Rect(50, 50, 630, 610)
        input_rect2 = pg.Rect(60, 60, 610, 590)
        pg.draw.rect(self.window, "black", input_rect, border_radius=12)
        pg.draw.rect(self.window, self.colors_for_breathing, input_rect2, 10, border_radius=12)
        with open("scoreboard.json", "r") as plik:
            data=json.load(plik)
            sorted_data=sorted(data, key=lambda x: x['score'], reverse=True)
        for i, directory in enumerate(sorted_data):
            if i>=10:
                break
            self.window.blit(self.font2.render(f"{i+1}.", True, (255,255,255)), (self.x_pos, self.y_pos+i*45))
            self.window.blit(self.font2.render(f"{directory['name']}", True, (255,255,255)), (self.x_pos+70, self.y_pos + i * 45))
            self.window.blit(self.font2.render(f"{directory['score']}", True, (255,255,255)), (self.x_pos+350, self.y_pos + i * 45))
        self.window.blit(self.font3.render("SCOREBOARD", True, self.colors_for_breathing), (210, 70))
        self.window.blit(self.font3.render("TOP 10", True,  self.colors_for_breathing), (280, 120))
        self.color_breathing(self.colors_for_breathing, self.directions_of_breathing)

    def print_controls(self):
        self.window.blit(background_scaled, (0, 0))
        self.window.blit(back_btn, back_rect)
        input_rect = pg.Rect(50, 50, 630, 650)
        input_rect2 = pg.Rect(60, 60, 610, 630)
        pg.draw.rect(self.window, "black", input_rect, border_radius=12)
        pg.draw.rect(self.window, self.colors_for_breathing, input_rect2,10, border_radius=12)
        self.window.blit(self.font3.render("CONTROLS", True, self.colors_for_breathing), (240, 70))
        self.window.blit(self.font3.render("RULES", True, self.colors_for_breathing), (280, 370))

        self.window.blit(key_up_resized, (100, 150))
        self.window.blit(key_down_resized, (100, 200))
        self.window.blit(key_left_resized, (100, 250))
        self.window.blit(key_right_resized, (100, 300))

        self.window.blit(self.text_font.render("Allows player to rotate a tetromino", True, 'white'), (160, 160))
        self.window.blit(self.text_font.render("Allows player to move tetromino down faster", True, 'white'), (160, 210))
        self.window.blit(self.text_font.render("Allows player to move tetromino block to left", True, 'white'), (160, 260))
        self.window.blit(self.text_font.render("Allows player to move tetromino block to right", True, 'white'), (160, 310))
        self.color_breathing(self.colors_for_breathing, self.directions_of_breathing)
        game_rules=["Tetris is a game where players control falling blocks",
                    "called Tetrominos, composed of four square units each.",
                    "The goal is to arrange the Tetrominos to form complete",
                    "horizontal lines, which disappear giving you some points.",
                    "Players must prevent the stack of Tetrominos from",
                    "reaching the top of the screen."]
        for i, b in enumerate(game_rules):
            self.window.blit(self.text_font.render(b, True, 'white'), (90,self.y_pos_controls+i*30))

    def check_events_controls(self):
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(mouse_pos):
                    self.game.game_menu = True
                    self.game.controls = False
        if back_rect.collidepoint(mouse_pos):
            self.game.enlarge_button(back_rect, back_btn, back_clicked)
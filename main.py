import time

from game_settings import *
from game import Game
from scoreboard import Scoreboard

run=True


if __name__=="__main__":

    game=Game()
    score = Scoreboard(game.window, game, game.tetris)

    while run:
        if game.game_menu:
            game.main_menu()
            game.check_events_menu()
            game.mouse_cursor()
            pg.display.update()
        elif game.levels:
            score.level_background()
            score.check_events_level()
            game.mouse_cursor()
            pg.display.update()
        elif game.scorebool:
            score.print_scoreboard()
            score.check_events_scoreboard()
            game.mouse_cursor()
            pg.display.update()
        elif game.running:
            game.run()
        elif game.inputbool:
            score.input()
            score.checking_events_input()
            game.mouse_cursor()
            if score.regex_bool:
                score.regex_matching_special_characters()
                score.regex_matching_length()
        elif game.controls:
            score.print_controls()
            score.check_events_controls()
            game.mouse_cursor()
            pg.display.update()
        pg.display.update()






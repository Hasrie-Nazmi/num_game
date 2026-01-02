import pygame
import sys
import time

from engine import Engine
from controls import Controls


class Game:
    def __init__(self):
        pygame.init()
        self.engine = Engine()
        self.controls = Controls()
        self.screen = pygame.display.set_mode((1000, 800))
        self.title = pygame.display.set_caption("NUM_GAME")
        self.clock = pygame.time.Clock()
        self.running = True
        display_info = pygame.display.Info()
        self.screen_width = display_info.current_w
        self.screen_height = display_info.current_h
        self.font_name = "assets/Neuropol X Rg.otf"

    def start_screen(self):
        self.draw_control_keys("W", 20, 20)
        self.write_text(
            "ADD: Adds Score with Next Number but will minus 1 life", (255, 255, 255), (80, 35), font_size=14)
        self.draw_control_keys("A", 20, 100)
        self.write_text(
            "MULTIPLY: Multiply Score with Next Number but it will subtract your lives with the Next Number", (255, 255, 255), (80, 115), font_size=14)
        self.draw_control_keys("S", 20, 180)
        self.write_text(
            "SUB: Subtracts score with Next Number. It will minus 1 life but you gain 1 power token.", (255, 255, 255), (80, 195), font_size=14)
        self.draw_control_keys("D", 20, 260)
        self.write_text(
            "DIVIDE: Divides Score with Next Number but you gain Lives according to the Next Number", (255, 255, 255), (80, 275), font_size=14)

        self.draw_control_keys("Q", 20, 340)
        self.write_text(
            "POWER UP: Activates the Power Up according to the accumulated Power Tokens. ", (255, 255, 255), (80, 355), font_size=14)
        self.write_text(
            "10 Tokens = Score x 5, 20 Tokens = Score & Lives x 5", (255, 255, 255), (80, 375), font_size=14)

        self.write_text("NOTE: During gameplay, tap",
                        (255, 255, 255), (20, 500), font_size=15)
        self.write_text("key twice to confirm action",
                        (255, 255, 255), (20, 525), font_size=15)
        self.write_text("Press 'SPACE' to continue",
                        (255, 255, 255), (self.screen_width/2-175, 700), font_size=20)

        pygame.display.flip()

        key_input = self.wait_for_key()
        if key_input == "space":
            return True

    def game_start(self):
        self.set_background_img("assets/game_background.jpg")
        self.draw_corner_decoration(0, self.screen_height-130, inverse=False)
        self.draw_corner_decoration(
            self.screen_width-378, self.screen_height-100, inverse=True)
        self.draw_game_info()
        pygame.display.flip()

    def end_screen(self):
        self.set_background_img("assets/endgame_background.jpg")

        self.write_text("GAME OVER!", (255, 255, 255),
                        (self.screen_width/2-80, self.screen_height/2))
        self.write_text(f"SCORE: {self.engine.get_high_scores():.2f}", (255, 255, 255),
                        (self.screen_width/2-300, self.screen_height/2+100))
        self.write_text(f"ROUNDS: {self.engine.get_rounds()}", (255, 255, 255),
                        (self.screen_width/2+125, self.screen_height/2+100))

        pygame.display.flip()

        key_input = self.wait_for_key()
        if key_input == "space":
            return

    def wait_for_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    waiting = False
                    print(pygame.key.name(event.key))
                    return pygame.key.name(event.key)

    def run(self):
        while True:
            if self.start_screen():
                while self.running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False

                        if self.engine.end_game():
                            self.end_screen()
                            pygame.quit
                            sys.exit()

                        self.engine.generate_next_num()
                        self.game_start()
                        self.engine.get_next_num()
                        self.engine.get_rounds()
                        key_input = self.wait_for_key()
                        key_input_confirm = self.wait_for_key()
                        if key_input == key_input_confirm:
                            correct_input = self.controls.button_controls(
                                self.engine, key_input_confirm)
                            if not correct_input:
                                self.popup_message("Wrong input")
                                time.sleep(2)
                            if self.engine.get_error() is not None:
                                self.popup_message(
                                    self.engine.get_error(), 10, 500)
                                time.sleep(2)

                        self.clock.tick(60)
                        pygame.display.flip()

    def set_background_img(self, img):
        bg = pygame.image.load(img).convert()
        bg = pygame.transform.scale(
            bg, (self.screen_width, self.screen_height))
        self.screen.blit(bg, (0, 0))

    def write_text(self, text_str, text_color, text_position, font_size=20):
        font = pygame.font.Font(self.font_name, font_size)
        text = font.render(text_str, True, text_color)
        self.screen.blit(text, text_position)

    def draw_control_keys(self, key_name, x_pos, y_pos):
        rect = pygame.Rect(x_pos, y_pos, 50, 50)
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            rect,
            width=2,
            border_radius=10
        )

        font = pygame.font.Font(self.font_name, 15)
        text = font.render(key_name, True, (255, 255, 255))
        text_rect = text.get_rect(center=rect.center)
        self.screen.blit(text, text_rect)

    def popup_message(self, text_str, rect_x=10, rect_width=200):
        rect = pygame.Rect(rect_x, 10, rect_width, 80)
        pygame.draw.rect(self.screen, (128, 0, 0), rect)
        font = pygame.font.Font(self.font_name, 15)
        text = font.render(text_str, True, (255, 255, 255))
        text_rect = text.get_rect(center=rect.center)
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def draw_corner_decoration(self, x, y, w=375, h=125, inverse=False):
        cut = 120  # how much corner to cut
        if inverse:
            points = [
                (x + cut, y),         # diagonal start
                (x + w, y),           # top-right
                (x + w, y + h),       # bottom-right
                (x, y + h),           # bottom-left
                (x, y + cut),         # diagonal end
            ]

        else:
            points = [
                (x, y),                   # top-left
                (x + w - cut, y),         # diagonal start
                (x + w, y + cut),         # diagonal end
                (x + w, y + h),           # bottom-right
                (x, y + h),               # bottom-left
            ]

        pygame.draw.polygon(self.screen, (255, 200, 0), points, 2)

    def draw_game_info(self):
        lives_pos = [f'Lives: {self.engine.get_lives()}',
                     (10, self.screen_height-120)]

        score_pos = [f'Score: {self.engine.get_score():.2f}',
                     (10, self.screen_height-80)]
        if self.engine.get_prev_action() is not None:
            prev_action_pos = [f'Previous Actions: {self.engine.get_prev_action().upper()}', (
                10, self.screen_height-40)]
        else:
            prev_action_pos = [f'Previous Actions: {self.engine.get_prev_action()}', (
                10, self.screen_height-40)]

        rounds_pos = [f'Rounds: {self.engine.get_rounds()}',
                      (self.screen_width/2-50, 5)]

        next_num_pos = [f'Next Number: {self.engine.get_next_num()}',
                        (self.screen_width/2-100, self.screen_height/2)]
        power_token_count_pos = [
            f'Power Token: {self.engine.get_power_token_count()}', (self.screen_width-275, self.screen_height-40)]

        power_type_pos = [f'Power Type: {self.engine.get_num_power()}',
                          (self.screen_width-275, self.screen_height-80)]

        game_info_pos = [lives_pos, rounds_pos, score_pos,
                         next_num_pos, power_token_count_pos, prev_action_pos, power_type_pos]

        for game_info in game_info_pos:
            self.write_text(game_info[0], (255, 255, 255), game_info[1])

import pygame
import sys

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

    def start_screen(self):

        images = {"add.jpg": (15, 10),
                  "sub.jpg": (350, 10),
                  "multi.jpg": (685, 10),
                  "divi.jpg": (15, 400),
                  "powerup.jpg": (350, 400)}
        self.screen.fill((30, 30, 60))
        for img in images:

            image = pygame.image.load(f"assets/instructions/{img}")
            image = pygame.transform.scale(image, (300, 400))
            self.screen.blit(image, images[img])

        self.write_text("NOTE: During gameplay, tap",
                        (255, 255, 255), (675, 500), font_size=15)
        self.write_text("key twice to confirm action",
                        (255, 255, 255), (675, 525), font_size=15)
        self.write_text("Press 'SPACE' to continue",
                        (255, 255, 255), (700, 700), font_size=15)
        pygame.display.flip()

        key_input = self.wait_for_key()
        if key_input == "space":
            return True

    def game_start(self):
        self.set_background_img("assets/game_background.jpg")
        self.draw_game_info()
        pygame.display.flip()

    def end_screen(self):
        self.set_background_img("assets/endgame_background.jpg")

        self.write_text("GAME OVER!", (255, 255, 255),
                        (self.screen_width/2-75, self.screen_height/2))
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
                            self.controls.button_controls(
                                self.engine, key_input_confirm)
                        self.clock.tick(60)
                        pygame.display.flip()

    def set_background_img(self, img):
        bg = pygame.image.load(img).convert()
        bg = pygame.transform.scale(
            bg, (self.screen_width, self.screen_height))
        self.screen.blit(bg, (0, 0))  # Draw background image

    def write_text(self, text_str, text_color, text_position, font="assets/Neuropol X Rg.otf", font_size=20):
        font = pygame.font.Font(font, font_size)
        text = font.render(text_str, True, text_color)
        self.screen.blit(text, text_position)

    def draw_game_info(self):
        lives_pos = [f'Lives: {self.engine.get_lives()}',
                     (20, self.screen_height-120)]

        score_pos = [f'Score: {self.engine.get_score()}',
                     (10, self.screen_height-80)]

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

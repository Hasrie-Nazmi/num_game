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
        self.font = pygame.font.Font("Neuropol X Rg.otf", 20)
        self.clock = pygame.time.Clock()
        self.running = True
        display_info = pygame.display.Info()
        self.screen_width = display_info.current_w
        self.screen_height = display_info.current_h

    def start_screen(self):
        game_instructions = ("Addition: Adds Score with Next Number but will minus 1 life\n"
                             "Substraction: Substract Score with Next Number. It will minus 1 life but you gain 1 power token. Accumulate 10 tokens, you can multiply your score by 5. Accumulate 20 tokens, you can multiply both your Score and Lives by 5\n"
                             "Multiplication: Multiply Score with Next Number but it will substract your Lives with the Next Number\n"
                             "Division: Divides Score with Next Number but you gain Lives according to the Next Number\n"
                             "Power Up: Activate the Power Up According to the accumulated Power Tokens")

        self.screen.fill((30, 30, 30))

        self.write_text(20, "NUM_GAME", (255, 255, 255),
                        (self.screen_width/2-75, 5))
        self.write_text(20, game_instructions, (255, 255, 255),
                        (10, 50))

        pygame.display.flip()

        key_input = self.wait_for_key()
        if key_input == "space":
            return True

    def game_start(self):
        self.set_background_img()
        self.draw_game_info()
        pygame.display.flip()

    def end_screen(self):
        self.screen.fill((30, 30, 30))

        self.write_text(20, "GAME OVER!", (255, 255, 255),
                        (self.screen_width/2-100, self.screen_height/2))
        self.write_text(20, "SCORE: ", (255, 255, 255),
                        (self.screen_width/2-150, self.screen_height/2+50))
        self.write_text(20, "ROUNDS: ", (255, 255, 255),
                        (self.screen_width/2+25, self.screen_height/2+50))

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
                        self.controls.button_controls(self.engine, key_input)
                        self.clock.tick(60)
                        pygame.display.flip()

    def set_background_img(self):
        bg = pygame.image.load("background.jpg").convert()
        bg = pygame.transform.scale(
            bg, (self.screen_width, self.screen_height))
        self.screen.blit(bg, (0, 0))  # Draw background image

    def write_text(self, font_size, text_str, text_color, text_position):
        text = self.font.render(text_str, True, text_color)
        self.screen.blit(text, text_position)

    def draw_game_info(self):
        lives_pos = [f'Lives: {self.engine.get_lives()}',
                     (10, self.screen_height-120)]

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
            self.write_text(20, game_info[0], (255, 255, 255), game_info[1])

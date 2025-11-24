import random


class Engine:

    def __init__(self):
        self.lives = 10
        self.score = random.randint(1, 10)
        self.high_score = self.score
        self.num_power = None
        self.num_power_token = 0
        self.next_num = random.randint(1, 10)
        self.prev_action = None
        self.rounds = 1

    def add(self):
        self.score += self.next_num
        self.prev_action = "add"
        self.lives -= 1
        self.clear_next_num()

    def sub(self):
        self.score -= self.next_num
        self.num_power_count()
        self.prev_action = "sub"
        self.lives -= 1
        self.clear_next_num()

    def multi(self):
        self.prev_action = "multi"
        self.score *= self.next_num * 1.5
        self.lives -= self.next_num
        self.clear_next_num()

    def divi(self):
        if (self.score / self.next_num) < 1:
            print("Your score is too low to divide by this number")
        else:
            self.prev_action = "divi"
            self.score /= self.next_num
            self.lives += self.next_num
            self.clear_next_num()

    def generate_next_num(self):
        if self.next_num is None:
            self.rounds += 1
            self.next_num = random.randint(1, 10)

    def clear_next_num(self):
        if self.next_num is not None:
            self.next_num = None

    def num_power_count(self):
        self.num_power_token += 1

        if self.num_power_token >= 20:
            self.num_power = "S&L"
        elif self.num_power_token >= 10:
            self.num_power = "S"
        else:
            self.num_power = None

    def num_power_activate(self):
        if self.num_power is not None:
            if self.num_power == "S":
                self.score **= 2
                self.prev_action = "S Squared"
            if self.num_power == "S&L":
                self.score *= 5
                self.lives *= 5
                self.prev_action = "S&L Squared"
            self.num_power = None
            self.num_power_token = 0
            self.clear_next_num()
            self.generate_next_num()
        else:
            print("No Number Power")

    def get_score(self):
        return self.score

    def get_prev_action(self):
        return self.prev_action

    def get_num_power(self):
        return self.num_power

    def get_power_token_count(self):
        return self.num_power_token

    def get_high_scores(self):
        if self.score > self.high_score:
            self.high_score = self.score
        return self.high_score

    def get_rounds(self):
        return self.rounds

    def get_next_num(self):
        return self.next_num

    def get_lives(self):
        return self.lives

    def end_game(self):
        if self.lives <= 0 or self.score < 0:
            return True
        else:
            return False

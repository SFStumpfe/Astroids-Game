import os

class Score:
    def __init__(self, save_file="highscore.txt"):
        self.score = 0
        self.save_file = save_file
        self.high_score = self.load_high_score()

    def add_point(self):
        self.score += 1

        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def reset(self):
        self.score = 0

    # ---------- SAVE / LOAD ----------

    def load_high_score(self):
        if not os.path.exists(self.save_file):
            return 0

        with open(self.save_file, "r") as f:
            try:
                return int(f.read())
            except ValueError:
                return 0

    def save_high_score(self):
        with open(self.save_file, "w") as f:
            f.write(str(self.high_score))
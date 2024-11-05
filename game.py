import random
import time

# Word class to handle each word's original and scrambled form
class Word:
    def __init__(self, original):
        self.original = original
        self.scrambled = self.scramble_word()

    def scramble_word(self):
        scrambled = list(self.original)
        random.shuffle(scrambled)
        return ''.join(scrambled)

    def check_answer(self, answer):
        return answer.lower() == self.original.lower()


# Level class to manage the words, timer, and attempts in each level
class Level:
    def __init__(self, word_list, level_time=30):
        self.words = [Word(word) for word in word_list]
        self.level_time = level_time  # Time limit per level in seconds
        self.start_time = None
        self.current_word_index = 0
        self.wrong_attempts = 0

    def start_level(self):
        self.start_time = time.time()

    def next_word(self):
        if self.current_word_index < len(self.words) - 1:
            self.current_word_index += 1
            return True
        return False  # No more words left in this level

    def get_current_word(self):
        return self.words[self.current_word_index].scrambled

    def check_answer(self, answer):
        word = self.words[self.current_word_index]
        if word.check_answer(answer):
            return True
        else:
            self.wrong_attempts += 1
            return False

    def is_time_up(self):
        if self.start_time is None:
            return False
        elapsed_time = time.time() - self.start_time
        return elapsed_time >= self.level_time


# Player class to track the player's score and wrong attempts
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.total_wrong_attempts = 0

    def update_score(self, points):
        self.score += points

    def increment_wrong_attempts(self):
        self.total_wrong_attempts += 1

    def display_score(self):
        return f"{self.name}'s Score: {self.score}, Wrong Attempts: {self.total_wrong_attempts}"


# Game class to manage the game flow across levels and display results
class Game:
    def __init__(self, levels_data, player_name):
        self.levels = [Level(words) for words in levels_data]
        self.current_level_index = 0
        self.player = Player(player_name)
        self.points_per_correct_answer = 10

    def start_game(self):
        print("Game started!")
        while self.current_level_index < len(self.levels):
            level = self.levels[self.current_level_index]
            self.play_level(level)
            self.current_level_index += 1
        self.show_results()

    def play_level(self, level):
        level.start_level()
        print(f"\nStarting Level {self.current_level_index + 1}!")

        while True:
            if level.is_time_up():
                print("Time's up for this level!")
                break

            scrambled_word = level.get_current_word()
            print(f"Scrambled Word: {scrambled_word}")
            answer = input("Your guess: ")

            if level.check_answer(answer):
                print("Correct!")
                self.player.update_score(self.points_per_correct_answer)
                if not level.next_word():
                    print("All words completed in this level!")
                    break
            else:
                print("Wrong! Try again.")
                self.player.increment_wrong_attempts()

        print(f"Level {self.current_level_index + 1} complete. Moving to the next level.")

    def show_results(self):
        print("\nGame Over!")
        print(self.player.display_score())


# Main program to run the game
if __name__ == "__main__":
    levels_data = [
        ["python", "programming", "code"],          # Level 1 words
        ["function", "variable", "class"],          # Level 2 words
        ["inheritance", "polymorphism", "abstraction"]  # Level 3 words
    ]

    player_name = input("Enter your name: ")
    game = Game(levels_data, player_name)
    game.start_game()

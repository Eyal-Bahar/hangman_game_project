# Write your code here
import random

# class Winner(Exception):
#     pass
#
# def print_missing(word, non_missing_idxs):
#     full_hiphen = "-" * (len(word))
#     to_show = list(full_hiphen)
#     word_list = list(word)
#     for idx in non_missing_idxs:
#         to_show[idx] = word_list[idx]
#     to_show = "".join(to_show)
#     print(f"{to_show}")
#
#
# ATTEMPTS = 8
# WORD_BANK = ["python", "java", "swift", "javascript"]
# word = random.choice(WORD_BANK)
# print("""H A N G M A N"\n""")
#
# non_missing_idxs = []
# ATTEMPTS_made = 0
# try:
#     while ATTEMPTS_made < ATTEMPTS:
#         print_missing(word, non_missing_idxs)
#         if len(set(non_missing_idxs)) == len(word):
#             raise Winner
#         print("Input a letter:")
#         letter = input()
#         if letter not in word:
#             print("That letter doesn't appear in the word.")
#             ATTEMPTS_made += 1
#         else:
#             found_letter_idx = [pos for pos, char in enumerate(word) if char == letter]
#
#             if found_letter_idx[0] in non_missing_idxs:
#                 print("No improvements.")
#                 ATTEMPTS_made += 1
#             non_missing_idxs = non_missing_idxs + found_letter_idx
#     print("You lost!")
#
# except Winner:
#     print("""You guessed the word!
#     You survived!""")

class Ui:
    def __init__(self):
        pass

    def startup_up(self):
        print("""H A N G M A N"\n""")

    def show_known(self, partially_revealed):
        print(f"{partially_revealed}")

    def request_letter(self):
        print("Input a letter:")
        return input()

    def wrong_guess(self):
        print("That letter doesn't appear in the word.")

    def no_improvment(self):
        print("No improvements.")

    def winner_msg(self):
        print("""You guessed the word!
        You survived!""")

    def loser_msg(self):
        print("You lost!")




class HangMan(Ui):
    ATTEMPTS_allowed = 8
    WORD_BANK = ["python", "java", "swift", "javascript"]
    word = random.choice(WORD_BANK)

    def __init__(self):
        self.ui = Ui
        self.known_word_idxs = []
        self.ATTEMPTS_left = self.ATTEMPTS_allowed
        self.partially_revealed: str = "-" * (len(self.word))

    def play(self):
        self.ui.startup_up()
        while self.ATTEMPTS_left:
            self.ui.show_known(self.partially_revealed)
            if self.winner():
                self.ui.winner_msg()
                return
            self.take_letter()
            if self.check_attempt():
                matching_letter_idxs = self.find_letter_idx()
                self.update_know_word_idxs(matching_letter_idxs)
                self.update_partially_revealed()
        self.ui.loser_msg()

    def update_partially_revealed(self):
        full_hiphen = "-" * (len(self.word))
        partially_revealed_list = list(full_hiphen)
        word_list = list(self.word)
        for idx in self.update_know_word_idxs:
            partially_revealed_list[idx] = word_list[idx]
        self.partially_revealed = "".join(partially_revealed_list)

    def take_letter(self):
        self.letter = self.ui.request_letter()

    def check_attempt(self):
        if self.letter not in self.word:
            self.ui.wrong_guess()
            self.count_attempt()
            return False
        else:
            return True

    def count_attempt(self):
        self.ATTEMPTS_made -= 1

    def find_letter_idx(self):
        letter_idxs = [pos for pos, char in enumerate(self.word) if char == self.letter]
        return letter_idxs

    def update_know_word_idxs(self, matching_letter_idxs):
        # verify first that its a new idx and then update
        if matching_letter_idxs[0] not in self.known_word_idxs:  # one idx is is enough since add all of them
            self.known_word_idxs = self.known_word_idxs + matching_letter_idxs
            return
        else:
            self.ui.no_improvment()
            self.count_attempt()
            return

    def winner(self):
        return len(set(self.known_word_idxs)) == len(self.word)


if __name__ == '__main__':
    hangman = HangMan
    hangman.play()



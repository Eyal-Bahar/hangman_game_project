# Write your code here
import random

class Ui:
    def __init__(self):
        pass

    def startup_up(self):
        print("""H A N G M A N\n""")

    def show_known(self, partially_revealed):
        print(f"{partially_revealed}")

    def request_letter(self):
        print("Input a letter:")
        return input()

    def wrong_guess(self):
        print("That letter doesn't appear in the word.")

    def no_improvment(self):
        print("No improvements.")

    def winner_msg(self, word):
        print(f"""You guessed the word {word}!\nYou survived!""")

    def loser_msg(self):
        print("You lost!")

    def input_check_faild(self, reason):
        if reason == "length":
            print("Please, input a single letter.")
            return
        if reason == "case":
            print("Please, enter a lowercase letter from the English alphabet.")
            return
        if reason == "novel input":
            msg = "You've already guessed this letter."
            print(msg)

    def startup_up_menu(self):
        valid_responses = ["play", "results", "exit"]
        response = None
        while response not in valid_responses:
            print("""Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:""")
            response = input()
        return response

    def show_results(self, wins, loses):
        print(f"You won: {wins} times.")
        print(f"You lost: {loses} times.")


class HangMan:
    ATTEMPTS_allowed = 8
    WORD_BANK = ["python", "java", "swift", "javascript"]

    def __init__(self) -> None:
        self.ui = Ui()
        self.restart_game_params()
        self.wins = 0
        self.loses = 0
        self.ui.startup_up()

    def restart_game_params(self):
        self.word = random.choice(self.WORD_BANK)
        self.known_word_idxs = []
        self.ATTEMPTS_left = self.ATTEMPTS_allowed
        self.partially_revealed: str = "-" * (len(self.word))
        self.previous_guesses = []

    def play(self):
        if self.wins + self.loses > 0:
            self.restart_game_params()

        while self.ATTEMPTS_left:
            self.ui.show_known(self.partially_revealed)
            if self.winner():
                self.ui.winner_msg(self.word)
                self.wins += 1
                return
            self.take_letter()
            self.previous_guesses.append(self.letter)
            if self.check_attempt():
                matching_letter_idxs = self.find_letter_idx()
                self.update_know_word_idxs(matching_letter_idxs)
                self.update_partially_revealed()
        self.ui.loser_msg()
        self.loses += 1

    def update_partially_revealed(self):
        full_hiphen = "-" * (len(self.word))
        partially_revealed_list = list(full_hiphen)
        word_list = list(self.word)
        for idx in self.known_word_idxs:
            partially_revealed_list[idx] = word_list[idx]
        self.partially_revealed = "".join(partially_revealed_list)

    def take_letter(self):
        self.letter = self.ui.request_letter()

        while self.check_input_length(self.letter) != "valid length":
            self.ui.input_check_faild("length")
            self.ui.show_known(self.partially_revealed)
            self.letter = self.take_letter()

        while self.check_input_case(self.letter) != "valid case":
            self.ui.input_check_faild("case")
            self.ui.show_known(self.partially_revealed)
            self.letter = self.take_letter()

        while self.check_input_novelty(self.letter) != "novel input":
            self.ui.input_check_faild("novel input")
            self.ui.show_known(self.partially_revealed)
            self.letter = self.take_letter()
        return self.letter

    def check_attempt(self):
        if self.letter not in self.word:
            self.ui.wrong_guess()
            self.count_attempt()
            return False
        else:
            return True

    def count_attempt(self):
        self.ATTEMPTS_left -= 1

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

    def check_input_length(self, letter):
        if len(letter) == 1 and letter != " ":
            return "valid length"
        else:
            return "unvalid"

    def check_input_case(self, letter):
        if letter.islower():
            return "valid case"
        else:
            return "unvalid"

    def check_input_novelty(self, letter):
        if letter not in self.previous_guesses:
            return "novel input"
        else:
            "unvalid"

    def start_up_menu(self):

        play_answer = self.ui.startup_up_menu()
        return play_answer

    def show_results(self):
        self.ui.show_results(self.wins, self.loses)




if __name__ == '__main__':
    hangman = HangMan()
    play_answer = "None"
    while play_answer != "exit":
        play_answer = hangman.start_up_menu()
        if play_answer == "play":
            hangman.play()
        if play_answer == "results":
            hangman.show_results()





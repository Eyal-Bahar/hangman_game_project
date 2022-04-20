# Write your code here
import random

class Winner(Exception):
    pass

def print_missing(word, non_missing_idxs):
    full_hiphen = "-" * (len(word))
    to_show = list(full_hiphen)
    word_list = list(word)
    for idx in non_missing_idxs:
        to_show[idx] = word_list[idx]
    to_show = "".join(to_show)
    print(f"{to_show}")


ATTEMPTS = 8
WORD_BANK = ["python", "java", "swift", "javascript"]
word = random.choice(WORD_BANK)
print("""H A N G M A N"\n""")

non_missing_idxs = []
ATTEMPTS_made = 0
try:
    while ATTEMPTS_made < ATTEMPTS:
        print_missing(word, non_missing_idxs)
        if len(set(non_missing_idxs)) == len(word):
            raise Winner
        print("Input a letter:")
        letter = input()
        if letter not in word:
            print("That letter doesn't appear in the word.")
            ATTEMPTS_made += 1
        else:
            found_letter_idx = [pos for pos, char in enumerate(word) if char == letter]

            if found_letter_idx[0] in non_missing_idxs:
                print("No improvements.")
                ATTEMPTS_made += 1
            non_missing_idxs = non_missing_idxs + found_letter_idx
    print("You lost!")

except Winner:
    print("""You guessed the word!
    You survived!""")
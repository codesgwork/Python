from Seventh_Module import *
import random
Ascii_Art = {0: ("      ",
                 "      ",
                 "      ",),
             1: ("   o   ",
                 "      ",
                 "      ",),
             2: ("   o   ",
                 "   |   ",
                 "      ",),
             3: ("   o   ",
                 "  /|   ",
                 "      ",),
             4: ("   o   ",
                 "  /|\\  ",
                 "      ",),
             5: ("   o   ",
                 "  /|\\  ",
                 "  /   ",),
             6: ("   o   ",
                 "  /|\\  ",
                 "  / \\  "),}
Letters_Guessed = []
Word = random.choice(Words)
Word_Len = len(Word)
Word_Guessed = ["_"] * Word_Len
Wrong_Guesses = 0
while True:
    print(" ".join(Word_Guessed))
    print("\n".join(Ascii_Art[Wrong_Guesses]))
    Guess = input("Guess a letter: ").lower()
    if Guess in Letters_Guessed:
        print("You already guessed that letter.")
    elif Guess in Word:
        for i in range(Word_Len):
            if Word[i] == Guess:
                Word_Guessed[i] = Guess
                Letters_Guessed.append(Guess)
    else:
        Wrong_Guesses += 1
    Letters_Guessed.append(Guess)
    if Wrong_Guesses == 6:
        print("You lose! The word was " + Word + ".")
        break
    if "_" not in Word_Guessed:
        print("You win!")
        break

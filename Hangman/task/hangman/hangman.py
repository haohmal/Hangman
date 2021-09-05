import random

words = ['python', 'java', 'kotlin', 'javascript']
letters = set()
bad_letters = set()


def restart_game():
    letters.clear()
    bad_letters.clear()


def create_result(word):
    hint = ""
    for char in word:
        if char in letters:
            hint += char
        else:
            hint += '-'
    return hint


def play_again():
    while True:
        play = input('Type "play" to play the game, "exit" to quit:')
        if play == 'play':
            return True
        elif play == 'exit':
            return False
        else:
            pass


print("H A N G M A N")
while True:

    tries = 8
    target = random.randint(0, len(words) - 1)
    result = "-" * len(words[target])
    restart_game()
    if not play_again():
        break
    while tries > 0:
        print()
        print(result)
        letter = input("Input a letter:")
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if letter not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a lowercase English letter")
            continue
        if letter in words[target] and letter not in letters:
            letters.add(letter)
            result = create_result(words[target])
            if result == words[target]:
                print(result)
                break
        elif letter in letters or letter in bad_letters:
            print("You've already guessed this letter")
        else:
            bad_letters.add(letter)
            tries -= 1
            print("That letter doesn't appear in the word")
    if result != words[target]:
        print("You lost!")
    else:
        print("You guessed the word!")
        print("You survived!")

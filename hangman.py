import random
def hangman():
    wordlist = ["jurassic", "titanic", "witcher", "moonlight", "castlevania"]
    word = wordlist[random.randint(0, len(wordlist)-1)]
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = raw_input(msg)
        if char in rletters:
            cind = rletters.index(char)
            for index, letra in enumerate(rletters):
                if char in rletters[index]:
                    # print(index)
                    board[index] = char
                    rletters[index] = '$'
            print(rletters)
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

hangman()
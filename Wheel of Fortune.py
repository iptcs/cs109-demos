word = "QUANTUM"

current_board = "_" * len(word)

for guess_count in range(10):
    guess = input(current_board + "Enter a letter: ").upper()
    next_board = ""
    for position in range(len(word)):
        if guess == word[position]:
            next_board = next_board + guess
        else:
            next_board = next_board + current_board[position]

    current_board = next_board
    if current_board == word:
        break

print(current_board)

maze = [["_", "_", "_", "W"],
        ["_", "W", "_", "_"],
        ["_", "W", "W", "_"],
        ["_", "W", "W", "_"]]
start_row = 2
start_col = 0

end_row = 2
end_col = 3

def get_maze_space_contents(row, col):
    if row == end_row and col == end_col:
        return "E"
    elif row == start_row and col == start_col:
        return "S"
    else:
        return maze[row][col]

def pretty_print_maze(player_row, player_col):
    for row_index in range(len(maze)):
        pretty_row = ""
        for col_index in range(len(maze[0])):
            if row_index == player_row and col_index == player_col:
                pretty_row += "P "
            else:
                pretty_row += get_maze_space_contents(row_index, col_index) + " "
        print(pretty_row)

def is_valid_move(player_row, player_col, direction):
    # What location will the player be in
    next_row = player_row
    next_col = player_col

    if direction == "up":
        next_row  -= 1
    elif direction  == "down":
        next_row += 1
    elif direction  == "left":
        next_col -= 1
    elif direction == "right":
        next_col += 1
    
    # Is it off the board
    if next_row < 0 or next_row >= len(maze):
        return False
    if next_col < 0 or next_col >= len(maze[next_row]):
        return False

    # Is it on a wall
    next_space_contents = get_maze_space_contents(next_row, next_col)
    if next_space_contents == "W":
        return False
    else:
        return True
def move(player_row, player_col, direction):
    #Do not change if move is invalid
    if not is_valid_move(player_row, player_col, direction):
        return [player_row, player_col]
    
    # Otherwise return new location
    if direction == "up":
        return [player_row - 1 , player_col]
    if direction == "down":
        return [player_row + 1, player_col]
    if direction == "right":
        return [player_row, player_col + 1]
    if direction == "left":
        return [player_row, player_col + 1]
    return [new_player_row, new_player_call]


def play_game():
    player_row = start_row
    player_col = start_col

    while (player_row != end_row) or (player_col != end_col):
        pretty_print_maze(player_row, player_col)
        direction = input("Enter your move")
        new_player_loc = move(player_row, player_col, direction)
        player_row = new_player_loc[0]
        player_col = new_player_loc[1]
    print("Your mother was a hamster")

play_game()

from random import randrange


def display_board(board):
    for row in board:
        print("+-------" * 3 + "+")
        for _ in range(3):
            print("|       ", end="")
        print("|")
        for square in row:
            print("|   " + square + "   ", end="")
        print("|")
        for _ in range(3):
            print("|       ", end="")
        print("|")
    print("+-------" * 3 + "+")


def enter_move(board):
    while True:
        move = int(input("Enter your move: ")) - 1
        row = move // 3
        col = move % 3
        if 0 <= row <= 2 and 0 <= col <= 2 and (board[row][col] == " " or board[row][col].isdigit()):
            board[row][col] = "O"
            break
        else:
            print("Wrong move. Try again.")


def make_list_of_free_fields(board):
    free_fields = []
    for i, row in enumerate(board):
        for j, square in enumerate(row):
            if square == " " or square.isdigit():
                free_fields.append((i, j))
    return free_fields


def victory_for(board, sign):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == sign for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == sign for j in range(3)]):  # Check column
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:  # Check main diagonal
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:  # Check other diagonal
        return True
    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = free_fields[randrange(len(free_fields))]
        board[move[0]][move[1]] = "X"


# Testing the functions
board = [[str(i * 3 + j + 1) for j in range(3)] for i in range(3)]
board[1][1] = "X"
while True:
    display_board(board)
    if victory_for(board, "X"):
        print("Computer won!")
        break
    elif victory_for(board, "O"):
        print("You won!")
        break
    if len(make_list_of_free_fields(board)) == 0:
        print("Draw!")
        break
    enter_move(board)
    display_board(board)
    if victory_for(board, "O"):
        display_board(board)
        print("You won!")
        break
    draw_move(board)

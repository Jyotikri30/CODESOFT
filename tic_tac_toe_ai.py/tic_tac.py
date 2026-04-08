import random

# Scores
player_score = 0
computer_score = 0

# Show position guide
def show_guide():
    print("\nPosition Guide:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9\n")

# Print board
def print_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Check winner
def check_winner(board, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for c in win_conditions:
        if board[c[0]] == board[c[1]] == board[c[2]] == player:
            return True
    return False

# Player move
def player_move(board):
    move = int(input("Enter your move (1-9): ")) - 1
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Already taken!")
        player_move(board)

# Easy AI
def easy_move(board):
    moves = [i for i in range(9) if board[i] == " "]
    return random.choice(moves)

# Hard AI (basic smart)
def hard_move(board):
    # Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner(board, "O"):
                board[i] = " "
                return i
            board[i] = " "

    # Block player
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner(board, "X"):
                board[i] = " "
                return i
            board[i] = " "

    return easy_move(board)

# Main game
while True:
    board = [" "] * 9

    show_guide()

    level = input("Choose difficulty (easy/hard): ").lower()

    while True:
        print_board(board)

        player_move(board)

        if check_winner(board, "X"):
            print_board(board)
            print("You win! 🎉")
            player_score += 1
            break

        if " " not in board:
            print("Draw!")
            break

        # Computer move
        if level == "hard":
            move = hard_move(board)
        else:
            move = easy_move(board)

        board[move] = "O"
        print(f"Computer chose {move + 1}")

        if check_winner(board, "O"):
            print_board(board)
            print("Computer wins! 🤖")
            computer_score += 1
            break

        if " " not in board:
            print("Draw!")
            break

    print(f"\nScore → You: {player_score} | Computer: {computer_score}")

    replay = input("Play again? (y/n): ").lower()
    if replay != "y":
        print("Thanks for playing! 👋")
        break
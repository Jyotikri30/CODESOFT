import tkinter as tk
import random


BG_COLOR = "#1e1e2f"
BTN_COLOR = "#2e2e3e"
X_COLOR = "#ff4d4d"   
O_COLOR = "#00c2ff"   


board = [""] * 9
player_score = 0
computer_score = 0
difficulty = "easy"


def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False


def reset_board():
    global board
    board = [""] * 9
    result_label.config(text="")
    for btn in buttons:
        btn.config(text="", state="normal", bg=BTN_COLOR)


def update_score():
    score_label.config(text=f"You: {player_score}   AI: {computer_score}")


def easy_move():
    moves = [i for i in range(9) if board[i] == ""]
    return random.choice(moves)


def hard_move():
    
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            if check_winner("O"):
                board[i] = ""
                return i
            board[i] = ""

    for i in range(9):
        if board[i] == "":
            board[i] = "X"
            if check_winner("X"):
                board[i] = ""
                return i
            board[i] = ""

    return easy_move()

# Computer prog
def computer_turn():
    global computer_score

    move = hard_move() if difficulty == "hard" else easy_move()

    board[move] = "O"
    buttons[move].config(text="O")
    buttons[move].config(fg=O_COLOR, disabledforeground=O_COLOR, state="disabled")

    if check_winner("O"):
        computer_score += 1
        update_score()
        result_label.config(text="Computer Wins ", fg=O_COLOR)
        disable_all()
        return

    if "" not in board:
        result_label.config(text="Draw!", fg="white")
        return


def disable_all():
    for btn in buttons:
        btn.config(state="disabled")


def on_click(i):
    global player_score

    if board[i] == "":
        board[i] = "X"
        buttons[i].config(text="X")
        buttons[i].config(fg=X_COLOR, disabledforeground=X_COLOR, state="disabled")

        if check_winner("X"):
            player_score += 1
            update_score()
            result_label.config(text="You Win ", fg=X_COLOR)
            disable_all()
            return

        if "" not in board:
            result_label.config(text="Draw!", fg="white")
            return

        window.after(400, computer_turn)


def set_difficulty(level):
    global difficulty
    difficulty = level
    diff_label.config(text=f"Mode: {level.upper()}")

#  GUI 
window = tk.Tk()
window.title("Tic Tac Toe AI ")
window.config(bg=BG_COLOR)


title = tk.Label(window, text="Tic Tac Toe", font=("Arial", 20, "bold"),
                 bg=BG_COLOR, fg="white")
title.pack(pady=10)


score_label = tk.Label(window, text="You: 0   AI: 0",
                       font=("Arial", 12),
                       bg=BG_COLOR, fg="white")
score_label.pack()


diff_label = tk.Label(window, text="Mode: EASY",
                      bg=BG_COLOR, fg="white")
diff_label.pack()


frame = tk.Frame(window, bg=BG_COLOR)
frame.pack()

buttons = []
for i in range(9):
    btn = tk.Button(frame,
                    text="",
                    width=6,
                    height=3,
                    font=("Arial", 20),
                    bg=BTN_COLOR,
                    fg="white",
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

# Result 
result_label = tk.Label(window, text="",
                        font=("Arial", 14),
                        bg=BG_COLOR)
result_label.pack(pady=10)

# Controls
control_frame = tk.Frame(window, bg=BG_COLOR)
control_frame.pack()

tk.Button(control_frame, text="Easy",
          command=lambda: set_difficulty("easy")).grid(row=0, column=0, padx=5)

tk.Button(control_frame, text="Hard",
          command=lambda: set_difficulty("hard")).grid(row=0, column=1, padx=5)

tk.Button(control_frame, text="Restart",
          command=reset_board).grid(row=0, column=2, padx=5)


window.mainloop()

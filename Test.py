import customtkinter as ctk
from tkinter import messagebox

def is_winner(board1, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    return any(board1[a] == board1[b] == board1[c] == player for a, b, c in win_conditions)

def is_board_full(board2):
    return ' ' not in board2

def get_empty_positions(board3):
    return [x for x, spot in enumerate(board3) if spot == ' ']

def minimax(board4, depth, is_maximizing):
    if is_winner(board4, 'O'):
        return 1
    if is_winner(board4, 'X'):
        return -1
    if is_board_full(board4):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for pos in get_empty_positions(board4):
            board4[pos] = 'O'
            score = minimax(board4, depth + 1, False)
            board4[pos] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for pos in get_empty_positions(board4):
            board4[pos] = 'X'
            score = minimax(board4, depth + 1, True)
            board4[pos] = ' '
            best_score = min(score, best_score)
        return best_score

def computer_move():
    best_score = float('-inf')
    best_move = None
    for pos in get_empty_positions(board):
        board[pos] = 'O'
        score = minimax(board, 0, False)
        board[pos] = ' '
        if score > best_score:
            best_score = score
            best_move = pos
    board[best_move] = 'O'
    buttons[best_move].configure(text='O', state="disabled", fg_color="gray")

def check_game_over():
    if is_winner(board, 'X'):
        messagebox.showinfo("Tic Tac Toe", "Congratulations! You have won!")
        label.place(relx=0.5, rely=0.5, anchor='center')
        restart_button.place(relx=0.5, rely=0.5, anchor="center")
    elif is_winner(board, 'O'):
        messagebox.showinfo("Tic Tac Toe", "The computer has won!")
        label.place(relx=0.5, rely=0.5, anchor='center')
        restart_button.place(relx=0.5, rely=0.5, anchor="center")
    elif is_board_full(board):
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        label.place(relx=0.5, rely=0.5, anchor='center')
        restart_button.place(relx=0.5, rely=0.5, anchor="center")

def player_move(position):
    if board[position] == ' ':
        board[position] = 'X'
        buttons[position].configure(text='X', state="disabled", fg_color="#3A7C3A")
        check_game_over()
        if not is_board_full(board):
            computer_move()
            check_game_over()
    else:
        messagebox.showwarning("Tic Tac Toe", "This position is already taken!")

def restart_game():
    global board
    board = [' ' for _ in range(9)]
    for button1 in buttons:
        button1.configure(text=' ', state="normal", fg_color='#2fa572')
    restart_button.place_forget()
    label.place_forget()


root = ctk.CTk()
root.title("Tic Tac Toe")
root.iconbitmap("logox.ico")
root.geometry("400x400")
root.resizable(width=False, height=False)
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
root.grid_columnconfigure((0, 1, 2), weight=1)
root.grid_rowconfigure((0, 1, 2), weight=1)

button_style = {"width": 100, "height": 100, "corner_radius": 10, "font": ("Arial", 20)}
board = [' ' for _ in range(9)]
buttons = []


for i in range(9):
    button = ctk.CTkButton(root, text=' ', command=lambda i=i: player_move(i), **button_style, fg_color='#2fa572')
    button.grid(row=i // 3, column=i % 3, padx=0, pady=0)
    buttons.append(button)

label = ctk.CTkLabel(master=root, width=400, height=200)
restart_button = ctk.CTkButton(label, text="Restart", command=restart_game, width=100, height=50, corner_radius=10,
                               font=("Arial", 15))

root.mainloop()

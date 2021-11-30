board = ["     ", "     ", "     ",   
         "     ", "     ", "     ",
         "     ", "     ", "     "]

game_ongoing = True
winner = None
curr_player = "  X  "

def displayboard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----------------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----------------")
    print(board[6] + "|" + board[7] + "|" + board[8])

def game():
    #initial board
    displayboard()

    while game_ongoing:
        #current turn
        turn(curr_player)
        #check if game is over
        is_game_over()
        #switch player
        flip_player()

    #after game is done
    if winner == "  X  " or winner == "  O  ":
        print("\n",winner + "won the game!\n")
    elif winner == None:
        print('\nTie!\n')
    

def turn(player):
    if player == "  X  ":
        p = player_1
    elif player == "  O  ":
        p = player_2
    print("\n", p + "'s turn.\n")
    position = input("Choose box (1-9): ")
    unfilled = False
    while not unfilled:
        while position not in ["1", "2", "3", "4","5" , "6", "7", "8", "9"]:
            position = (input("Invalid input. Choose box (1-9): "))
        position = int(position)
        if board[position-1] == "     ":
            unfilled = True
        else:
            position = input("Position already filled. Choose another box: ")

    board[position-1] = player
    displayboard()

def is_game_over():
    check_win()
    check_tie()
 
def check_win():
    global winner
    global game_ongoing
    row1 = board[0] == board[1] == board[2] != "     "
    row2 = board[3] == board[4] == board[5] != "     "
    row3 = board[6] == board[7] == board[8] != "     "
    column1 = board[0] == board[3] == board[6] != "     "
    column2 = board[1] == board[4] == board[7] != "     "
    column3 = board[2] == board[5] == board[8] != "     "
    diag1 = board[0] == board[4] == board[8] != "     "
    diag2 = board[2] == board[4] == board[6] != "     "
    if row1 or row2 or row3 or column1 or column2 or column3 or diag1 or diag2:
        #game ends
        game_ongoing = False
    if row1:
        winner = board[0]
    elif row2:
        winner = board[3]
    elif row3:
        winner = board[6]
    elif column1:
        winner = board[0]
    elif column2:
        winner = board[1]
    elif column3:
        winner = board[2]
    elif diag1:
        winner = board[4]
    elif diag2:
        winner = board[4]
    else:
        winner = None
    return

def check_tie():
    global game_ongoing
    if "     " not in board:
        game_ongoing = False
    return

def flip_player():
    global curr_player
    if curr_player == "  X  ":
        curr_player = "  O  "
    elif curr_player == "  O  ":
        curr_player = "  X  "
    return

def reset():
    global board
    global game_ongoing
    board = ["     ", "     ", "     ",
             "     ", "     ", "     ",
             "     ", "     ", "     "]
    game_ongoing = True


if __name__ == "__main__":
    while True:

        print("Choose:\n1.Play gam1e\n2.Exit game")
        choice = int(input())
        if choice == 1:
            print("Player 1: ")
            player_1 = input("Enter name: ")
            print("\n")
            print("Player 2: ")
            player_2 = input("Enter name: ")
            print("\n")

            #play the game
            game()
            reset()

        elif choice == 2:
            print("Thanks for playing!")
            break

        else:
            print("Enter a valid choice")







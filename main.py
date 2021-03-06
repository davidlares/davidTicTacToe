from board import Board

if __name__ == "__main__":

    board = Board()
    board.wipe_screen()

    while True:
        # Get X input
        x = int(input("\n X turn - Please choose [1 - 9]: "))
        
        if x >= 10 or x < 1:
            print("Invalid Number, exiting \n")
            break

        board.set_choice(x,"X")

        if board.is_winner("X"):
            board.wipe_screen() # for showing final results
            print("\n Congrats! X Player Wins! \n")
            break

        # Get O input (AI Intended)
        board.opponent_move("O") # default AI player
        board.wipe_screen() # showing "realtime results"

        if board.is_winner("O"):
            board.wipe_screen() # for showing final results
            print("\n Congrats! O Player Wins! \n")
            break

from board import Board

board = Board()

player1 = "O"
player2 = "X"

players = [player1, player2]

print("welcome to Tic Tac Toe!")
print(f"For this round, player O will go first!\n")
input("Hit Enter to continue")

header = """
        Available   TIC-TAC-TOE
         Moves
        """


win = False

available_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
user_moves = ["", "", "", "", "", "", "", "", ""]


while not win:

    for player in players:
        print(header)
        board.show_board(available_moves, user_moves)
        user_input = input(f"Player {player}, choose your next position: (1-9)")
        position = int(user_input)

        if isinstance(position, int) and 1 <= position <= 9:
            # add user move to user_moves list
            user_moves[int(position) - 1] = player
            # remove number form available moves list
            available_moves[int(position) - 1] = ""

            win = board.win(user_moves, player)
            if win:
                break
        else:
            print("please Enter a value between 1-9")
            win = True
            break


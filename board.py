
class Board:

    def __init__(self):
        pass

    def show_board(self, available_moves: list, user_moves: list):
        """
        This Function will take predifine list form tik_tak_toe.py file, and It will be dynamically changed in there
        :param available_moves:
        :param user_moves:
        :return: board
        """

        print(f"      {available_moves[0]} | {available_moves[1]} | {available_moves[2]}     {user_moves[0]}| {user_moves[1]} | {user_moves[2]}    ")
        print("      ---------    -------  ")
        print(f"      {available_moves[3]} | {available_moves[4]} | {available_moves[5]}     {user_moves[3]}| {user_moves[4]} | {user_moves[5]}    ")
        print("      ---------    -------  ")
        print(f"      {available_moves[6]} | {available_moves[7]} | {available_moves[8]}     {user_moves[6]}| {user_moves[7]} | {user_moves[8]}    ")
        print("      ---------    -------  ")



    def win(self, user_moves: list, player):
        """
        This function will decide if a player won or not
        :param user_moves:
        :param player:
        :return: bool
        """

        if user_moves[0] == player and user_moves[1] == player and user_moves[2] == player or \
           user_moves[3] == player and user_moves[4] == player and user_moves[5] == player or \
           user_moves[6] == player and user_moves[7] == player and user_moves[8] == player or \
           user_moves[0] == player and user_moves[3] == player and user_moves[6] == player or \
           user_moves[1] == player and user_moves[4] == player and user_moves[7] == player or \
           user_moves[2] == player and user_moves[5] == player and user_moves[8] == player or \
           user_moves[0] == player and user_moves[4] == player and user_moves[8] == player or \
           user_moves[2] == player and user_moves[4] == player and user_moves[6] == player:
            print(f"Congratulations! player {player} wins !")
            return True
        else:
            return False





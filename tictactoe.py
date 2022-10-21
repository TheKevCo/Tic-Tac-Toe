from art import logo


class TicTacToe:
    def __init__(self):
        self.row1 = ["⬜", "⬜", "⬜"]
        self.row2 = ["⬜", "⬜", "⬜"]
        self.row3 = ["⬜", "⬜", "⬜"]
        self.board = [self.row1, self.row2, self.row3]
        print(f"{logo}\n\nWelcome to the Tic Tac Toe Game!\n\n")
        print(f"C  O  L  U  M  N\n{self.row1} R\n{self.row2} O\n{self.row3} W\n")
        self.x = '❌'
        self.o = '⭕'

    def coordinate_check(self, coordinates):
        if self.board[coordinates[0]][coordinates[1]] == self.x:
            print("A player has already placed a move here, choose different coordinates")
            return False
        elif self.board[coordinates[0]][coordinates[1]] == self.o:
            print("A player has already placed a move here, choose different coordinates")
            return False
        for value in coordinates:
            if value >= 3:
                print("You entered too big of a coordinate, only select from 1-3 for a column and row")
                return False

        return True

    def win_condition(self):
        # There are 8 win conditions in tic-tac-toe, this function accounts for all 8.

        column_1 = []
        column_2 = []
        column_3 = []

        # checks horizontal wins
        # creates columns for us to check vertical and diagonal wins later

        for row in self.board:
            if row[0] + row[1] + row[2] == "❌❌❌":
                print('User 1 has won the game!')
                return True
            elif row[0] + row[1] + row[2] == "⭕⭕⭕":
                print('User 2 has won the game!')
                return True
            else:
                column_1.append(row[0])
                column_2.append(row[1])
                column_3.append(row[2])

        # vertical checker
        column_board = [column_1, column_2, column_3]
        for column in column_board:
            if column[0] + column[1] + column[2] == "❌❌❌":
                print('User 1 has won the game!')
                return True
            elif column[0] + column[1] + column[2] == "⭕⭕⭕":
                print('User 2 has won the game!')
                return True

        # diagonal checker
        if column_1[0] + column_2[1] + column_3[2] == "❌❌❌":
            print('User 1 has won the game!')
            return True
        elif column_1[0] + column_2[1] + column_3[2] == "⭕⭕⭕":
            print('User 2 has won the game!')
            return True
        elif column_1[2] + column_2[1] + column_3[0] == "❌❌❌":
            print('User 1 has won the game!')
            return True
        elif column_1[2] + column_2[1] + column_3[0] == "⭕⭕⭕":
            print('User 1 has won the game!')
            return True

        # draw
        blank_space = False
        for row in self.board:
            for mark in row:
                if mark == "⬜":
                    blank_space = True
        if not blank_space:
            print('No more moves, game is tied')
            return True
        else:
            return False

    def game_start(self):
        while not self.win_condition():
            valid_move_user_1 = False
            while not valid_move_user_1:
                user_1 = input("User 1, please input a choice in the form of coordinates (column/row), ex. 12 or 22: ")
                user_1_coordinates = [(int(user_1[1]) - 1), (int(user_1[0]) - 1)]
                if self.coordinate_check(user_1_coordinates):
                    valid_move_user_1 = True
            self.board[user_1_coordinates[0]][user_1_coordinates[1]] = self.x
            print(f"{self.row1}\n{self.row2}\n{self.row3}")
            if self.win_condition():
                break
            valid_move_user_2 = False
            while not valid_move_user_2:
                user_2 = input("User 2, please input a choice in the form of coordinates (column/row), ex. 12 or 22: ")
                user_2_coordinates = [(int(user_2[1]) - 1), (int(user_2[0]) - 1)]
                if self.coordinate_check(user_2_coordinates):
                    valid_move_user_2 = True
            self.board[user_2_coordinates[0]][user_2_coordinates[1]] = self.o
            print(f"{self.row1}\n{self.row2}\n{self.row3}")
            if self.win_condition():
                break

        print('GG!')

from numpy import random
from collections import Counter
outcomes = ["Empty", "🔴", "⚫️" ]
# board_size = int(input("Enter a board size between  4 and 16: "))
#
red = "🔴"
def build_board(board_size):
    outcomes = ["Empty", "🔴", "⚫️"]
    newly_created_board = random.choice(outcomes, (board_size,board_size))
    return newly_created_board
# new_board = build_board((board_size))
# print(new_board)



def get_count(board, outcome):
    counter = 0
    for row in board:
        for item in row:
            if item == outcome:
                counter += 1
                print(get_count(board, item))
    return counter
#print(get_count(new_board, "Empty"))


official_name = __name__
if official_name == "__main__":
    print("This file is not intended to be run as a main")
else:
    print(f"Current version: {official_name}")
#get_count(newly_created_board=)


import checkers
current_name = __name__
# Check if running as __main__
if current_name == "__main__":

    def game():
        board_size = int(input("Choose a board size between 4 and 16: "))
        new_board = checkers.build_board(board_size=board_size)
        print(new_board)

        return
    game()
        # board_count = checkers.get_count(newly_created_board=new_board,outcomes=new_board )
        # print(board_count)
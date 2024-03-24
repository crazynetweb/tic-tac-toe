def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"\nPlayer {player}'s turn")

        # Ask for player input
        while True:
            try:
                row = int(input("Enter row (1-3): ")) - 1
                col = int(input("Enter column (1-3): ")) - 1
                if board[row][col] == " ":
                    break
                else:
                    print("That cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 3.")

        board[row][col] = player
        print_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            break
        elif all(cell != " " for row in board for cell in row):
            print("It's a tie!")
            break

        turn += 1


if __name__ == "__main__":
    main()

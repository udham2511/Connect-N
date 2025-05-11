def display() -> None:
    """displays board on shell"""
    print("Board:")
    output = "   "

    for col in range(cols):
        output += f"[{col}]"

    print(output)

    for row in range(rows):
        output = f"[{row:2}]"

        for col in range(cols):
            output += f"{disks[board[row][col]]:2}"

        print(output)


def dropDisk(column: int, player: int) -> bool:
    """drops disk in last empty row of given column

    Args:
        column (int): column number
        player (int): which player's turn

    Returns:
        bool: legal or illegal move
    """
    for row in range(rows - 1, -1, -1):
        if board[row][column] == 0:
            board[row][column] = player
            return True

    return False


def haveWinner() -> bool:
    """checks if someone won!

    Returns:
        bool: if player has won or not.
    """
    for row in range(rows):
        for num in range(cols - N + 1):
            values = [board[row][num + n] for n in range(N)]

            if values.count(1) == N or values.count(2) == N:
                return True

    for col in range(cols):
        for num in range(rows - N + 1):
            values = [board[num + n][col] for n in range(N)]

            if values.count(1) == N or values.count(2) == N:
                return True

    for num in range(N - 1, rows):
        i = num
        j = 0

        diagonal = []

        while i >= 0 and j < cols:
            diagonal.append(board[i][j])
            i -= 1
            j += 1

        for n in range(len(diagonal) - N + 1):
            values = [x for x in diagonal[n : n + N]]

            if values.count(1) == N or values.count(2) == N:
                return True

    for num in range(1, cols - (N - 1)):
        i = rows - 1
        j = num

        diagonal = []

        while i >= 0 and j < cols:
            diagonal.append(board[i][j])
            i -= 1
            j += 1

        for n in range(len(diagonal) - N + 1):
            values = [x for x in diagonal[n : n + N]]

            if values.count(1) == N or values.count(2) == N:
                return True

    for num in range(N - 1, cols):
        i = rows - 1
        j = num

        diagonal = []

        while i >= 0 and j >= 0:
            diagonal.append(board[i][j])

            i -= 1
            j -= 1

        for n in range(len(diagonal) - N + 1):
            values = [x for x in diagonal[n : n + N]]

            if values.count(1) == N or values.count(2) == N:
                return True

    for num in range(rows - 2, N - 2, -1):
        i = num
        j = cols - 1

        diagonal = []

        while i >= 0 and j >= 0:
            diagonal.append(board[i][j])

            i -= 1
            j -= 1

        for n in range(len(diagonal) - N + 1):
            values = [x for x in diagonal[n : n + N]]

            if values.count(1) == N or values.count(2) == N:
                return True

    return False


N = input("Please enter value of N: ")

if not N.isdigit():
    raise TypeError("N must be integer")

N = int(N)

if N < 3:
    raise ValueError("N must be greater than 2")

rows = N + 3
cols = N + 2

disks = ["\u2B1C", "\u26AA", "\u26AB"]
board = [[0] * cols for _ in range(rows)]

player = 0

display()
while True:
    column = input(f"Player {player} select column: ")

    if column == "q":
        print(f"Player {player} resigend!")
        break

    elif not column.isdigit():
        print("column number must be an integer")
        continue

    elif int(column) > cols - 1:
        print(f"column must be in range (0 -> {cols - 1})")
        continue

    isLegal = dropDisk(int(column), player + 1)

    if not isLegal:
        print(f"Column {column} is an illegal move!")
        continue

    display()

    if haveWinner():
        print(f"Player {player} won!")
        break

    player = (player + 1) % 2

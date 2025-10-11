board = ["[ ]" for _ in range(9)]

for x, board_tile in enumerate((board), 1):
    if x % 3 == 0:
        print(board_tile, "\n")
    else:
        print(board_tile, end=" ")
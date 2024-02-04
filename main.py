from random import randint

row1 = ["1", "2", "3"]
row2 = ["1", "2", "3"]
row3 = ["1", "2", "3"]
board = [row1, row2, row3]

def main(board):
    print("Ваш ход. Пишите так: СТРОКАстолб (пример: 12)")
    turny, turnx = (int(i) - 1 for i in (input()))
    if board[turny][turnx] not in ("X", "O"):
        board[turny][turnx] = "X"
        board = computer(board)
        output(board)

    else:
        print("Сдесь уже занято")
    main(board)

def computer(board2):
    compx = randint(0,2)
    compy = randint(0,2)
    print(compx, compy)
    if board[compy][compx] not in ("X", "O"):
        board2[compx][compy] = "O"
    else:
        computer(board2)
    return board2
def output(board1):
    for i in board1:
        print(i)


output(board)
main(board)
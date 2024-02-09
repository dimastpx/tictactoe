from random import randint


row1 = ["1", "2", "3"]
row2 = ["1", "2", "3"]
row3 = ["1", "2", "3"]
board = [row1, row2, row3]


def main(board):
    print("Ваш ход. Пишите так: столб строка (пример: 12)")
    turnx, turny = (int(i) - 1 for i in (input()))
    if board[turny][turnx] not in ["X", "O"]:
        board[turny][turnx] = "X"
        board = computer(board)
        output(board)
        win_check(board)

    else:
        print("Сдесь уже занято")
    main(board)

def computer(board2):
    compx = randint(0,2)
    compy = randint(0,2)
    print(compy + 1, compx + 1)
    if board2[compy][compx] not in ["x","0"]:
        board2[compx][compy] = "O"
    else:
        computer(board2)
    return board2
def output(board1):
    for i in board1:
        print(i)

def win_check(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            print("You win!")
            exit()



root.mainloop()
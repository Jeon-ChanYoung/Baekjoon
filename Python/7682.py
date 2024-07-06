visit = []

def gettingAllCase(board, turn):
    if isFinished(board):
        visit.append([row[:] for row in board])
        return
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                board[i][j] = "X" if turn else "O"
                gettingAllCase(board, not turn)
                board[i][j] = "."

def check_winner(board, mark):
    # 가로 세로
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)) or all(board[j][i] == mark for j in range(3)):
            return True
    # 대각선
    if board[0][0] == board[1][1] == board[2][2] == mark or board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False

def isFinished(board):
    if check_winner(board, "X") or check_winner(board, "O"):
        return True
    
    for row in board:
        if "." in row:
            return False
    return True

gettingAllCase([["."]*3 for _ in range(3)], True)
for board in iter(input, "end"):
    board = [list(board[3*i:3*i+3]) for i in range(3)]

    if board in visit:
        print("valid")
    else:
        print("invalid")

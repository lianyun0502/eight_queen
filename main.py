import numpy as np

queen_num = 8
ans_num = 0
def main():
 
    board = np.zeros((queen_num, queen_num), dtype='int8')
    set_queen(0, board)

    pass


def show_answer(board:np.ndarray):
    global ans_num
    ans_num = ans_num + 1
    print(f"Answer {ans_num}------------------")
    print(board)
    pass

def set_queen(queen_idx:int, board:np.ndarray)->bool:
    global queen_num
    if queen_idx == queen_num: # last queen is set
        show_answer(board)
        return True # answer is found
    
    for i in range(queen_num):
        for j in range(queen_num):
            if board[i][j] == 0:
                board_copy = board.copy()
                board_copy[i][j] = 2
                board_after_disable = set_disable_position(i, j, board_copy)
                set_queen(queen_idx+1, board_after_disable)

    return False # no answer
    pass

def set_disable_position(i:int, j:int, board:np.ndarray)->np.ndarray:
    for k in range(queen_num):
        if board[i][k] == 0:
            board[i][k] = 1
        if board[k][j] == 0:
            board[k][j] = 1
        if i+k < queen_num and j+k < queen_num:
            if board[i+k][j+k] == 0:
                board[i+k][j+k] = 1
        if i+k < queen_num and j-k >= 0:
            if board[i+k][j-k] == 0:
                board[i+k][j-k] = 1
        if i-k >= 0 and j+k < queen_num:
            if board[i-k][j+k] == 0:
                board[i-k][j+k] = 1
        if i-k >= 0 and j-k >= 0:
            if board[i-k][j-k] == 0:
                board[i-k][j-k] = 1
    return board

main()

import numpy as np

queen_num = 8
ans_num = 0
division_8 = 0
division_4 = 0
division_2 = 0

def main():
    global queen_num, ans_num, division_8, division_4, division_2
    board = np.zeros((queen_num, queen_num), dtype='int8')
    set_queen(0, board)
    print(f"Total answer: {ans_num}")
    ans_num = ans_num - division_8
    ans_num = ans_num - division_4
    ans_num = ans_num - division_2
    print(f"Total indiviual answer: {ans_num+(division_8//8)+(division_4//4)+(division_2//2)}")
    pass

def check_is_rotate_180(board:np.ndarray)->bool:
    global queen_num
    board_rotate = np.zeros((queen_num, queen_num), dtype='int8')
    for i in range(queen_num):
        for j in range(queen_num):
            board_rotate[i][j] = board[queen_num-i-1][queen_num-j-1]
    if np.array_equal(board, board_rotate):
        return True
    return False

def check_is_rotate_90(board:np.ndarray)->bool:
    global queen_num
    board_rotate = np.zeros((queen_num, queen_num), dtype='int8')
    for i in range(queen_num):
        for j in range(queen_num):
            board_rotate[i][j] = board[j][queen_num-i-1]
    if np.array_equal(board, board_rotate):
        return True
    return False

def check_is_mirror(board:np.ndarray)->bool:
    global queen_num
    board_mirror = np.zeros((queen_num, queen_num), dtype='int8')
    for i in range(queen_num):
        for j in range(queen_num):
            board_mirror[i][j] = board[i][queen_num-j-1]
    if np.array_equal(board, board_mirror):
        return True
    return False

def check_is_symmetry_1(board:np.ndarray)->bool:
    global queen_num
    for i in range(queen_num):
        for j in range(queen_num):
            if board[i][j] == 2:
                if board[i][j] != board[queen_num-i-1][j]:
                    return False
    return True

def check_is_symmetry_2(board:np.ndarray)->bool:
    global queen_num
    for i in range(queen_num):
        for j in range(queen_num):
            if board[i][j] == 2:
                if board[i][j] != board[i][queen_num-j-1]:
                    return False
    return True

def check_is_symmetry_3(board:np.ndarray)->bool:
    global queen_num
    for i in range(queen_num):
        for j in range(queen_num):
            if board[i][j] == 2:
                if board[i][j] != board[j][i]:
                    return False
    return True

def check_individual_answer(board:np.ndarray):
    global queen_num, division_8, division_4, division_2
    up_down_symmetry = check_is_symmetry_1(board)
    left_right_symmetry = check_is_symmetry_2(board)
    diagnal_symmetry = check_is_symmetry_3(board)
    rotated_90 = check_is_rotate_90(board)
    rotated_180 = check_is_rotate_180(board)

    if rotated_180: 
        if not (up_down_symmetry and left_right_symmetry and diagnal_symmetry):
            if rotated_90:
                division_2 = division_2 + 1
            else:
                division_4 = division_4 + 1
    else:
        division = 3
        if up_down_symmetry:
            division = division - 1
        if left_right_symmetry:
            division = division - 1
        if diagnal_symmetry:
            division = division - 1

        if division == 3: 
            division_8 = division_8 + 1
        elif division == 2:
            division_4 = division_4 + 1
        elif division == 1:
            division_2 = division_2 + 1

    print('is up down symmetry: ', up_down_symmetry)
    print('is left right symmetry: ', left_right_symmetry)
    print('is diagnal symmetry: ', diagnal_symmetry)
    print('is rotate 90: ', rotated_90)
    print('is rotate 180: ', rotated_180)

def show_answer(board:np.ndarray):
    global ans_num
    ans_num = ans_num + 1
    
    print(f"Answer {ans_num}------------------")
    check_individual_answer(board)
    for i in range(queen_num):
        for j in range(queen_num):
            if board[i][j] == 2:
                print("Q", end="")
            else:
                print(".", end="")
        print()
    pass

def set_queen(queen_idx:int, board:np.ndarray)->bool:
    global queen_num
    if queen_idx == queen_num: # last queen is set
        show_answer(board)
        return True # answer is found
    
    for i in range(queen_num):
        for j in range(queen_num-queen_idx):
            if board[i][j+queen_idx] == 0:
                board_copy = board.copy()
                board_copy[i][j+queen_idx] = 2
                board_after_disable = set_disable_position(i, j+queen_idx, board_copy)
                set_queen(queen_idx+1, board_after_disable)

    return False # no answer


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

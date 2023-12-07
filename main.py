import numpy as np
import time
queen_num = 8 # number of queens
ans_num = 0 # number of answers
division_8 = 0 # number answers have 8 family members
division_4 = 0 # number answers have 4 family members
division_2 = 0 # number answers have 2 family members

def main():
    '''
    start function.
    '''
    s = time.time() # 計算程式執行時間 s = start time
    global queen_num, ans_num, division_8, division_4, division_2
    board = np.zeros((queen_num, queen_num), dtype='int8') 
    set_queen(0, board)
    print(f"Total answer: {ans_num}")

    
    # 獨立解的個數為總解減去旋轉對稱解的個數 
    ans_num = ans_num - division_8
    ans_num = ans_num - division_4
    ans_num = ans_num - division_2
    print(f"Total indiviual answer: {ans_num+(division_8//8)+(division_4//4)+(division_2//2)}")
    print(f"Total time: {time.time()-s}")
    pass

def check_is_rotate_180(board:np.ndarray)->bool:
    '''
    判斷此解是否為旋轉180對稱解
    '''
    global queen_num
    board_rotate = np.zeros((queen_num, queen_num), dtype='int8')
    for i in range(queen_num):
        for j in range(queen_num):
            board_rotate[i][j] = board[queen_num-i-1][queen_num-j-1]
    if np.array_equal(board, board_rotate):
        return True
    return False

def check_is_rotate_90(board:np.ndarray)->bool:
    '''
    判斷此解是否為旋轉90對稱解
    '''
    global queen_num
    board_rotate = np.zeros((queen_num, queen_num), dtype='int8')
    for i in range(queen_num):
        for j in range(queen_num):
            board_rotate[i][j] = board[j][queen_num-i-1]
    if np.array_equal(board, board_rotate):
        return True
    return False

def check_is_mirror(board:np.ndarray)->bool:
    '''
    判斷此解是否為鏡像對稱解
    '''
    global queen_num
    board_mirror = np.zeros((queen_num, queen_num), dtype='int8')
    for i in range(queen_num):
        for j in range(queen_num):
            board_mirror[i][j] = board[i][queen_num-j-1]
    if np.array_equal(board, board_mirror):
        return True
    return False

def check_is_symmetry_1(board:np.ndarray)->bool:
    '''
    判斷此解是否為上下對稱解
    '''
    global queen_num
    for i in range(queen_num):
        for j in range(queen_num):
            if board[i][j] == 2:
                if board[i][j] != board[queen_num-i-1][j]:
                    return False
    return True

def check_is_symmetry_2(board:np.ndarray)->bool:
    '''
    判斷此解是否為左右對稱解
    '''
    global queen_num
    for i in range(queen_num):
        for j in range(queen_num):
            if board[i][j] == 2:
                if board[i][j] != board[i][queen_num-j-1]:
                    return False
    return True

def check_is_symmetry_3(board:np.ndarray)->bool:
    '''
    判斷此解是否為對角對稱解
    '''
    global queen_num
    for i in range(queen_num):
        for j in range(queen_num):
            if board[i][j] == 2:
                if board[i][j] != board[j][i]:
                    return False
    return True

def check_individual_answer(board:np.ndarray):
    '''
    判斷此解是否為獨立解，並印出此解的形式
    '''
    global queen_num, division_8, division_4, division_2
    up_down_symmetry = check_is_symmetry_1(board)
    left_right_symmetry = check_is_symmetry_2(board)
    diagnal_symmetry = check_is_symmetry_3(board)
    rotated_90 = check_is_rotate_90(board)
    rotated_180 = check_is_rotate_180(board)
    '''
    所有旋轉對稱解的形式歸納出有四種，分別為：
    1. 有八種對稱解 : 旋轉180度後不相等且上下、左右、斜對角皆對稱
    2. 有四種對稱解 : 
        1. 旋轉180度後不相等且上下、左右、斜對角有兩種對稱
        2. 旋轉180度後相等且旋轉90度後相等且上下、左右、斜對角都不對稱
    3. 有兩種對稱解 : 
        1. 旋轉180度後不相等且上下、左右、斜對角有一種對稱
        2. 旋轉180度後相等但旋轉90度後不相等且上下、左右、斜對角都不對稱
    4. 無對稱解
    '''
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
    '''
    依照答案的二維矩陣印出題目要求的輸出格式
    '''
    # check_individual_answer(board) # 判斷此解是否為獨立解 不判斷對稱解可註解此行
    for i in range(queen_num):
        for j in range(queen_num):
            if board[i][j] == 2:
                print("Q", end="")
            else:
                print(".", end="")
        print()
    pass

def set_queen(queen_idx:int, board:np.ndarray)->bool:
    '''
    我採用遞迴的方式來解此題，每次遞迴都會將queen_idx+1，直到queen_idx == queen_num，
    這代表所有皇后都已經放置完成，為一組答案。
    '''
    global queen_num, ans_num
    if queen_idx == queen_num: # 最後一個皇后有位置放置，代表找到一組答案
            
        ans_num = ans_num + 1
        print(f"Answer {ans_num}------------------")
        show_answer(board) # 印出答案 不印出答案可註解此行
        return True # answer is found
    
    for i in range(queen_num):
        for j in range(queen_num-queen_idx):
            if board[i][j+queen_idx] == 0: 
                board_copy = board.copy() # 這裡需要copy一份新的棋盤，用於回溯不適答案的狀況
                board_copy[i][j+queen_idx] = 2 # 置入皇后
                board_after_disable = set_disable_position(i, j+queen_idx, board_copy)
                set_queen(queen_idx+1, board_after_disable) # 遞迴放置下一個皇后的步驟

    return False # no answer


def set_disable_position(i:int, j:int, board:np.ndarray)->np.ndarray:
    '''
    當皇后被放置後，將會將皇后的攻擊範圍設為1，並回傳新的棋盤作為下次遞迴的棋盤
    '''
    for k in range(queen_num):
        if board[i][k] == 0: # 將row = k 全設為1
            board[i][k] = 1
        if board[k][j] == 0: # 將column = k 全設為1
            board[k][j] = 1
        if i+k < queen_num and j+k < queen_num: # 將右下斜線全設為1
            if board[i+k][j+k] == 0:
                board[i+k][j+k] = 1
        if i+k < queen_num and j-k >= 0: # 將左下斜線全設為1
            if board[i+k][j-k] == 0:
                board[i+k][j-k] = 1
        if i-k >= 0 and j+k < queen_num:  # 將右上斜線全設為1
            if board[i-k][j+k] == 0:
                board[i-k][j+k] = 1
        if i-k >= 0 and j-k >= 0: # 將左上斜線全設為1
            if board[i-k][j-k] == 0:
                board[i-k][j-k] = 1
    return board

main()

def solve_puzzle(board, index = 0, used = None): # Make sure to add input parameters here


    if used is None:
        used = []

    if index == len(board) - 1: 
        return True
    if index in used:
        return False
   
    used.append(index)

    num = board[index]
    index_add = float('inf')
    index_sub = float('inf') * -1

    if index + num > len(board) - 1:
        while index_add > len(board) - 1:
            index_add = index + num - len(board)
    else:
        index_add = index + num

    if index - num < 0: 
        while index_sub < 0:
            index_sub = index - num + len(board)
    else:
        index_sub = index - num
    
    if solve_puzzle(board, index_add, used) == True:
        return True  
    elif solve_puzzle(board, index_sub, used) == True:
        return True
    else:
        return False    


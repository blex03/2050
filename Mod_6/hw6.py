# TODO: implement the following 3 functions. Use docstrings, whitespace, and comments.

from statistics import median


def cocktail_sort(L): 
    for iterator in range(len(L)//2):
        for i in range(len(L) - 1 - iterator):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
        
        for j in range(len(L) - 1 - iterator - 1):
            if L[-1 - j - 1] < L[-1 - j -2]:
                L[-1 - j - 1], L[-1 - j - 2] = L[-1 - j - 2], L[-1 - j - 1]
    
    return L

def bs_sublist(L, left, right, item): 
    
    median = ((right + left)//2)      #New Median
    
    if (right - left) < 2:            #Base Case
        if item > L[right]:
            return right
        elif item <= L[left]:
            return left - 1
        else:
            return left
                
    if item < L[median]:              #Recur
        return bs_sublist(L,left, median, item) 
    else:
        return bs_sublist(L, median, right, item)

        
def opt_insertion_sort(L):

    n = len(L)
    for i in range(n - 2, -1, -1):
        item = L[i] 
        pos = bs_sublist(L, i + 1, n - 1, L[i])
    
        for i in range(i, pos): 
            L[i]= L[i + 1] 

        L[pos] = item

    return L 


print(opt_insertion_sort([3, 2, 1]))
    

def insertion_sort(L):
    """Naive insertion sort. Adaptive, but still slow."""
    n = len(L)
    for j in range(n): # go through every item
        for i in range(n - 1 - j, n - 1): # bubble it into a sorted sublist
            if L[i] > L[i+1]:                 # 1 comparison
                L[i], L[i+1] = L[i+1], L[i]   # 2 writes 
            else: break
    
    return L

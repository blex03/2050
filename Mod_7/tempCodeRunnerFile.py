##### TODO 2 #####
# you'll need a helper function or default parameters here
def max_profit(L, left = 0, right = -1): # O(nlogn)
    if right == -1:
        right = len(L)
    if left == right:
        return 0
    # BASE CASE
    #    Only 1 item? Max profit is easy - it's the profit if we bought the day before and sold today
    if left+1 == right:
        return L[0]

    # DIVIDE into three problems and CONQUER:
    mid = (left + right) // 2

    #    find the max profit if we buy and sell in the left (recursive call)
    p1 = max_profit(L, left, mid)
    #    find the max profit if we buy and sell in the right (recursive call)
    p2 = max_profit(L, mid + 1, right)
    #    find the max profit if we buy in the left and sell in the right (requires a separate function)
    p3 = max_profit_crossing(L, left, right, mid)

    # COMBINE subproblems into the solution for this level of recursion
    #    Which of the above three scenarios gives the best profit?
    return max(p1, p2, p3)

##### TODO 3 #####
def max_profit_crossing(L, left, right, mid):
    # O(n): Max profit if we sell on the mid?
    p1 = 0
    total = 0

    for i in range(mid, left - 1, -1):

        total += L[i]

        if total > p1: 
            p1 = total


   # O(n): Max profit if we buy on the mid?
    p2 = 0
    total = 0

    for i in range(mid + 1, right):

        total += L[i]
        if total > p2: 
            p2 = total

    p3 = p1 + p2
    final = max(p1, p2, p3)
    return final
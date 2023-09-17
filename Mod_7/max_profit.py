##### TODO 1 #####
def price_to_profit(L):

    profits = []
    
    for i in range(len(L)):
        if i == 0:
            profits.append(0)
        else:
            profits.append(L[i] - L[i - 1])

    return profits

# brute force solution
def max_profit_brute(L):
    """Finds maximum profit. Assumes L is a list of profits (i.e. change in price every day), not raw prices"""
    n = len(L)
    max_sum = 0 # assume we can at least break even - buy and sell on the same day

    # outer loop finds the max profit for each buy day
    for i in range(n):
       # total profit if we bought on day i and sold on day j
        total = L[i]
        if total > max_sum: max_sum = total
        
        for j in range(i+1, n): 
            total += L[j] # total profit if we sell on day j
                          # we assume L[j] is the profit if we bought on day j-1 and sold on day j
                          # i.e., L is the change in value each day, relative to the day before
            if total > max_sum: max_sum = total

    return max_sum

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

print(max_profit([0, 9, 2, 114]))
print(max_profit_brute([0, 114, 2, -150]))
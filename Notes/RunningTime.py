class RunningTime:
    def __init__(self, n):
        self._L = n

    #returns the maximum value from the list _L.
    def linear(self):
        #set the variable max_value to -1 (all the elements should be larger than -1)
        max_value = -1
        for x in self._L:
            if x > max_value:
                max_value = x
        return max_value

    #counts the occurrence of all items in the list _L and returns dictionary with the number of 
    # occurrences for each item
    def quadratic(self):
        dict_counter = {}
        for x in self._L:
            #if the element is not in the dictionary yet, then count number of occourance
            if x not in dict_counter:
                dict_counter[x] = 0
                for y in self._L:
                    if x == y:
                        dict_counter[x]= dict_counter[x]+1
        return dict_counter
    
    #return a list that contains all the sublists of a list (powerlist). 
    def exponential(self):  
        lists = [[]] # list of lists
        for i in range(len(self._L) + 1):
            for j in range(i):
                lists.append(self._L[j: i])
        return lists

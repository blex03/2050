def constant(list):  #returns first element of a list
                      #-------------------              
    return list[0]   # 1 = O(1)
    
def linear(list):    #counts elements in a list
    total = 0        #  1

    for i in list:   #  n
        total += 1   #  2

    return total     #  1
                     #-------------------
                     #  1 + 2n + 1 = O(n)

def quadratic(list): #returns list of pairs

    pairs = []                    #  1

    for i in list:                #  n
        pair = []                 #  1
        for j in list:            #  n
            pair.append(i)        #  1
            pair.append(j)        #  1
        
        pairs.append(pair)        #  1

    return pairs                  #  1
                                  #--------------------------------
                                  # 1 + n + 2n^2 + 1 = O(n^2)


def _add(x,y):
    c = x+y
    return c

def sub(x,y):
    c = x-y
    return c

def multi(x,y):
    c = x*y
    return c

def div(x,y):
    c = x/y
    return c


# Python files can act as either reusable modules, or as standalone programs (scripts). 
# if __name__ == “main”: is used to execute some code only if the file was run directly, and not imported.
if __name__ == "__main__":
    x = 5
    y = 8
    res  = _add(x,y)
    #print("Results: ", res)
    #print(sub(x,y))
    assert (_add(6,6) == 12)
    assert(sub(10,5) == 5)
    print(res)
def word_compare(x, y = "steal"):
    
    char_dicx = {} # A dictionary for each word
    char_dicy = {} # The keys will be characters and the values will be the number of times they occur
                   # If the dictionaries are equal, the words are anagrams
                   
    if isinstance(x, str) and isinstance(y, str):    
        for i in x:
            if i not in char_dicx:
                char_dicx[i] = 1
            else:
                char_dicx[i] += 1
        for i in y:
            if i not in char_dicy:
                char_dicy[i] = 1
            else:
                char_dicy[i] += 1     
        if char_dicx == char_dicy:
            return "Anagram"     
        else:
            return x, y
    else:
        return "Those aren't strings!"





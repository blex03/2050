# STOP! You should write tests in TestHw2.py before modifying this file.
import random


class Card:
    def __init__(self, number, color, shading, shape): 

        self.number = number
        self.color = color
        self.shading = shading
        self.shape = shape

    def __str__(self): 

        return f'Card({self.number}, {self.color}, {self.shading}, {self.shape})'

    # repr() is called instead of str() by some of pytho's built-ins. We'll always
    # want the same value returned in this course, so we can piggyback off of str
    def __repr__(self): return str(self)

    def __eq__(self, other):
        if (self.number == other.number) and (self.color == other.color) and (self.shading == other.shading) and (self.shape == other.shape):
            return True


# Valid values for default game of GROUP! included here to avoid spelling
# issues. Feel free to copy/paste:
# [1, 2, 3]
# ['diamond', 'squiggle', 'oval']
# ['green', 'blue', 'purple']
# ['empty', 'striped', 'solid']
class Deck:
    def __init__(self, numbers = [1, 2, 3], colors = ['green', 'blue', 'purple'], shadings = ['empty', 'striped', 'solid'], shapes = ['diamond', 'squiggle', 'oval']): 
        self.my_nums = numbers
        self.my_cols = colors
        self.my_shadings = shadings
        self.my_shapes = shapes 

        self.cards = []

        for i in self.my_nums:
            for j in self.my_cols:
                for k in self.my_shadings:
                    for l in self.my_shapes:
                        self.cards.append(Card(i, j, k, l))
               
    # should remove and return top card
    def draw_top(self): 

        if len(self.cards) == 0:
            raise RuntimeError
        else: 
            top = self.cards[-1]
            self.cards = self.cards[:-1]
            return top

    # should randomly shuffle cards. Does not need a return.
    def shuffle(self): 
        random.shuffle(self.cards)

    # should return number of items in deck
    def __len__(self): 

        return len(self.cards)



# Oonce Card and Deck are both finished, write tests for this algorithm, then
# write the algorithm

# True if, for all attributes, each card has the same or different values;
# e.g. {1, 1, 1} or {1, 2, 3}, but not {1, 1, 3}
def is_group(c1, c2, c3): 
    if ((c1.number == c2.number) and (c2.number == c3.number)) or ((c1.color == c2.color) and (c2.color == c3.color)) or ((c1.shading == c2.shading) and (c2.shading == c3.shading)) or ((c1.shape == c2.shape) and (c2.shape == c3.shape)):
        return True
    elif  ((c1.number != c2.number) and (c2.number != c3.number) and (c1.number != c3.number)) and ((c1.color != c2.color) and (c2.color != c3.color) and (c1.color != c3.color)) and ((c1.shading != c2.shading) and (c2.shading != c3.shading) and (c1.shading != c3.shading)) and ((c1.shape != c2.shape) and (c2.shape != c3.shape) and (c1.shape != c3.shape)):
        return True
    else: 
        return False
       
        
    



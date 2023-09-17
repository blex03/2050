class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other): 
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5 < ((other.x ** 2) + (other.y ** 2)) ** 0.5

    def __gt__(self, other): 
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5 > ((other.x ** 2) + (other.y ** 2)) ** 0.5

    def __eq__(self, other): 
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5 == ((other.x ** 2) + (other.y ** 2)) ** 0.5

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def dist_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(6, 9)
    p3 = Point(6, 9)

    s = str(p1)

    d = Point.dist_from_origin(p1)

    assert p1.x == 3                 #init
    assert p1.y == 4

    assert p1 < p2                   #Comparators
    assert not p2 < p1
    assert p2 > p1
    assert not p1 > p2
    assert p2 == p3
    assert not p2 == p1

    assert s == "Point(3, 4)"        #str

    assert d == 5                    #dist_from_origin

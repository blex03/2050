from BSTMap import BSTMap, BSTNode # provided for you

# Inherit from BSTMap, but overload `newnode` to use this one instead
class MyBSTMap(BSTMap):
    
    def newnode(self, key, value = None): 
        return MyBSTNode(key, value)    # overloads the `newnode` method to use MyBSTNode() instead of BSTNode()

    # TODO: implement the three methods below
    def __eq__(self, other):
        """ADD DOCSTRING"""
             # The heavy lifting here is done in the corresponding
             # function in MyBSTNode - just tell it which node to
             # start with.

        return MyBSTNode.__eq__(self.root, other.root)

    # these are "static" methods - they belong to the class but do not take an instance of 
    # the class as a parameter (no `self``).
    # note the "decorator" @staticmethod - this let's python know this is not a typical "bound" method
    @staticmethod
    def frompreorder(L):
        """Generates BST from preordered list of kv"""
        tree = MyBSTMap()
        for i in L:
            tree.put(i[0], i[1])
        return tree

    @staticmethod
    def frompostorder(L):
        """ADD DOCSTRING"""
        tree = MyBSTMap()
        for i in L[::-1]:
            tree.put(i[0], i[1])
        return tree


class MyBSTNode(BSTNode):
    
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class

    # TODO: implement the method below
    def __eq__(self, other):
        """returns True if two trees have the same shape and same key/value pairs"""
    
        if self is None and other is None:
            return True
        elif self is None or other is None:
            return False
        else:
            return (self.key == other.key) and (self.value == other.value) and (self.left == other.left) and (self.right == other.right)



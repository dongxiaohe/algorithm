class TreeNode():
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

two = TreeNode("2", None, None)
zero = TreeNode("0", None, None)
one = TreeNode("1", zero, two)
three = TreeNode("3", one, None)

"""
           
                                                                  root
                                                    
                                      left                                                    right
                                                                      
                   left-left                      left-right                       right-left       right-right
     left-left-left        right-right-right                left-right-right                                     right-right-right
"""

import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data, parent=None, left=None, right=None, balance=0):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.balance = balance

class BST:
    def __init__(self):
        self.root = None

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        
        x.balance = x.balance + 1 - min(y.balance, 0)
        y.balance = y.balance + 1 + max(x.balance, 0)

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        
        x.balance = x.balance - 1 - max(y.balance, 0)
        y.balance = y.balance - 1 + min(x.balance, 0)

    def _lr_rotate(self, x):
        self._left_rotate(x.left)
        self._right_rotate(x)

    def _rl_rotate(self, x):
        self._right_rotate(x.right)
        self._left_rotate(x)

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            print("Case #1: Pivot not detected")
            return

        current = self.root
        pivot = None
        last_direction = None

        while current:
            if data < current.data:
                if current.balance != 0:
                    pivot = current
                    last_direction = 'left'
                current.balance -= 1
                if not current.left:
                    current.left = Node(data, parent=current)
                    break
                current = current.left
            else:
                if current.balance != 0:
                    pivot = current
                    last_direction = 'right'
                current.balance += 1
                if not current.right:
                    current.right = Node(data, parent=current)
                    break
                current = current.right

        if pivot:
            if last_direction == 'left' and pivot.balance < 0:
                child = pivot.left
                if child.balance > 0:
                    print("Case #3b: LR rotation needed")
                    self._lr_rotate(pivot)
                else:
                    print("Case 3b not fully addressed or another case")
            elif last_direction == 'right' and pivot.balance > 0:
                child = pivot.right
                if child.balance < 0:
                    print("Case #3b: RL rotation needed")
                    self._rl_rotate(pivot)
                else:
                    print("Case 3b not fully addressed or another case")

    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False


tree = BST()
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(10)  
tree.insert(25)  
tree.insert(35)  
tree.insert(15) 
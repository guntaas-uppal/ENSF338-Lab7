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
        
        
        if pivot is None:
            print("Case #1: Pivot not detected")
        elif pivot and last_direction == 'left' and pivot.balance < 0 or last_direction == 'right' and pivot.balance > 0:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
        else:
            print("Case 3 not supported")

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

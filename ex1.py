import random
import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return
        
        current = self.root
        while True:
            parent = current
            if data < current.data:
                if not current.left:
                    current.left = Node(data, parent=current)
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = Node(data, parent=current)
                    break
                current = current.right

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

    def max_balance(self):
        max_balance = 0
        stack = [(self.root, 0)]
        while stack:
            node, depth = stack.pop()
            if node:
                current_balance = depth - min(self._depth(node.left), depth)
                max_balance = max(max_balance, current_balance)
                stack.append((node.right, depth + 1))
                stack.append((node.left, depth + 1))
        return max_balance

    def _depth(self, node):
        if not node:
            return 0
        depth = 0
        while node:
            depth += 1
            node = node.right
        return depth

tree = BST()
for i in range(1000):
    tree.insert(i)

times = []
balances = []
for _ in range(1000):
    task = list(range(1000))
    random.shuffle(task)
    start_time = timeit.default_timer()
    for item in task:
        tree.search(item)
    end_time = timeit.default_timer()
    times.append(end_time - start_time)
    balances.append(tree.max_balance())

plt.scatter(balances, times)
plt.title('Scatter plot of Absolute Balance vs Search Time')
plt.xlabel('Absolute Balance')
plt.ylabel('Search Time (seconds)')
plt.show()

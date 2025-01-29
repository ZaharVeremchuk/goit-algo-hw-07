# Двійкове дерево
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

# Визначення мінімального значення в дереві
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

# Визначення максимального значення в дереві
def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current

# Загальна сума значень вершин
def sum_of_nodes(root):
    if root is None:
        return 0
    return root.val + sum_of_nodes(root.left) + sum_of_nodes(root.right)
        

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 10)
root = insert(root, 7)
root = insert(root, 55)
root = insert(root, 8)

print(f"Завдання 1. Максимальне значення = {max_value_node(root).val}")
print(f"Завдання 2. Мінімальне значення = {min_value_node(root).val}")
print(f"Завдання 3. Загальна сума вершин = {sum_of_nodes(root)}")

# root = delete(root, 7)
# print(root)


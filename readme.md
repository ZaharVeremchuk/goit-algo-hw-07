**Завдання 1 (код):**
```
# Визначення максимального значення в дереві
def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current
```

**Завдання 2 (код):**
```
# Визначення мінімального значення в дереві
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current
```

**Завдання 3 (код):**
```
# Загальна сума значень вершин
def sum_of_nodes(root):
    if root is None:
        return 0
    return root.val + sum_of_nodes(root.left) + sum_of_nodes(root.right)
```
**Дерево:**
```
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
```

**Результати:**<br>
Завдання 1. Максимальне значення = 55<br>
Завдання 2. Мінімальне значення = 2<br>
Завдання 3. Загальна сума вершин = 90<br>
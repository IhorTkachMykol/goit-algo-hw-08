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

def find_min(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current

# Побудова дерева
root = Node(5)
for val in [3, 2, 4, 7, 6, 8]:
    root = insert(root, val)

# Пошук мінімуму
result = find_min(root)
if result:
    print(f"Найменше значення у дереві: {result.val}")  # → 2
else:
    print("Дерево порожнє")
    
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# горизонтальне дерево 
def print_tree(root, prefix="", is_left=True):
    if root is None:
        return
    connector = "├── " if is_left else "└── "
    print(prefix + connector + str(root.val))
    child_prefix = prefix + ("│   " if is_left else "    ")
    if root.left or root.right:
        print_tree(root.left,  child_prefix, is_left=True)
        print_tree(root.right, child_prefix, is_left=False)

# класична деревовидна форма 
def print_tree_levels(root):
    if root is None:
        return
    queue = [(root, 0)]
    current_level = 0
    line = []
    while queue:
        node, level = queue.pop(0)
        if level != current_level:
            print(" ".join(line))
            line = []
            current_level = level
        line.append(str(node.val))
        if node.left:  queue.append((node.left,  level + 1))
        if node.right: queue.append((node.right, level + 1))
    if line:
        print(" ".join(line))

root = Node(5)
for v in [3, 2, 4, 7, 6, 8]:
    root = insert(root, v)

print("=== Горизонтальне дерево ===")
print(str(root.val))
print_tree(root.left,  "", is_left=True)
print_tree(root.right, "", is_left=False)

print("\n=== По рівнях ===")
print_tree_levels(root)

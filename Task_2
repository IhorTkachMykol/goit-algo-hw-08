class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def get_height(node):
    return 0 if not node else node.height

def get_balance(node):
    return 0 if not node else get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y, T2 = z.right, z.right.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def right_rotate(y):
    x, T3 = y.left, y.left.right
    x.right = y
    y.left = T3
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def insert(root, key):
    if not root:
        return AVLNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)
    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)
    return root

# сума всіх вузлів ---
def sum_all(root):
    if root is None:
        return 0
    return root.key + sum_all(root.left) + sum_all(root.right)

# --- Тест ---
root = None
for val in [10, 20, 30, 40, 50, 25]:
    root = insert(root, val)

result = sum_all(root)
print(f"Сума всіх значень у дереві: {result}") 

class AVLNode:
    def __init__(self, val):
        self.val   = val
        self.left  = self.right = None
        self.height = 1

class AVL:
    def _h(self, n):  return n.height if n else 0
    def _bf(self, n): return self._h(n.left) - self._h(n.right)

    def _update(self, n):
        n.height = 1 + max(self._h(n.left), self._h(n.right))

    def _rotate_right(self, y):
        x = y.left; y.left = x.right; x.right = y
        self._update(y); self._update(x)
        return x

    def _rotate_left(self, x):
        y = x.right; x.right = y.left; y.left = x
        self._update(x); self._update(y)
        return y

    def _balance(self, n):
        self._update(n)
        bf = self._bf(n)
        if bf > 1:
            if self._bf(n.left) < 0:
                n.left = self._rotate_left(n.left)
            return self._rotate_right(n)
        if bf < -1:
            if self._bf(n.right) > 0:
                n.right = self._rotate_right(n.right)
            return self._rotate_left(n)
        return n

    def insert(self, root, val):
        if not root: return AVLNode(val)
        if val < root.val:   root.left  = self.insert(root.left,  val)
        elif val > root.val: root.right = self.insert(root.right, val)
        return self._balance(root)

    def inorder(self, root):
        return (self.inorder(root.left) + [root.val] +
                self.inorder(root.right)) if root else []

if __name__ == "__main__":
    avl  = AVL()
    root = None
    for v in [10, 20, 30, 40, 50, 25]:
        root = avl.insert(root, v)

    print("Inorder:", avl.inorder(root))  # [10,20,25,30,40,50]
    print("Balandlik:", root.height)       # 3 (muvozanat!)

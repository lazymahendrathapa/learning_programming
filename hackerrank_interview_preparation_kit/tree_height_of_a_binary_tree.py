class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def set_level(root, level):
    root.level = level
    # print(root.info, root.level)
    if root.left:
        # print("Left", root.left.info)
        set_level(root.left, level + 1)

    if root.right:
        # print("Right", root.right.info)
        set_level(root.right, level + 1)


def height(root):
    set_level(root, 0)

    val = [root]
    # print(val)
    level = 0
    while len(val) > 0:

        # print("here")
        v = val.pop(0)
        if level < v.level:
            level = v.level

        if v.left:
            val.append(v.left)
        if v.right:
            val.append(v.right)

    return level


if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())
    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    print(height(tree.root))


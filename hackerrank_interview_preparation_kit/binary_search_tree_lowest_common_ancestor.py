class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None


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


def lca(root, a, b):

    temp = root

    while True:
        if temp.info > a and temp.info > b:
            temp = temp.left
        elif temp.info < a and temp.info < b:
            temp = temp.right
        else:
            return temp


if __name__ == '__main__':
    tree = BinarySearchTree()

    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    v = list(map(int, input().split()))

    ans = lca(tree.root, v[0], v[1])

    print(ans.info)






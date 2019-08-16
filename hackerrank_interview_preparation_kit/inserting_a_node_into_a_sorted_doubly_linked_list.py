class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node):

    while node:
        print(node.data, end=' ')
        node = node.next


def sorted_insert(head, data):

    new_node = DoublyLinkedListNode(data)

    if not head:
        return new_node

    if head.data > data:
        new_node.next = head
        head.prev = new_node
        return new_node

    if not head.next:
        if head.data < data:
            head.next = new_node
            new_node.prev = head
            return head
        else:
            new_node.next = head
            head.prev = new_node
            return new_node

    current_node = head

    return_node = None
    while True:
        if current_node.data > data:
            break
        else:

            if current_node.next:
                return_node = current_node
                current_node = current_node.next
            else:
                #print("Here")
                new_node.prev = current_node
                current_node.next = new_node

                return_node = None

                break

    if return_node:
        new_node.next = return_node.next
        new_node.prev = return_node
        return_node.next = new_node

    return head


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sorted_insert(llist.head, data)

        print_doubly_linked_list(llist1)

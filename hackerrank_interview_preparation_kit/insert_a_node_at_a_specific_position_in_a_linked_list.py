class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node):
    while node:
        print(node.data, end=" ")

        node = node.next


def insert_node_at_position(head, data, position):

    new_node = SinglyLinkedListNode(data)

    if not head:
        return new_node
    elif position == 0:
        new_node.next = head
        return new_node

    current_node = head

    for i in range(position-1):
        current_node = current_node.next

    new_node.next = current_node.next
    current_node.next = new_node

    return head


if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())
    position = int(input())

    llist_head = insert_node_at_position(llist.head, data, position)

    print_singly_linked_list(llist_head)


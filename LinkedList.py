class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, letter):
        new_node = Node(letter)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self):
        if self.head is not None:
            self.head = self.head.next

    def display(self):
        current = self.head

        if current is None:
            print("EMPTY")
            return

        while current:
            print(current.data, end="")
            if current.next:
                print(" -> ", end="")
            current = current.next
        print()


if __name__ == "__main__":
    linked = LinkedList()
    print("LINKED LIST")

    for letter in "RAMOS":
        linked.add(letter)

    linked.display()

    while linked.head:
        linked.remove()
        linked.display()

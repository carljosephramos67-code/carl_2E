class Stack:
    def __init__(self):
        self.data = []

    def push(self, letter):
        self.data.append(letter)

    def pop(self):
        if self.data:
            self.data.pop()

    def display(self):
        print(self.data)


if __name__ == "__main__":
    stack = Stack()
    print("STACK (LIFO)")

    for letter in "RAMOS":
        stack.push(letter)

    stack.display()

    while stack.data:
        stack.pop()
        stack.display()

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, letter):
        self.data.append(letter)

    def dequeue(self):
        if self.data:
            self.data.pop(0)

    def display(self):
        print(self.data)


if __name__ == "__main__":
    queue = Queue()
    print("QUEUE (FIFO)")

    for letter in "RAMOS":
        queue.enqueue(letter)

    queue.display()

    while queue.data:
        queue.dequeue()
        queue.display()

class Array:
    def __init__(self):
        self.data = []

    def add(self, letter):
        self.data.append(letter)

    def remove(self):
        if self.data:
            self.data.pop(0)

    def display(self):
        print(self.data)


if __name__ == "__main__":
    array = Array()
    print("ARRAY")

    for letter in "RAMOS":
        array.add(letter)

    array.display()

    while array.data:
        array.remove()
        array.display()

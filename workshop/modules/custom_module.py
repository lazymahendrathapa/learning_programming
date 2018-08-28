number_one = 1
age_of_queen = 78

def print_hello():
    print("Hello People")

def times_four(input):
    return input * 4

class Piano:
    def __init__(self):
        self.type = ""
        self.height = 0
        self.price = 0

    def enter_input(self):
        self.type = input("Which type of piano? ")
        self.height = input("Which height? ")
        self.price = input("Which price? ")

    def print_details(self):
        print(f'{self.type} has height {self.height} and price {self.price}')
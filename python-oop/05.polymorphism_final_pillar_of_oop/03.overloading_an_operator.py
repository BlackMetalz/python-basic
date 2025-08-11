class Square:
    def __init__(self, side):
        self.side = side

    def __add__(square_one, square_two):
        return (square_one.side + square_two.side) * 4


square_one = Square(5) # 5 * 4 = 20
square_two = Square(10) # 10 * 4 = 40

print("Sum of sides of square one and two: ", square_one + square_two)

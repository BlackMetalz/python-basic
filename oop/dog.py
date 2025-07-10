# Definition of the Dog class
class Dog:
    # Initializer method to set the name and age of the dog
    # We need to define parameters for the dog's name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old."


def main():
    # This function is used to demonstrate the functionality of the Dog class
    my_dog = Dog("Buddy", 5)
    print(my_dog.bark())  # Output: Woof!
    print(my_dog.get_info())  # Output: Buddy is 5 years old.
    another_dog = Dog("Max", 3)
    print(another_dog.bark())  # Output: Woof!
    print(another_dog.get_info())  # Output: Max is 3 years old

# Example usage
if __name__ == "__main__":
    main()

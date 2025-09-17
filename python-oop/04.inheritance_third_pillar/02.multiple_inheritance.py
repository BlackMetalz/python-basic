class OperatingSystem:
    multi_tasking = True
    name = "Mac OS" # This will print first because of class order in multiple inheritance

class Apple:
    website = "www.apple.com"
    name = "Apple Inc."

class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multi_tasking is True:
            print("This is a multi-tasking system. Visit {} for more details.".format(self.website))
            print("Name: %s" % self.name)

macBook = MacBook()
# print(macBook())
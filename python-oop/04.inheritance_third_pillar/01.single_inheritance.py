class Apple:
    manufacturer = "Apple Inc."
    contact_website = "www.apple.com/contact"

    def contact_details(self):
        print("To contact Apple Inc., please visit:", self.contact_website)


class MacBook(Apple):
    def __init__(self):
        self.year_of_manufacture = 2025

    def manufacture_details(self):
        print(f"This MacBook was manufactured in {self.year_of_manufacture} by {self.manufacturer}.")
    

new_macBook = MacBook()

new_macBook.manufacture_details()
new_macBook.contact_details()
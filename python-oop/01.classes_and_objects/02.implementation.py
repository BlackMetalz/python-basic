class Employee:
    name = "kienlt" # Atribute of the class
    age  = 33
    skills = ["python", "django", "flask"]

    def is_old_already(self): # Method of the class
        if (self.age > 30):
            return "Old already!"
        return "Still young!"

    def has_enough_skills(self):
        if (len(self.skills) > 3):
            return "Has enough skills!"
        return "Not enough skills!"

    # Static method. This is a method that belongs to the class, not to any instance.
    @staticmethod # With this decorator, we can call this method without creating an instance of the class.
    def yoo_wtf():
        return "WTF is this? Yoo!"
    
# Usage:
emp1 = Employee()
print(emp1.name)
print(emp1.age)
print(emp1.skills)
print(emp1.is_old_already()) 
print(emp1.has_enough_skills()) 
print(Employee.yoo_wtf())  # Call static method without instance
class Employee:
    def set_number_of_working_hours(self):
        self.set_number_of_working_hours = 40 # 40 hours per week

    def display_working_hours(self):
        print("Working hours: ", self.set_number_of_working_hours)

class Trainee(Employee):
    # Overriding
    def set_number_of_working_hours(self):
        self.set_number_of_working_hours = 20 # 20 hours per week for a trainee

    def reset_number_of_working_hours(self):
        super().set_number_of_working_hours() # Call the method from Employee class


employee = Employee()
employee.set_number_of_working_hours()
print("Employee:")
employee.display_working_hours()

trainee = Trainee()
trainee.set_number_of_working_hours() # inherits the method from Employee, but overrides it with its own implementation
print("Trainee:")
trainee.display_working_hours() # inherits the method from Employee without overriding it xD

trainee.reset_number_of_working_hours() # Call the method from Employee class
print("Trainee after reset:")
trainee.display_working_hours() # inherits the method from Employee without overriding it xD
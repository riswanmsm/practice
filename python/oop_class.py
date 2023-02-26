class Employee:
    # class variable
    company_name = 'youtube'

    # constructor
    def __init__(self, first_name, last_name):
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self._domain_ending = '.com'

    # instance method
    def get_email(self):
        return self.first_name + '.' + self.last_name + '@' + Employee.company_name + self._domain_ending

    # class method
    @classmethod
    def change_company(cls, company_name):
        cls.company_name = company_name


# creating new object of Employee class
emp1 = Employee('riswan', 'saheed')
# calling instance method
print(emp1.get_email())  # it will print riswan.saheed@youtube.com

# calling class method
Employee.change_company('runedigital')

# creating new object of Employee class
emp1 = Employee('riswan', 'saheed')
# calling instance method
print(emp1.get_email())  # it will print riswan.saheed@runedigital.com

print(Employee.company_name)
print(emp1.company_name)


# car_count = 0
# def calculate_car_count():
#     pass

# class Car:
#     manufacturer = "temp"
#     def __init__(self, chassi_number):
#         self.chassi_number = chassi_number
#         self.model = "temp"

#     def run(self):
#         pass


# car1 = Car("11-A5")
# car1.manufacturer = "toyota"

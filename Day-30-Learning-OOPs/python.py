class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@company.com"

    def get_fullname(self):
        return f"{self.first} {self.last}"


# Testing employee instances
emp_1 = Employee("Rizwan", "Akbar", 50000)
emp_2 = Employee("Usman", "Ali", 60000)

print(f"Employee 1: {emp_1.get_fullname()} | Email: {emp_1.email}")
print(f"Employee 2: {emp_2.get_fullname()} | Email: {emp_2.email}")
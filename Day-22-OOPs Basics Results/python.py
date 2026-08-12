

class Person:
    """Parent Class"""
    def __init__(self, name):
        self.name = name


class Student(Person):
    """Child Class inheriting from Person"""
    def __init__(self, name, marks):
        super().__init__(name)
        self.__marks = marks  # Encapsulated (Private) attribute

    def get_marks(self):
        return self.__marks

    def display_status(self):
        status = "Passed" if self.__marks >= 50 else "Failed"
        print(f"Student: {self.name} | Marks: {self.__marks} | Status: {status}")


# Main Execution
if __name__ == "__main__":
    students = [
        Student("Ali", 85),
        Student("Sara", 92),
        Student("Usman", 40)
    ]

    print("--- STUDENT RESULTS ---")
    for student in students:
        student.display_status()
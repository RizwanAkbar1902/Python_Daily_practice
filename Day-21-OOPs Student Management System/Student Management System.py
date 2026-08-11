"""
Project: Student Management System
Day: 21
Author: Rizwan Akbar

Description:
A console-based Student Management System built to practice
Object-Oriented Programming (OOP).

The program allows a school manager to register students,
enroll students in courses, and display student information.

Concepts Practiced:
- Classes and Objects
- Constructors (__init__)
- Encapsulation
- Private Attributes
- Methods
- Type Hints
- Dictionaries
- Lists
- Conditional Statements
- Object Composition
"""


class Student:
    """Represent a student and manage their enrolled courses."""

    def __init__(self, student_id: int, name: str, age: int, grade: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.__courses = []

    def enroll_course(self, course_name: str):
        """Enroll the student in a course if not already enrolled."""

        course_name = course_name.strip()

        if not course_name:
            print("[!] Course name cannot be empty.")
            return

        if course_name not in self.__courses:
            self.__courses.append(course_name)
            print(f"[+] {self.name} enrolled in {course_name}.")
        else:
            print(f"[!] {self.name} is already enrolled in {course_name}.")

    def get_details(self):
        """Display the student's information and enrolled courses."""

        courses = ", ".join(self.__courses)

        if not courses:
            courses = "No courses enrolled"

        print(
            f"\nID: {self.student_id}"
            f" | Name: {self.name}"
            f" | Age: {self.age}"
            f" | Grade: {self.grade}"
        )
        print(f"Enrolled Courses: {courses}")


class SchoolManager:
    """Manage students registered at a school."""

    def __init__(self, school_name: str):
        self.school_name = school_name
        self.students = {}

    def add_student(self, student: Student):
        """Add a student if their ID is not already registered."""

        if student.student_id in self.students:
            print(
                f"[!] Student ID {student.student_id} "
                "is already registered."
            )
            return

        self.students[student.student_id] = student
        print(
            f"[+] Added student: {student.name} "
            f"to {self.school_name}."
        )

    def display_all_students(self):
        """Display a report containing all registered students."""

        print("\n" + "=" * 50)
        print(f"      {self.school_name.upper()} - STUDENT REPORT")
        print("=" * 50)

        if not self.students:
            print("No students registered yet.")
            return

        for student in self.students.values():
            student.get_details()


def main():
    """Create sample students and demonstrate the system."""

    school = SchoolManager("Tech Academy")

    # Create student objects
    student_1 = Student(101, "Ali Khan", 20, "A")
    student_2 = Student(102, "Sara Ahmed", 21, "A+")

    # Register students
    school.add_student(student_1)
    school.add_student(student_2)

    # Enroll students in courses
    student_1.enroll_course("Python Programming")
    student_1.enroll_course("Data Structures")

    student_2.enroll_course("Web Development")

    # Display student report
    school.display_all_students()


if __name__ == "__main__":
    main()
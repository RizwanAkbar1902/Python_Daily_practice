print("==== Student Management System ====")
choice = 0
students = {}
while choice !=4 :
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")
    print()
    choice = int(input("Enter a choise: "))

    if choice == 1:
        print()
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))

        if marks <0 or marks > 100:
            print("Input valid marks ")
        elif marks >90 :
            grade = "A"
        elif marks >80:
            grade = "B"
        elif marks >70:
            grade = "C"
        elif marks >60:
            grade ="D"
        else :
            grade = "F"
        students[name] = {"marks" : marks , "grade" : grade}
        print()
        print()
        print("Student added Successfully!")
        print("============================================")
        print()
        

    elif choice == 2:
        print()
        if len(students) == 0 :
            print("NO record yet.")
        else:
            for name in students:
                print(name,"---", students[name]["marks"],"---", students[name]["grade"])
                print()
        print("============================================")
        print()
    elif choice == 3:
        search = input("Enter name you want to search: ")
        if search in  students:
            print()
            print("Record founded !")
            print("Name : ",search)
            print("Marks : ", students[name]["marks"])
            print(students[name]["grade"])
            print("============================================")
            print()
    elif choice == 4:
        print("Good Bye!")
        print("============================================")
        print()
    else:
        print("Please input value between 1-4 : ")
        print("============================================")
        print()
    
        
        

    

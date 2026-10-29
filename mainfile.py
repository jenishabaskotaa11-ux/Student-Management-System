import json
students = {
    "student1": {"name": "Jenisha", "age": 21, "marks": 85},
    "student2": {"name": "Aarav", "age": 20, "marks": 72},
    "student3": {"name": "Maya", "age": 22, "marks": 91}
}
try:
    with open("std_system.json","r")as file:
        students=json.load(file)
except FileNotFoundError:
    with open("std_system.json","w")as file:
        json.dump(students,file,indent=4)

while True:
    print("Student Management System\n1. Search Student Details\n2. Update Student's marks\n3. Delete Student\n4.View all Students\n5. Add Student\n6. Exit")
    option=input("enter your choice:")

    if option=='1':
        student_name=input("enter student's name:")
        for student in students:
            if student_name.strip().title()==students[student]["name"]:
                # print(students[student])
                with open("std_system.json","r")as file:
                    saved_std=json.load(file)
                    print(saved_std[student])
                break
        else:
            print("student not found!!")

    elif option=='2':
        student_name=input("enter student's name:")
        for student in students:
            if student_name.strip().title()==students[student]["name"]:
                students[student]["marks"]=(input("enter updated marks:"))
                updated_mark=students[student]["marks"]
                while True:
                    if updated_mark.isdigit() is False:
                        print("only numbers accepted")
                    elif (0<=int(updated_mark)<=100) is False:
                        print("marks must be between 0 and 100.")
                    else:
                        break
                    updated_mark=input("enter valid mark:")
                students[student]["marks"]=int(updated_mark)
                # print(students)
                with open("std_system.json","w")as file:
                    json.dump(students,file,indent=4)
                with open("std_system.json","r")as file:
                    saved_std=json.load(file)
                    print(saved_std)     
                print("marks updated!!")
                break
        else:
            print("student not found!!")

    elif option=='3':
        student_name=input("enter student's name:")
        for student in students:
            if student_name.strip().title()==students[student]["name"]:
                del students[student]
                # print(students)
                with open("std_system.json","w")as file:
                    json.dump(students,file,indent=4)
                with open("std_system.json","r")as file:
                    saved_std=json.load(file)
                    print(saved_std)                
                print("student deleted!!")
                break
        else:
            print("student not found!!")      

    elif option=='4':
        # print(students)
        with open("std_system.json","r")as file:
            saved_std=json.load(file)
            print(saved_std)

    elif option=="5":
        name=input("enter student's name:")
        
        age=input("enter student's age:")
        while True:
            if age.isdigit() is False:
                print("age must be a number.")
                age=input("enter student's valid age:")
            elif (0<int(age)<60) is False:
                age=input("enter student's valid age:")
            else:
                break
        age=int(age)

        marks=input("enter student's marks:")
        while True:
            if marks.isdigit() is False:
                print("marks must be a number")
                marks=input("enter student's marks:")
            elif (0<=int(marks)<=100)is False:
                print("marks must be between 0 and 100.")
                marks=input("enter student's marks:")
            else:
                break
        marks=int(marks)

        n=1
        while "student"+str(n) in students:
            n=n+1
        
        students["student"+str(n)]={"name":name.strip().title(),"age":age,"marks":marks}
        with open ("std_system.json","w")as file:
            json.dump(students,file,indent=4)
        print("student added successfully!")
        with open("std_system.json","r")as file:
            saved_std=json.load(file)
            print(saved_std)     
                        
    elif option=='6':
        print("thank you for using us!!")
        break
    else:
        print("invalid choice")

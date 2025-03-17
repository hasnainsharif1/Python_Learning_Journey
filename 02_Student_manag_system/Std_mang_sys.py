import os

Student_data_list = []

def static_interface():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    static_interface()
    print("-------- Student Managment System -------- ")
    print("1.Add Student")
    print("2.Update Student")
    print("3.Delet Student")
    print("4.View All Student")
    print("5.Find Higest/Lowest Grades")
    print("6.Filter Student")
    print("7.Exit Or Stop\n\n")
    user_input = int(input("Enter Your Choice: "))

    if user_input == 1:
        static_interface()
        std_dict = {}
        roll_no = int(input("Enter Roll Number: "))
        name = str(input('Enter Student Name: '))
        age = int(input("Enter Age: "))
        grades = int(input("Enter Grades: "))

        std_dict['name'] = name
        std_dict['roll_no'] = roll_no
        std_dict['age'] = age
        std_dict['grades'] = grades
        Student_data_list.append(std_dict)
        print("Student Data Added Successfully!")
        print(Student_data_list)
    elif user_input == 2:
        std_id = int(input("Enter Student Id Or Name: "))
        found = False

        for student in Student_data_list:
            if student.get('roll_no') == std_id:
                name = str(input('Enter Student Name: '))
                age = int(input("Enter Age: "))
                grades = int(input("Enter Grades: "))

                student['name'] = name
                student['age'] = age
                student['grades'] = grades

                print("Student Data updated successully!")
                found = True
                break  
        if found == False:
            print("Student not Found!")
    elif user_input == 3:
        std_id = int(input("Enter Student Id Or Name: "))
        found = False

        for student in Student_data_list:
            if student.get('roll_no') == std_id:
                Student_data_list.remove(student)

                print("Student Deleted Successfully!")
                found = True
                break
        if found == False:
            print("Student Not Found!")
        

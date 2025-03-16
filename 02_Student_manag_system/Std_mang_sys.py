Student_data_list = []



while True:
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
        std_dict = {}
        name = input('Enter Student Name: ')
        roll_no = input("Enter Roll Number: ")
        age = input("Enter Age: ")
        grades = input("Enter Grades: ")

        std_dict['name', 'roll_no', 'age', 'grades'] = name, roll_no, age, grades
        Student_data_list.append(std_dict)
        print(Student_data_list)
        break









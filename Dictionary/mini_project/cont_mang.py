contact = []
amt = int(input("Enter how many contact you want to add: "))

for i in range(amt):
    numb = int(input(f"Enter {i+1} contact number: "))
    contact.append(numb)

print("All Contacts Added Sucessfully!")

while True:
    select_value = int(input("Enter 1 for Add\nEnter 2 for Update\nEnter 3 for Delete\nEnter 4 for View\nEnter 5 for Exit/Stop: "))

    if select_value == 1:
        new_contact = int(input("Enter new Contact: "))
        contact.append(new_contact)
    elif select_value == 2:
        prev_cont = int(input("Ener Contact you want to update: "))
        if prev_cont in contact:
            next_contact = int(input("Enter new Conact: "))
            index = contact.index(prev_cont)
            contact[index] = next_contact
        else:
            print("Contact not found!")
    elif select_value == 3:
        del_contact = int(input("Enter Contact you want to delete: "))
        if del_contact in contact:
            contact.remove(del_contact)
        else:
            print("Not Found!")
    elif select_value == 4:
        print(contact)
    elif select_value == 5:
        break
    else:
        print("Enter valid Number!")
#title
print("\t\t\t\t\t\t Phonebook Application")
print("\t\t\t\t\t\t 'Connect with people'")

#phonebook directory initialization
phoneBook= {99999 : {"Name" : "James McCartney", "Gender" : "Male", "Age" : 35, "Add" : "#21, 5th Avenue"}, 
            99998 : {"Name" : "Ian Campbell", "Gender" : "Male", "Age" : 30, "Add" : "#6, 5th Avenue"},
            99997 : {"Name" : "Kelly Johnson", "Gender" : "Female", "Age" : 25, "Add" : "#2, 4th Avenue"},
            99996 : {"Name" : "John Newman", "Gender" : "Male", "Age" : 42, "Add" : "#25, 5th Avenue"}}

#main program
def print_menu():
    print("Press 1 to access phonebook directory")
    print("Press 2 to enter a new contact")
    print("Press 3 to quit")

option = 0
print_menu()
while option != 3:
    option = int(input("What do you want to do? "))  #takes user input
    
    if option == 1:
        number = int(float(input("Enter the number: ")))  #takes number to display info
        if number in phoneBook:
            print("Name : ", phoneBook[number]["Name"])
            print("Age : ", phoneBook[number]["Age"])
            print("Gender : ", phoneBook[number]["Gender"])
            print("Address : ", phoneBook[number]["Add"])
        else:
            print("Please enter a valid number")

    elif option == 2:
        key = input("Number : ")
        name = input("Name : ")
        age = input("Age : ")
        gender = input("Gender : ")
        add = input("Address : ")

        phoneBook[key] = {"Name" : name, "Age" : age, "Gender" : gender, "Address" : add}
        
        print("******************")
        for number, p_info in phoneBook.items():
            print("Number : ", number)
            for key in p_info:
                print(key + ":", p_info[key])
            print()
            
    elif option != 3:
        print_menu()
        
        

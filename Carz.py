Carz=[]
while True:
    print('''
        1.Add customer
        2.view
        3.Search
        4.Update
        5.Delete
        6.Exit''')
    choice=int(input("enter the choice:"))
    if choice==1:
        name=input("enter the Owner name:")
        car_no=input("enter the vehicle number:")
        vh_model=input("Enter the vehicle model")
        mob_no = int(input("Enter Mobile Number: "))
        Address=input("enter the address:")
        Carz.append([name,car_no,vh_model,mob_no,Address,])
        print("Customer added successfully")
    elif choice == 2:
        if Carz:
            print('_' * 75)
            print('{:<10}{:<20}{:<20}{:<15}{:<15}'.format('NAME', 'VEHICLE NUMBER','VEHICLE MODEL', 'MOBILE NO', 'ADDRESS'))
            print('_' * 75)
            for i in Carz:
                print('{:<10}{:<20}{:<20}{:<15}{:<15}'.format(i[0], i[1], i[2], i[3], i[4]))
        else:
            print("DETAILS IS NOT FOUND") 
    elif choice == 3:
        car_no=input("Enter the vehicle number: ")
        for i in Carz:
            if i[1] == car_no:
                print('_' * 75)
                print('{:<10}{:<20}{:<20}{:<15}{:<15}'.format('NAME', 'VEHICLE NUMBER','VEHICLE MODEL', 'MOBILE NO', 'ADDRESS'))
                print('_' * 75)
                print('{:<10}{:<20}{:<20}{:<15}{:<15}'.format(i[0], i[1], i[2],i[3],i[4]))
                break
        else:
            print("Vehile is not found.")
    elif choice == 4:
        car_no =input("Enter the vehile details: ")
        for i in Carz:
            if i[1] == car_no:
                print("1. Update Name")
                print("2. Update Mobile Number")
                print("3. Update address")
                update_choice = int(input("What would you like to update? "))
                
                if update_choice == 1:
                    i[0] = input("Enter new Name: ")
                elif update_choice == 2:
                    i[3] = int(input("Enter new Mobile Number: "))
                elif update_choice == 3:
                    i[4] =input("Enter new address: ")
                print("Customer details updated successfully!")
                break
        else:
            print("it's not found.")
    elif choice == 5:
        car_no=input("Enter vehicle no to remove: ")
        for i in Carz:
            if i[1] == car_no:
                Carz.remove(i)
                print("Vehicle deleted successfully!")
            break
        else:
            print("Customer not found.")
    elif choice == 6:
        print("Existing ....!")
        break

    else:
        print("Invalid Choice.")

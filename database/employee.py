import sqlite3
con = sqlite3.connect('python/database/emp.db')
try:
    con.execute("CREATE TABLE IF NOT EXISTS employee(emp_id INTEGER PRIMARY KEY, name TEXT, position TEXT, salary REAL)")
except:
    print("Table exists")
while True:
    print("""
          1. Add Employee
          2. View Employees
          3. Update Employee
          4. Search Employee
          5. Delete Employee
          6. Exit
        """)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = float(input("Enter Salary: "))
        con.execute('INSERT INTO employee(emp_id, name, position, salary) VALUES (?, ?, ?, ?)', (emp_id, name, position, salary))
        con.commit()
        print("Employee added successfully.\n")

    elif choice == 2:
        data = con.execute("SELECT * FROM employee")
        print('_' * 60)
        print('{:<10}{:<20}{:<15}{:<10}'.format('EMP ID', 'NAME', 'POSITION', 'SALARY'))
        print('_' * 60)
        for row in data:
            print('{:<10}{:<20}{:<15}{:<10}'.format(row[0], row[1], row[2], row[3]))
        print()

    elif choice == 3:
        emp_id = int(input('Enter the employee ID to update: '))
        data = con.execute('SELECT * FROM employee WHERE emp_id = ?', (emp_id,))
        row = data.fetchone()
        
        if row:
            while True:
                print('''
                        1. Update Name
                        2. Update Position
                        3. Update Salary
                        4. Exit
                ''')
                ch = int(input('Enter your choice: '))
                
                if ch == 1:
                    new_name = input('Enter new name: ')
                    con.execute('UPDATE employee SET name = ? WHERE emp_id = ?', (new_name, emp_id))
                    con.commit()
                    print("Name updated successfully.\n")
                elif ch == 2:
                    new_position = input("Enter new position: ")
                    con.execute('UPDATE employee SET position = ? WHERE emp_id = ?', (new_position, emp_id))
                    con.commit()
                    print("Position updated successfully.\n")
                elif ch == 3:
                    new_salary = float(input("Enter new salary: "))
                    con.execute('UPDATE employee SET salary = ? WHERE emp_id = ?', (new_salary, emp_id))
                    con.commit()
                    print("Salary updated successfully.\n")
                elif ch == 4:
                    break
                else:
                    print("Invalid choice, please try again.")
        else:
            print("Employee ID not found.\n")

    elif choice == 4:
        emp_id = int(input('Enter the employee ID to search: '))
        data = con.execute('SELECT * FROM employee WHERE emp_id = ?', (emp_id,))
        row = data.fetchone()
        
        if row:
            print('_' * 60)
            print('{:<10}{:<20}{:<15}{:<10}'.format('EMP ID', 'NAME', 'POSITION', 'SALARY'))
            print('_' * 60)
            print('{:<10}{:<20}{:<15}{:<10}'.format(row[0], row[1], row[2], row[3]))
            print()
        else:
            print("Employee not found.\n")

    elif choice == 5:
        emp_id = int(input('Enter the employee ID to delete: '))
        con.execute('DELETE FROM employee WHERE emp_id = ?', (emp_id,))
        con.commit()
        print("Employee deleted successfully.\n")

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice, please try again.")

kodeMK = []

while True:
    print("\n-- C R U D --")
    print("1. Add data")
    print("2. Check data")
    print("3. Update data")
    print("4. Delete data")
    print("5. Exit")
    tanya = input("\nChoose an option (1-5): ")
    if tanya == "1":
        kode = input("Enter course code to add: ")
        kodeMK.append(kode)
        print(f"Course code '{kode}' added.")
        while True:
            tanyakode = input("Add another course code? (y/n): ")
            if tanyakode.lower() == 'y':
                kode = input("Enter course code to add: ")
                kodeMK.append(kode)
                print(f"Course code '{kode}' added.")
            elif tanyakode.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    elif tanya == "2":
        if kodeMK:
            print("\nCurrent course codes:")
            for kode in kodeMK:
                print(f"- {kode}")
        else:
            print("\nNo course codes available.")
    elif tanya == "3":
        kode_lama = input("\nEnter the course code to update: ")
        if kode_lama in kodeMK:
            kode_baru = input("Enter the new course code: ")
            index = kodeMK.index(kode_lama)
            kodeMK[index] = kode_baru
            print(f"\nCourse code '{kode_lama}' updated to '{kode_baru}'.")
        else:
            print(f"\nCourse code '{kode_lama}' not found.")
    elif tanya == "4":
        kode_hapus = input("\nEnter the course code to delete: ")
        if kode_hapus in kodeMK:
            kodeMK.remove(kode_hapus)
            print(f"\nCourse code '{kode_hapus}' deleted.")
        else:
            print(f"\nCourse code '{kode_hapus}' not found.")
    elif tanya == "5":
        print("\nExiting the program.")
        break
    else:
        print("\nInvalid option. Please choose a number between 1 and 5.")    


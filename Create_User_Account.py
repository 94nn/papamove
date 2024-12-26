def registration():
    while True:
        print("1. Register")
        print("2. Back")
        Decision = input("Enter your choice: ")

        if Decision == "1":
            UserID = input("Enter your user id: ")
            User_Name = input("Enter your user name: ")
            Password = input("Enter your password: ")
            User_Type = input("Enter your user type (Customer/Driver): ")

            confirmation = input("Confirm registration? (Yes/No): ")
            if confirmation.lower() == "yes":
                with open("users.txt", "a") as file:
                    file.write(f"{UserID},{User_Name},{Password},{User_Type}\n")
                print("Successfully created account")
                return
            else:
                print("Fail to register a new account!")
                return
        else:
            break
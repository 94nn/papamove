import Create_User_Account
import Main_Menu
import os

# Create parceldetails.txt if it doesn't exist
if not os.path.exists("parceldetails.txt"):
    open("parceldetails.txt", "w").close()

def login():
    print("1. Create account")
    print("2. Login")
    print("3. Exit")    
    Decision = input("Enter your choice: ")
    return Decision

def validate_user(UserID, Password):
    with open("users.txt", "r") as file:
        for line in file:
            parts = [part.strip() for part in line.strip().split(",")]
            if len(parts) == 4:
                stored_UserID, stored_User_Name, stored_Password, stored_User_Type = parts
                if UserID == stored_UserID and Password == stored_Password:
                    return True
    return False
    
def process_login():
    while True:
        Decision = login()
        if Decision == "1":
            Create_User_Account.registration()
        elif Decision == "2":
            UserID = input("Enter your user id: ").strip()
            Password = input("Enter your password: ").strip()

            # Validate user
            login_successful = False
            try:
                with open("users.txt", "r") as file:
                    for line in file:
                        # Strip whitespace and split by comma
                        parts = [part.strip() for part in line.strip().split(",")]
                        if len(parts) == 4:  # Make sure we have all 4 parts
                            stored_UserID, stored_User_Name, stored_Password, stored_User_Type = parts
                            if UserID == stored_UserID and Password == stored_Password:
                                print("Login successful!")
                                login_successful = True
                                Main_Menu.main_menu()
                                break
                
                if not login_successful:
                    print("Invalid username or password")
            except FileNotFoundError:
                print("User database not found")
            except ValueError:
                print("Error reading user database")
        else:
            break

if __name__ == "__main__":
   process_login()

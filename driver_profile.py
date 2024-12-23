#Driver's Profile
def vehicle_type():
    while True:
        print("1 Motor")
        print("2 Car")
        print("3 Van")
        Decision = input("Select your vehicle (1/2/3) (or type exit to exit): ").strip().lower()

        if Decision == "1":
            return("Motor")
        elif Decision == "2":
            return("Car")
        elif Decision == "3":
            return("Van")
        elif Decision == "exit":
            print("Exiting")
            exit()
        else:
            print("Invalid input, try again!")



def collect_driver_info():
    contact_info = input("Enter your contact number: ").strip()
    Address = input("Enter your address: ").strip()
    Driving_license = input("Enter your driving license number: ").strip()
    Criminal_records = input("Any criminal records? (Yes/No): ").strip().lower()
    if Criminal_records == "yes":
        print("Explain your criminal records: ")
        Criminal_records_explanation = input("Enter your criminal records explanation: ").strip()
        print("Your criminal records explanation has been submitted to the admin!")
    else:
        Criminal_records = "No"
        Criminal_records_explanation = "No criminal records! Such a good driver!"
    return contact_info, Address, Driving_license, Criminal_records, Criminal_records_explanation


if __name__ == "__main__":
    Vehicle_Type_Selected = vehicle_type()
    contact_info, Address, Driving_license, Criminal_records, Criminal_records_explanation = collect_driver_info()
    print("")
    print("Driver's Profile")
    print("Contact Information: ", contact_info)
    print("Address: ", Address)
    print("Driving License: ", Driving_license)
    print("Your criminal records explanation: ", Criminal_records_explanation)
    print("Vehicle Type: ", Vehicle_Type_Selected)
    print()
    with open("driver_profile.txt", "a") as file:
        file.write(f"{contact_info}\n")
        file.write(f"{Address}\n")
        file.write(f"{Driving_license}\n")
        file.write(f"{Criminal_records}\n")
        file.write(f"{Criminal_records_explanation}\n")
        file.write(f"{Vehicle_Type_Selected}\n")

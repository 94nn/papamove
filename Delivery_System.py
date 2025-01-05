from datetime import datetime

# Create parceldetails.txt if it doesn't exist
try:
    with open("parceldetails.txt", "r"):
        pass
except FileNotFoundError:
    with open("parceldetails.txt", "w"):
        pass

# Function to process login
def login():
    print("\n===== WELCOME TO PAPAMOVE! =====")
    print("1. Create account")
    print("2. Login")
    print("3. Exit")    
    Decision = input("Enter your choice (1/2/3): ")
    return Decision

# Create new account
def registration():
    while True:
        print("\n===== CREATE NEW ACCOUNT =====")
        print("1. Register")
        print("2. Back")
        Decision = input("Enter your choice (1/2): ")

        if Decision == "1":
            UserID = input("Enter your user id: ")
            User_Name = input("Enter your user name: ")
            Password = input("Enter your password: ")
            User_Type = input("Enter your user type (Customer/Driver): ")

            confirmation = input("Confirm registration? (Yes/No): ")
            if confirmation.lower() == "yes":
                with open("users.txt", "a") as file:
                    file.write(f"User ID: {UserID}, User Name: {User_Name}, Password: {Password}, User Type: {User_Type}\n")
                print("Successfully created account")
                return
            else:
                print("Fail to register a new account!")
                return
        elif Decision == "2":
            break
        else:
            print("Invalid input, try again!")

# Function to process payment
def process_payment():
    print("\n===== MAKE PAYMENT =====")
    Card_Number = input("Enter your card number:")
    cvc = input("Enter the CVC:")
    Name = input("Enter the cardholder name:")
    Expired_Date = input("Enter the expired date:")
    Country = input("Enter your country:")
    confirm = input("Confirm payment? (Yes/No): ").lower()
    if confirm == "yes":
        print("Processing payment...")
        print("Payment successful!")
        print("Thank you for choosing our service!")
        print("Returning to main menu...")
        main_menu()
    elif confirm == "no":
        print("Payment canceled. Returning to main menu...")
        main_menu()
    else:
        print("Invalid input, try again!")

def generate_order_id(file_path="parceldetails.txt"):
    try:
        with open(file_path, "r") as file:
            # Read all non-empty lines
            lines = [line.strip() for line in file if line.strip()]
            
            if lines:
                last_entry = lines[-1]  # Get the last entry

                # Find and extract the "Order Number" from the last line
                order_number_str = None
                for part in last_entry.split(","):
                    if "Order Number" in part:
                        order_number_str = part.split(": ")[1].strip()
                        break
                
                if order_number_str:
                    order_number = int(order_number_str) + 1  # Increment the last order number
                else:
                    order_number = 1  # If no valid order number, start from 1
            else:
                order_number = 1  # If file is empty, start from 1
                
    except FileNotFoundError:
        order_number = 1  # If file does not exist, start from 1

    # Format order ID as DXX
    order_id = f"D{order_number:02}"
    return order_id, order_number

# Function to print package info
def print_package_info(Vehicle_Type, Parcel_Weight, Total_Price, order_id, Pick_Up_State, Drop_Off_State, Round_Trip, Quantity_Of_Round_Trip):
    print("\n===== PACKAGE DETAILS =====")
    print(f"Order ID       : {order_id}")
    print(f"Vehicle Type   : {Vehicle_Type}")    
    print(f"Weight (kg)    : {Parcel_Weight}")
    print(f"Pick Up State  : {Pick_Up_State}")
    print(f"Drop Off State : {Drop_Off_State}")
    print(f"Round Trip     : {Round_Trip}")
    print(f"Quantity       : {Quantity_Of_Round_Trip}")
    print(f"Total Price    : RM{float(Total_Price):.2f}")
    print("===========================")

# Function to make payment
def payment(main_menu_callback):
    order_id = generate_order_id()

    with open("parceldetails.txt", "r") as file:
        lines = file.readlines()

        if lines:
            last_line = lines[-1] 
            parts = [part.strip() for part in last_line.split(",")]

            # Create a dictionary to store key-value pairs
            order_data = {}
            for part in parts:
                key, value = part.split(": ", 1)
                order_data[key.strip()] = value.strip()

            # Extract values from the dictionary
            order_id = order_data.get("Order ID")
            Vehicle_Type = order_data.get("Vehicle Type")
            Parcel_Weight = order_data.get("Parcel Weight")
            Pick_Up_State = order_data.get("Pick Up State")
            Drop_Off_State = order_data.get("Drop Off State")
            Round_Trip = order_data.get("Round Trip")
            Quantity_Of_Round_Trip = order_data.get("Quantity Of Round Trip")
            Total_Price = order_data.get("Total Price")

            print_package_info(Vehicle_Type, Parcel_Weight, Total_Price, order_id, Pick_Up_State, Drop_Off_State, Round_Trip, Quantity_Of_Round_Trip)

    confirm = input("Do you want to proceed with payment? (yes/no): ").lower()
    if confirm == "yes":
        process_payment()
        main_menu()
    else:
        print("Order canceled. Returning to main menu...")
        main_menu()

# Function to calculate total price
def count_price(Price, Vehicle_Price, Quantity_Of_Round_Trip, Parcel_Weight):
    Sum_Of_Price = float((Price + Vehicle_Price) * Parcel_Weight)
    Round_Trip_Cost = float((Sum_Of_Price * 0.5) * Quantity_Of_Round_Trip)
    Total_Price = float(Sum_Of_Price + Round_Trip_Cost) 
    return Total_Price

# Function to get route price for motor
def Motor_Route(main_menu_callback, Vehicle_Type, Parcel_Weight, Pick_Up_State, Drop_Off_State, Vehicle_Price, order_id, order_number):
    round_trip_price = {
        ('johor', 'kuala lumpur'): 0.15,
        ('johor', 'butterworth'): 0.30,
        ('johor', 'kedah'): 0.33,
        ('johor', 'perlis'): 0.40,
        ('johor', 'terengganu'): 0.30,
        ('johor', 'kelantan'): 0.30,
        ('kuala lumpur', 'johor'): 0.15,
        ('kuala lumpur', 'butterworth'): 0.15,
        ('kuala lumpur', 'kedah'): 0.18,
        ('kuala lumpur', 'perlis'): 0.25,
        ('kuala lumpur', 'terengganu'): 0.15,
        ('kuala lumpur', 'kelantan'): 0.15,
        ('butterworth', 'johor'): 0.30,
        ('butterworth', 'kuala lumpur'): 0.15,
        ('butterworth', 'kedah'): 0.03,
        ('butterworth', 'perlis'): 0.10,
        ('kedah', 'johor'): 0.33,
        ('kedah', 'kuala lumpur'): 0.18,
        ('kedah', 'butterworth'): 0.03,
        ('kedah', 'perlis'): 0.07,
        ('perlis', 'johor'): 0.40,
        ('perlis', 'kuala lumpur'): 0.25,
        ('perlis', 'butterworth'): 0.10,
        ('perlis', 'kedah'): 0.07,
        ('terengganu', 'johor'): 0.30,
        ('terengganu', 'kuala lumpur'): 0.15,
        ('terengganu', 'kelantan'): 0.00,
        ('kelantan', 'johor'): 0.30,
        ('kelantan', 'kuala lumpur'): 0.15,
        ('kelantan', 'terengganu'): 0.00
    }

    # Use dictionary lookup instead of if-else chain
    route_key = (Pick_Up_State.lower(), Drop_Off_State.lower())

    # Validate route
    if route_key in round_trip_price:
        Price = round_trip_price[route_key]
    else:
        print("Invalid route")
        Price = None
        main_menu()

    Round_Trip = input("Do you want a round trip? (Yes/No)")
    if Round_Trip.lower() == "yes":
        Quantity_Of_Round_Trip = int(input("Enter the quantity of round trip: "))
        Total_Price = count_price(Price, float(Vehicle_Price), Quantity_Of_Round_Trip, float(Parcel_Weight))
    else:
        Quantity_Of_Round_Trip = 0
        Total_Price = count_price(Price, float(Vehicle_Price), Quantity_Of_Round_Trip, float(Parcel_Weight))

    with open("parceldetails.txt", "a") as file:
        file.write(f"Order Number: {order_number}, Order ID: {order_id}, Vehicle Type: {Vehicle_Type}, Parcel Weight: {Parcel_Weight}, Pick Up State: {Pick_Up_State}, Drop Off State: {Drop_Off_State}, Round Trip: {Round_Trip}, Quantity Of Round Trip: {Quantity_Of_Round_Trip}, Vehicle Price: {Vehicle_Price}, Total Price: {Total_Price}\n")
    
    payment(main_menu_callback)

# Function to get route price for car
def Car_Route(main_menu_callback, Vehicle_Type, Parcel_Weight, Pick_Up_State, Drop_Off_State, Vehicle_Price, order_id, order_number):
    # write a dictionary for the price of the round trip in tuple
    round_trip_price = {
        ('johor', 'kuala lumpur'): 0.10,
        ('johor', 'butterworth'): 0.20,
        ('johor', 'kedah'): 0.22,
        ('johor', 'perlis'): 0.24,
        ('johor', 'terengganu'): 0.20,
        ('johor', 'kelantan'): 0.20,
        ('kuala lumpur', 'johor'): 0.10,
        ('kuala lumpur', 'butterworth'): 0.10,
        ('kuala lumpur', 'kedah'): 0.12,
        ('kuala lumpur', 'perlis'): 0.14,
        ('kuala lumpur', 'terengganu'): 0.10,
        ('kuala lumpur', 'kelantan'): 0.10,
        ('butterworth', 'johor'): 0.20,
        ('butterworth', 'kuala lumpur'): 0.10,
        ('butterworth', 'kedah'): 0.02,
        ('butterworth', 'perlis'): 0.04,
        ('kedah', 'johor'): 0.22,
        ('kedah', 'kuala lumpur'): 0.12,
        ('kedah', 'butterworth'): 0.02,
        ('kedah', 'perlis'): 0.02,
        ('perlis', 'johor'): 0.24,
        ('perlis', 'kuala lumpur'): 0.14,
        ('perlis', 'butterworth'): 0.04,
        ('perlis', 'kedah'): 0.02,
        ('terengganu', 'johor'): 0.20,
        ('terengganu', 'kuala lumpur'): 0.10,
        ('terengganu', 'kelantan'): 0.00,
        ('kelantan', 'johor'): 0.20,
        ('kelantan', 'kuala lumpur'): 0.10,
        ('kelantan', 'terengganu'): 0.00
    }

    # Use dictionary lookup instead of if-else chain
    route_key = (Pick_Up_State.lower(), Drop_Off_State.lower())

    # Validate route
    if route_key in round_trip_price:
        Price = round_trip_price[route_key]
    else:
        print("Invalid route")
        Price = None
        main_menu()

    Round_Trip = input("Do you want a round trip? (Yes/No)")
    if Round_Trip.lower() == "yes":
        Quantity_Of_Round_Trip = int(input("Enter the quantity of round trip: "))
        Total_Price = count_price(Price, float(Vehicle_Price), Quantity_Of_Round_Trip, float(Parcel_Weight))
    else:
        Quantity_Of_Round_Trip = 0
        Total_Price = count_price(Price, float(Vehicle_Price), Quantity_Of_Round_Trip, float(Parcel_Weight))

    with open("parceldetails.txt", "a") as file:
        file.write(f"Order Number: {order_number}, Order ID: {order_id}, Vehicle Type: {Vehicle_Type}, Parcel Weight: {Parcel_Weight}, Pick Up State: {Pick_Up_State}, Drop Off State: {Drop_Off_State}, Round Trip: {Round_Trip}, Quantity Of Round Trip: {Quantity_Of_Round_Trip}, Vehicle Price: {Vehicle_Price}, Total Price: {Total_Price}\n")
    
    payment(main_menu_callback)

# Function to get route price for van
def Van_Route(main_menu_callback, Vehicle_Type, Parcel_Weight, Pick_Up_State, Drop_Off_State, Vehicle_Price, order_id, order_number):
    round_trip_price = {
        ('johor', 'kuala lumpur'): 0.05,
        ('johor', 'butterworth'): 0.10,
        ('johor', 'kedah'): 0.11,
        ('johor', 'perlis'): 0.12,
        ('johor', 'terengganu'): 0.10,
        ('johor', 'kelantan'): 0.10,
        ('kuala lumpur', 'johor'): 0.05,
        ('kuala lumpur', 'butterworth'): 0.05,
        ('kuala lumpur', 'kedah'): 0.06,
        ('kuala lumpur', 'perlis'): 0.07,
        ('kuala lumpur', 'terengganu'): 0.05,
        ('kuala lumpur', 'kelantan'): 0.05,
        ('butterworth', 'johor'): 0.10,
        ('butterworth', 'kuala lumpur'): 0.05,
        ('butterworth', 'kedah'): 0.01,
        ('butterworth', 'perlis'): 0.02,
        ('kedah', 'johor'): 0.11,
        ('kedah', 'kuala lumpur'): 0.06,
        ('kedah', 'butterworth'): 0.01,
        ('kedah', 'perlis'): 0.01,
        ('perlis', 'johor'): 0.12,
        ('perlis', 'kuala lumpur'): 0.11,
        ('perlis', 'butterworth'): 0.02,
        ('perlis', 'kedah'): 0.01,
        ('terengganu', 'johor'): 0.10,
        ('terengganu', 'kuala lumpur'): 0.05,
        ('terengganu', 'kelantan'): 0.00,
        ('kelantan', 'johor'): 0.10,
        ('kelantan', 'kuala lumpur'): 0.05,
        ('kelantan', 'terengganu'): 0.00
    }

    route_key = (Pick_Up_State.lower(), Drop_Off_State.lower())

    if route_key in round_trip_price:
        Price = round_trip_price[route_key]
    else:
        print("Invalid route")
        Price = None
        main_menu()

    Round_Trip = input("Do you want a round trip? (Yes/No)")
    if Round_Trip.lower() == "yes":
        Quantity_Of_Round_Trip = int(input("Enter the quantity of round trip: "))
        Total_Price = count_price(Price, float(Vehicle_Price), Quantity_Of_Round_Trip, float(Parcel_Weight))
    else:
        Quantity_Of_Round_Trip = 0
        Total_Price = count_price(Price, float(Vehicle_Price), Quantity_Of_Round_Trip, float(Parcel_Weight))

    with open("parceldetails.txt", "a") as file:
        file.write(f"Order Number: {order_number}, Order ID: {order_id}, Vehicle Type: {Vehicle_Type}, Parcel Weight: {Parcel_Weight}, Pick Up State: {Pick_Up_State}, Drop Off State: {Drop_Off_State}, Round Trip: {Round_Trip}, Quantity Of Round Trip: {Quantity_Of_Round_Trip}, Vehicle Price: {Vehicle_Price}, Total Price: {Total_Price}\n")
    
    payment(main_menu_callback)

def track_order():
    # Parse package information into a dictionary
    package_data = {}
    parcel_ids = []  

    with open("parcel_status.txt", "r") as package_file:
        for line in package_file:
            parts = [part.strip() for part in line.strip().split(",")]

            if len(parts) == 6:
                try:
                    parcel_id = parts[0].split("-")[1].strip().lower()
                    parcel_status = parts[1].split("-")[1].strip()
                    pick_up_time = parts[2].split("-")[1].strip() 

                    if ' ' in pick_up_time:
                        pick_up_time = pick_up_time.replace(' ', '') 

                    arrival_time = parts[3].split("-")[1].strip()
                    current_location = parts[4].split("-")[1].strip()

                    parcel_ids.append(parcel_id)

                    package_data[parcel_id] = {
                        "parcel_id": parcel_id,
                        "parcel_status": parcel_status,
                        "pick_up_time": pick_up_time,
                        "arrival_time": arrival_time,
                        "current_location": current_location
                    }
                except IndexError as e:
                    print(f"Error processing line: {line} (Error: {e})")
            else:
                print(f"Skipped invalid line in parcel_status.txt: {line}")

    while True:
        order_id = input("Enter your Order ID: ").strip().lower()

        # Validate if the order_id exists in the parcel_ids list
        if order_id not in parcel_ids:
            print("Pop Up: Invalid Order ID")
            main_menu()

        if order_id in package_data:
            order = package_data[order_id]
            if order["parcel_status"].lower() == "picked up":
                print(f"Picked Up Time: {order['pick_up_time']}, Parcel Picked Up")
            elif order["parcel_status"].lower() == "delivered":
                print(f"Arrival Time: {order['arrival_time']}, Parcel Delivered")
            else:
                print(f"Current location: {order['current_location']}, Parcel in Transit")
        else:
            print("Order ID exists in parcel details but no tracking information is available yet.")

        print("\nOptions:")
        print("1. Track another order")
        print("2. Back to main menu")
        decision = input("Enter your choice (1/2): ").strip()

        if decision != "1":
            print("Exiting order tracking.")
            main_menu()

def main_menu():
    print("\n===== MAIN MENU =====")
    print("1. Make Order")
    print("2. Track Order")
    print("3. Exit")
    
    Decision = input("Enter your decision: ")

    if Decision == "1":
        print("\n===== PARCEL DETAILS =====")
        print("1. Motor")
        print("2. Car")
        print("3. Van")

        Vehicle = input("Select your vehicle type (1/2/3): ")
        Parcel_weight = input("Enter your parcel weight (kg): ")
        print("1. Johor \n2. Kuala Lumpur \n3. Butterworth \n4. Kedah \n5. Perlis \n6. Kelantan \n7. Terengganu")
        Pick_Up_State = input("Enter your desired pick up state: ")
        Drop_Off_State = input("Enter your desired drop off state: ")

        if Vehicle == "1":
            Vehicle_Type = "Motor"
            Vehicle_Price = 5
            order_id, order_number = generate_order_id()
            Motor_Route(main_menu, Vehicle_Type, Parcel_weight, Pick_Up_State, Drop_Off_State, Vehicle_Price, order_id, order_number)
        elif Vehicle == "2":
            Vehicle_Type = "Car"
            Vehicle_Price = 8
            order_id, order_number = generate_order_id()
            Car_Route(main_menu, Vehicle_Type, Parcel_weight, Pick_Up_State, Drop_Off_State, Vehicle_Price, order_id, order_number)
        else:
            Vehicle_Type = "Van"
            Vehicle_Price = 18
            order_id, order_number = generate_order_id()
            Van_Route(main_menu, Vehicle_Type, Parcel_weight, Pick_Up_State, Drop_Off_State, Vehicle_Price, order_id, order_number)

    elif Decision == "2":
        track_order()
    elif Decision == "3":
        print("Exiting...")
        process_login()
    else:
        print("Invalid input, try again!")
        main_menu()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#============================ Driver ===============================
def current_hub():
    while True:
        print("\n=============== Locations =================")
        print("1 Johor")
        print("2 Kuala Lumpur")
        print("3 Butterworth")
        print("4 Kedah")
        print("5 Perlis")
        print("6 Kelantan")
        print("7 Terengganu")
        Decision = input("Select your current location (1/2/3/4/5/6/7) (or type exit to exit): ").strip().lower()

        if Decision == "1":
            return("Johor")
        elif Decision == "2":
            return("Kuala Lumpur")
        elif Decision == "3":
            return("Butterworth")
        elif Decision == "4":
            return("Kedah")
        elif Decision == "5":
            return("Perlis")
        elif Decision == "6":
            return("Kelantan")
        elif Decision == "7":
            return("Terengganu")
        elif Decision == "exit":
            print("Exiting")
            driver_menu()
        else:
            print("Invalid input, try again!")
            current_hub()

def parcel_status(UserID):
    Current_location = current_hub()  

    Parcel_id = input("Enter parcel ID: ").strip()
    updated_lines = []
    parcel_found = False  

    # with open("package_info.txt", "r") as file:
    with open("parceldetails.txt", "r") as file:
        for line in file:
            parts = [part.split(":")[1].strip() for part in line.strip().split(",") if ":" in part]
            if len(parts) != 10:
                print(f"Skipped invalid line: {line.strip()}")
                updated_lines.append(line)
                continue

            # Unpack parcel information
            order_number, order_id, vehicle_type, Parcel_Weight, pick_up_state, drop_off_state, Round_Trip, Quantity_Of_Round_Trip, Vehicle_Price, Total_Price = parts

            if Parcel_id == order_id:
                parcel_found = True

                # Update status based on current hub location
                if pick_up_state.lower() == Current_location.lower():
                    parcel_status = "Picked up"
                    pick_up_time = datetime.now().strftime("%H:%M")
                    arrival_time = ""
                elif drop_off_state.lower() == Current_location.lower():
                    parcel_status = "Delivered"
                    pick_up_time = ""
                    arrival_time = datetime.now().strftime("%H:%M")
                else:
                    parcel_status = "In Transit"
                    pick_up_time = ""
                    arrival_time = ""
                
                with open("parcel_status.txt", "a") as file:
                    file.write(f"Parcel ID - {Parcel_id}, Parcel Status - {parcel_status}, Pick Up Time - {pick_up_time}, Arrival Time - {arrival_time}, Current Location - {Current_location}, Driver ID - {UserID}\n")

    # Check if parcel ID was not found
    if not parcel_found:
        print("Invalid parcel ID, try again!")
        return

    print("Parcel status updated successfully.")

def add_maintenance_form_txt(UserID, stored_Vehicle_Plate, stored_Vehicle_Type, vehicle_status, Service_Type, Repair_Cost, Maintenance_Date):
    with open("maintenance_form.txt","a") as file:
        file.write(f"UserID: {UserID}, Vehicle Plate: {stored_Vehicle_Plate}, Vehicle Type: {stored_Vehicle_Type}, Vehicle Status: {vehicle_status}, Service Type: {Service_Type}, Repair Cost: {Repair_Cost}, Maintenance Date: {Maintenance_Date}\n")

def maintenance_form():
    print("\n=================== Please fill up the maintenance claim form to the admin! ===================")
    UserID = input("Enter your user ID: ").strip() 
    print("1. Proceed\n2. Exit")
    Decision = input("Enter your decision (1/2):")

    if Decision == "1":
        with open("driver_profile.txt", "r") as file:
            lines = file.readlines()
            if lines:
                for line in lines:
                    parts = [part.strip() for part in line.strip().split(",")]
                    parts = [item.split(":") for item in parts if len(item.split(":")) == 2]
                    parts = [item[1].strip() for item in parts]

                    if len(parts) == 8:  
                        stored_userID = parts[0]  
                        stored_Contact_info = parts[1]
                        stored_Address = parts[2]
                        stored_Driving_license = parts[3]
                        stored_Vehicle_Type = parts[4]
                        stored_Vehicle_Plate = parts[5]
                        stored_Criminal_records = parts[6]
                        stored_Criminal_records_explanation = parts[7]

                        if UserID == stored_userID.strip():
                            Service_Type = input("Enter your service type(engine/brake/aircon/others): ")
                            Repair_Cost = float(input("Enter your repair cost(RM): "))
                            Maintenance_Date = input("Enter your maintenance date(DD-MM-YYYY): ")
                            vehicle_status = "bad"

                            add_maintenance_form_txt(UserID, stored_Vehicle_Plate, stored_Vehicle_Type, vehicle_status, Service_Type, Repair_Cost, Maintenance_Date)

                            print("\n===== Maintenance Claim Form =====")
                            print("Vehicle Plate: ", stored_Vehicle_Plate)
                            print("UserID: ", UserID)
                            print("Vehicle Type: ", stored_Vehicle_Type)
                            print("Service Type: ", Service_Type)
                            print("Repair Cost: ", Repair_Cost)
                            print("Maintenance Date: ", Maintenance_Date)
                            print("Your maintenance claim form has been submitted to the admin!")
                            print("Thank you! Have a good day!")  
                            driver_menu(UserID)
                else:
                    print("Invalid user ID, try again!")
                    maintenance_form() 
    elif Decision == "2":
        driver_menu(UserID)
    else:
        print("Invalid input, try again!")
        maintenance_form()

def vehicle_status(UserID):
    print("\n============== You are in vehicle status page. ==============")
    while True:
        Update_vehicle = input("Enter your vehicle status (Good/Bad): ")
        if Update_vehicle.lower() == "good":
            vehicle_status = "good"
            Service_Type = "No Service Type"
            Repair_Cost = "No Repair Cost"
            Maintenance_Date = "No Maintenance Date"
            with open("driver_profile.txt", "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1]
                    parts = []
                    for part in last_line.strip().split(","):
                        split_part = part.split(":")
                        if len(split_part) == 2:
                            parts.append(split_part[1].strip())
                        else:
                            print(f"Warning: Invalid format in line: {part}")
                            parts.append("")  

                    if len(parts) == 8:
                        stored_userID, stored_Contact_info, stored_Address, stored_Driving_license, stored_Vehicle_Type, stored_Vehicle_Plate, stored_Criminal_records, stored_Criminal_records_explanation = parts
                    else:
                        print("Error: Incorrect number of parts in profile data.")
                        return

            print("No need to send for maintenance!")
            add_maintenance_form_txt(UserID, stored_Vehicle_Plate, stored_Vehicle_Type, vehicle_status, Service_Type, Repair_Cost, Maintenance_Date)
            driver_menu(UserID)
        elif Update_vehicle.lower() == "bad": 
            print("Send for maintenance!")
            maintenance_form()
            driver_menu(UserID)
        else:
            print("Invalid input, try again!")

def Maintenance_monthly(UserID):
    print("\n=================== Welcome to the maintenance monthly check! ===================")
    with open("driver_profile.txt", "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            parts = [part.split(":")[1].strip() for part in last_line.strip().split(",")]

            if len(parts) == 8:
                stored_userID, stored_Contact_info, stored_Address, stored_Driving_license, stored_Vehicle_Type, stored_Vehicle_Plate, stored_Criminal_records, stored_Criminal_records_explanation = parts

                Maintenance_Date = input("Enter your maintenance date(DD-MM-YYYY): ")
                Maintenance_Result = input("Enter your maintenance result (Good/Bad): ")
                print("1. Proceed\n2. Exit")
                Decision = input("Enter your decision (1/2):")
                if Decision == "1":
                    if Maintenance_Result.lower() == "good":
                        vehicle_status = "good"
                        Service_Type = "No Service Type"
                        Repair_Cost = "No Repair Cost"
                        print("No need to send for service!")
                        print("\n========== Updated Maintenance Form ==========")
                        print("UserID: ", UserID)
                        print("Vehicle Plate: ", stored_Vehicle_Plate)
                        print("Vehicle Type: ", stored_Vehicle_Type)
                        print("Maintenance Date: ", Maintenance_Date)
                        print("Your maintenance has been updated!")
                        print("Thank you! Have a good day!")
                        add_maintenance_form_txt(UserID, stored_Vehicle_Plate, stored_Vehicle_Type, vehicle_status, Service_Type, Repair_Cost, Maintenance_Date)
                        driver_menu(UserID)
                    elif Maintenance_Result.lower() == "bad":
                        print("Send for service!")
                        maintenance_form()
                    else:
                        print("Invalid input, try again!")
                        Maintenance_monthly(UserID)
        else:
            print("No driver data found.")       

def fuel_management():
    print("\n=================== Welcome to fuel management page! ===================")
    UserID = input("Enter your user ID: ")
    print("1. Proceed\n2. Exit")
    Decision = input("Enter your decision (1/2): ")
    if Decision == "1":
        Vehicle_Type = input("Enter your vehicle type (motor/car/van): ")
        selected_hub = current_hub()
        fuel_levels = input("Enter your current fuel levels (high/low): ")
        last_refuel_date = input("Enter the date where you last refuel your fuel (DD-MM-YYYY): ")
        if fuel_levels.lower() == "low":
            print("\nSend to refuel!!!")
            refuel_date = input("Enter your date of refueling (DD-MM-YYYY): ")
            refuel_time = input("Enter the time of refueling (HH:MM): ")    
            refuel_quantity = input("Enter how many litres you refueled: ")
            refuel_cost = input("Enter the refuel amount (RM): ")
            mileage = ""
            remaining_fuel = ""
            print("\n=================== Fuel Management Record ===================")
            print("Your refuel date of the vehicle:", refuel_date)
            print("Your refuel time is at:", refuel_time)
            print("Your refuel quantity at:", refuel_quantity , "litres")
            print("Your refuel cost at:RM", refuel_cost)
            print("Your fuel status has been send to admin! Thank you!")
            print("Have a great journey ahead!") 
            print("================================================================")
        else: 
            mileage = input("Enter your mileage(km): ")
            remaining_fuel = input("Enter your remaining fuel levels: ")
            refuel_date = ""
            refuel_time = ""    
            refuel_quantity = ""
            refuel_cost = ""
            print("\n=================== Fuel Management Record ===================")
            print("Your current mileage is at:", mileage, "km")
            print("Your current fuel levels is at:", remaining_fuel, "litres")
            print("Your fuel status has been send to admin! Thank you!")
            print("Have a great journey ahead!")  
            print("================================================================")

        with open("driver_fuel_management.txt", "a") as file:
            file.write(f"Driver ID: {UserID}, Vehicle Type: {Vehicle_Type}, Selected Hub: {selected_hub}, Fuel Levels: {fuel_levels}, Last Refuel Date: {last_refuel_date}, Refuel Date: {refuel_date}, Refuel Time: {refuel_time}, Refuel Quantity: {refuel_quantity}, Refuel Cost: {refuel_cost}, Mileage: {mileage}, Remaining Fuel: {remaining_fuel}\n")
        driver_menu(UserID)
    elif Decision == "2":
        driver_menu(UserID)
    else:
        print("Invalid input, try again!")
        fuel_management()

def driver_input_availability(UserID):
    availability_status = input("Enter your availability status (available/not available): ").strip().lower()

    if availability_status == "available":
        time_schedule = "Sample Time Schedule"  # Placeholder for actual data
        package_info = "Sample Package Info"    # Placeholder for actual data
        route = "Sample Route"                  # Placeholder for actual data
        Current_hub = ""
        print("\n=================== New Task Assigned!!! ===================")
        print(f"Time Schedule: {time_schedule}")
        print(f"Package Info: {package_info}")
        print(f"Route: {route}")
        print("================================================================")
        task_assigned = "yes"
          
    elif availability_status == "not available":
        Current_hub = current_hub()
        task_assigned = ""
        print("\n============== Driver availability status has been updated! ==============")
    
    else:
        print("Invalid input, try again!")
        driver_availability()

    with open("driver_availability.txt", "a") as file:
        file.write(f"UserID: {UserID}, Availability Status: {availability_status}, Current Hub: {Current_hub}, Task Assigned: {task_assigned}\n")
    driver_menu(UserID)

def driver_menu(UserID):
    print("\n=================== Welcome to driver page! How are you today? ===================")
    while True:
        print("1. Vehicle status")
        print("2. Maintenance monthly")
        print("3. Update parcel status")
        print("4. Fuel Management")
        print("5. Driver Availability")
        print("6. Exit")
        Decision = input("Which page you want do to go to? (1/2/3/4/5/6): ").strip().lower()

        if Decision == "1":
            vehicle_status(UserID)
        elif Decision == "2":
            Maintenance_monthly(UserID)
        elif Decision == "3":
            parcel_status(UserID)
        elif Decision == "4":
            fuel_management()
        elif Decision == "5":
            driver_input_availability(UserID)
        elif Decision == "6":
            print("Exiting")
            process_login()
        else:
            print("Invalid input, try again!")

def vehicle_type(UserID, Contact_info, Address, Driving_license, Criminal_records, Criminal_records_explanation):
    while True:
        print("\n===== Vehicle Type =====")
        print("1 Motor")
        print("2 Car")
        print("3 Van")
        Decision = input("Select your vehicle (1/2/3) (or type exit to return to main menu): ").strip().lower()

        if Decision == "1":
            Vehicle_Type = "Motor"
            Vehicle_Plate = input("Enter your vehicle plate number: ")
            with open("driver_profile.txt", "a") as file:
                file.write(f"Driver ID: {UserID}, Contact Info: {Contact_info}, Address: {Address}, Driving License: {Driving_license}, Vehicle Type: {Vehicle_Type}, Vehicle Plate: {Vehicle_Plate}, Criminal Records: {Criminal_records}, Criminal Records Explanation: {Criminal_records_explanation}\n")
            print_driver_profile(UserID, Contact_info, Address, Driving_license, Vehicle_Type, Vehicle_Plate, Criminal_records_explanation)
            driver_menu(UserID)
        elif Decision == "2":
            Vehicle_Type = "Car"
            Vehicle_Plate = input("Enter your vehicle plate number: ")
            with open("driver_profile.txt", "a") as file:
                file.write(f"Driver ID: {UserID}, Contact Info: {Contact_info}, Address: {Address}, Driving License: {Driving_license}, Vehicle Type: {Vehicle_Type}, Vehicle Plate: {Vehicle_Plate}, Criminal Records: {Criminal_records}, Criminal Records Explanation: {Criminal_records_explanation}\n")
            print_driver_profile(UserID, Contact_info, Address, Driving_license, Vehicle_Type, Vehicle_Plate, Criminal_records_explanation)
            driver_menu(UserID)
        elif Decision == "3":
            Vehicle_Type = "Van"
            Vehicle_Plate = input("Enter your vehicle plate number: ")
            with open("driver_profile.txt", "a") as file:
                file.write(f"Driver ID: {UserID}, Contact Info: {Contact_info}, Address: {Address}, Driving License: {Driving_license}, Vehicle Type: {Vehicle_Type}, Vehicle Plate: {Vehicle_Plate}, Criminal Records: {Criminal_records}, Criminal Records Explanation: {Criminal_records_explanation}\n")
            print_driver_profile(UserID, Contact_info, Address, Driving_license, Vehicle_Type, Vehicle_Plate, Criminal_records_explanation)
            driver_menu(UserID)
        elif Decision == "exit":
            Vehicle_Type = "Nothing"
            Vehicle_Plate = "Nothing"
            with open("driver_profile.txt", "a") as file:
                file.write(f"Driver ID: {UserID}, Contact Info: {Contact_info}, Address: {Address}, Driving License: {Driving_license}, Vehicle Type: {Vehicle_Type}, Vehicle Plate: {Vehicle_Plate}, Criminal Records: {Criminal_records}, Criminal Records Explanation: {Criminal_records_explanation}\n")
            print("Exiting")
            process_login()
        else:
            print("Invalid input, try again!")
            vehicle_type()

def collect_driver_info(UserID):
    Decision = input("Have you entered your driver info? (yes/no):")
    if Decision.lower() == "no":
        Contact_info = input("Enter your contact number: ").strip()
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
        vehicle_type(UserID, Contact_info, Address, Driving_license, Criminal_records, Criminal_records_explanation)
    elif Decision.lower() == "yes":
        driver_menu(UserID)
    else:
        print("Invalid input, try again!")
        collect_driver_info(UserID)

def print_driver_profile(UserID, Contact_info, Address, Driving_license, Vehicle_Type, Vehicle_Plate, Criminal_records_explanation):
    print("\n===== Driver's Profile =====")
    print("User ID:", UserID)
    print("Contact Information:", Contact_info)
    print("Address:", Address)
    print("Driving License:", Driving_license)
    print("Vehicle Type:", Vehicle_Type)
    print("Vehicle Plate:", Vehicle_Plate)
    print("Your criminal records explanation:", Criminal_records_explanation)
    print("===========================")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#============================ Admin ===============================
#define admin main dashboard
def admin_dashboard():
    print("\n--- Welcome to the Admin Dashboard ---")
    while True:
        admin_menu_choice = int(input("1. Vehicle Management\n2. Fuel Management\n3. Driver Management\n4. Reports\n5. Log Out\nEnter your choice number: "))
        
        #check admin menu option
        if admin_menu_choice == 1:
            vehicle_mgmt()
        elif admin_menu_choice == 2:
            fuel_mgmt()
        elif admin_menu_choice == 3:
            driver_mgmt()
        elif admin_menu_choice == 4:
            reports()
        elif admin_menu_choice == 5:   
            print("\nLogged Out!")
            process_login()
        else:
            print("\nInvalid choice. Try again.")
            admin_dashboard()

#*vehicle management* functions:
#1 - define view vehicle performance history page
def vehicle_performance():
    driver_id = input("\nEnter the driver's ID to view its performance history: ")
    print(f"\nVehicle Performance of Driver {driver_id}")
    try:
        with open("maintenance_form.txt", "r") as file:
            found = False
            for line in file:
                parts = [part.split(":")[1].strip() for part in line.strip().split(",")]
                if len(parts) == 7:
                    UserID, Vehicle_Plate, Vehicle_Type, Vehicle_Status, Service_Type, Repair_Cost, Maintenance_Date = parts
                    if driver_id == UserID:
                        found = True
                        if Vehicle_Status.lower() == "good":
                            print("Vehicle Status: Good")
                            view_choice = int(input("\nChoose one to proceed:\n1. View other vehicle's performance history\n"
                                                    "2. Back to Vehicle Management Main Page\n"
                                                    "3. Back to Admin Dashboard\nEnter your choice number: "))
                            if view_choice == 1:
                                vehicle_performance()
                            elif view_choice == 2:
                                vehicle_mgmt()
                            elif view_choice == 3:
                                admin_dashboard()
                            else:
                                print("\nInvalid choice. Returning to Vehicle Management.")
                                vehicle_mgmt()
                        else:
                            view_choice = input("Vehicle Status: Under Maintenance\nView Maintenance History? Yes/No: ")
                            if view_choice.lower() == "yes":
                                vehicle_maintenance()
                            elif view_choice.lower() == "no":
                                view_choice = int(input("\nChoose one to proceed:\n1. View other vehicle's performance history\n"
                                                        "2. Back to Vehicle Management Main Page\n"
                                                        "3. Back to Admin Dashboard\nEnter your choice number: "))
                                if view_choice == 1:
                                    vehicle_performance()
                                elif view_choice == 2:
                                    vehicle_mgmt()
                                elif view_choice == 3:
                                    admin_dashboard()
                                else:
                                    print("\nInvalid choice. Returning to Vehicle Management.")
                                    vehicle_mgmt()
                            else:
                                print("\nInvalid choice. Returning to Vehicle Management.")
                                vehicle_mgmt()
            if not found:
                print(f"\nNo performance data found for driver ID {driver_id}.")
    except FileNotFoundError:
        print("\nPerformance data file not found.")
    except ValueError:
        print("\nThe data in the file is not in the expected format.")

#2.1 - read vehicle maintenance history txt file
def read_maintenance_history(driver_id):
    try:
        with open("maintenance_form.txt", "r") as file:
            lines = file.readlines()

        print(f"\nMaintenance history for Driver ID: {driver_id}")
        found = False
        for line in lines: 
            try:
                parts = [part.split(":")[1].strip() for part in line.strip().split(",")]

                if len(parts) == 7:
                    UserID, Vehicle_Plate, Vehicle_Type, Vehicle_Status, Service_Type, Repair_Cost, Maintenance_Date = parts
                    if driver_id.strip().lower() == UserID.strip().lower():
                        found = True
                        print(f"Vehicle Plate: {Vehicle_Plate}")
                        print(f"Vehicle Type: {Vehicle_Type}")
                        print(f"Vehicle Status: {Vehicle_Status}")
                        print(f"Service Type: {Service_Type}")
                        print(f"Repair Cost: RM{Repair_Cost}")
                        print(f"Maintenance Date: {Maintenance_Date}")
                        print()

            except (IndexError, ValueError) as e:
                print(f"\nSkipping invalid record: {line.strip()} (Error: {e})")

        if not found:
            print(f"\nNo maintenance history found for Driver ID {driver_id}.")

    except FileNotFoundError:
        print(f"\nError: File not found at 'maintenance_form.txt'.")

#2 - define view vehicle maintenance history page
def vehicle_maintenance():
    driver_id = input("\nEnter the driver's ID to view its maintenance history: ")
    read_maintenance_history(driver_id)

    view_choice = int(input("\nChoose one to proceed:\n1. View other vehicle's maintenance history\n2. Back to Vehicle Management Main Page\n3. Back to Admin Dashboard\nEnter your choice number: "))
    if view_choice == 1:
        vehicle_maintenance()
    elif view_choice == 2:
        vehicle_mgmt()
    elif view_choice == 3:
        admin_dashboard()
    else:
        print("\nInvalid choice. Returning to Vehicle Management.")
        vehicle_mgmt()

#3.1 - save vehicles inspection to txt file
def save_vehicles_to_txt(vehicles, file_path):
    # Save the vehicles dictionary to a text file
    with open(file_path, 'w') as file:
        for driver_id, data in vehicles.items():
            # Construct the vehicle_dict string representation with driver_id as a string, not a list
            vehicle_dict = (
                f"{{'driver_id': '{driver_id}', "
                f"'maintenance_alerts': {data['maintenance_alerts']}, "
                f"'inspection_schedule': {data['inspection_schedule']}}}"
            )
            file.write(f"{vehicle_dict}\n")

#3.2 - read vehicles inspection data in txt file
def load_vehicles_from_txt(file_path):
    vehicles = {}
    # Load the vehicles dictionary from txt file
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Parse the line as a dictionary string manually
                try:
                    # Removing surrounding spaces and handling the dictionary format manually
                    line = line.strip().replace("'", '"') 
                    if line.startswith('{') and line.endswith('}'):
                        vehicle_data = eval(line)

                        # Extract the driver_id directly as a string (not a list)
                        driver_id = vehicle_data['driver_id']

                        alerts = vehicle_data.get('maintenance_alerts', [])
                        schedules = vehicle_data.get('inspection_schedule', [])

                        # Save the data into the vehicles dictionary
                        vehicles[driver_id] = {
                            "maintenance_alerts": alerts,
                            "inspection_schedule": schedules
                        }
                    else:
                        print(f"\nSkipping invalid line: {line}")
                except (SyntaxError, ValueError, NameError):
                    print(f"\nSkipping invalid line: {line}")
    except FileNotFoundError:
        print("\nFile not found.")
    
    return vehicles

#3.3 - plan inspection for a vehicle
def plan_inspection(vehicles, driver_id, inspection_date, alert_message):
    if driver_id in vehicles:
        vehicles[driver_id]["maintenance_alerts"].append(alert_message)
        vehicles[driver_id]["inspection_schedule"].append(inspection_date)
        print(f"\nInspection planned for vehicle {driver_id} on {inspection_date} with alert: '{alert_message}'.")
    else:
        print(f"\nDriver {driver_id} not found.")

#3.4 - view vehicle inspection schedule
def get_vehicle_data(vehicles, driver_id):
    try:
        #convert driver_id to an integer to match the dictionary key type
        driver_id = driver_id
        if driver_id in vehicles:
            return {
                "Maintenance Alerts": vehicles[driver_id]["maintenance_alerts"],
                "Inspection Schedule": vehicles[driver_id]["inspection_schedule"]
            }
        else:
            print(f"\nVehicle {driver_id} not found.")
            return None
    except ValueError:
        #handle cases where input cannot be converted to an integer
        print("\nInvalid vehicle ID. Please enter a numeric ID.")
        return None
    
#3 - define plan vehicle inspections, get vehicle maintenance alerts and schedules page
def vehicle_inspections():
    file_path = 'vehicles.txt'
    vehicles = load_vehicles_from_txt(file_path)
    
    while True:
        choice = int(input("\n--- Vehicle Inspection Planner ---\n1. Plan an inspection for a vehicle\n2. View vehicle inspection schedule\n3. Save inspection plan and exit\nEnter your choice number: "))

        if choice == 1:
            #plan an inspection
            driver_id = input("\nEnter the driver ID to plan inspection for: ").strip()
            inspection_date = input("Enter the inspection date (YYYY-MM-DD): ").strip()
            alert_message = input("Enter the maintenance alert message: ").strip()
            plan_inspection(vehicles, driver_id, inspection_date, alert_message)
        elif choice == 2:
            #view vehicle schedule
            driver_id = input("\nEnter the driver ID to view its inspection schedule: ").strip()
            data = get_vehicle_data(vehicles, driver_id)
            if data:
                print(f"\nInspection Schedule for Vehicle {driver_id}:")
                print("\nMaintenance Alerts:")
                if data["Maintenance Alerts"]:
                    for alert in data["Maintenance Alerts"]:
                        if alert:  #check to avoid printing empty alerts
                            print(f"- {alert}")
                else:
                    print("\nNo maintenance alerts found.")

                print("\nInspection Dates:")
                if data["Inspection Schedule"]:
                    for date in data["Inspection Schedule"]:
                        if date:  #check to avoid printing empty dates
                            print(f"- {date}")
                else:
                    print("\nNo inspection dates found.")
        elif choice == 3:
            #save inspection plan to file and exit
            save_vehicles_to_txt(vehicles, file_path)
            print("\nData saved. Exiting...")
            vehicle_mgmt()
        else:
            print("\nInvalid choice. Please try again.")

#define *vehicle management* main page
def vehicle_mgmt():
    print("\n--- Vehicle Management Page ---")
    vehicle_menu_choice = int(input("1. View Performance History\n2. View Maintenance History\n3. Plan Inspections, View Maintenance Alerts & Schedules\n4. Back to Admin Dashboard\nEnter your choice number: "))
    
    #check vehicle menu choice
    if vehicle_menu_choice == 1:
        vehicle_performance()
    elif vehicle_menu_choice == 2:
        vehicle_maintenance()
    elif vehicle_menu_choice == 3:
        vehicle_inspections()
    elif vehicle_menu_choice == 4:
        admin_dashboard()
    else:
        print("\nInvalid choice. Try again.") 

#------------------------------------------------------------------------------------------
#*fuel management* functions:
#1 - define monitor fuel levels page
def fuel_levels():
    while True:
        print("\nFuel Levels Monitor\n1. View Fuel Levels of Vehicle\n2. Back to Fuel Management Page")
        try: 
            view_choice = int(input("Enter your choice number: "))
            if view_choice == 1:
                driver_id = input("\nEnter the driver's ID to view its fuel level: ")
                try:
                    with open("driver_fuel_management.txt", "r") as file:  
                        lines = file.readlines() 

                        # Loop through all lines to check for the driver_id
                        found = False
                        for line in lines:
                            parts = [part.split(":") for part in line.strip().split(",")] 

                            if len(parts) == 11: 
                                UserID = parts[0][1].strip()
                                Vehicle_Type = parts[1][1].strip()
                                selected_hub = parts[2][1].strip()
                                fuel_levels = parts[3][1].strip()
                                last_refuel_date = parts[4][1].strip()
                                refuel_date = parts[5][1].strip()
                                refuel_time = parts[6][1].strip()
                                refuel_quantity = parts[7][1].strip()
                                refuel_cost = parts[8][1].strip()
                                mileage = parts[9][1].strip()
                                remaining_fuel = parts[10][1].strip()

                                if driver_id == UserID: 
                                    found = True 
                                    if fuel_levels == "high":
                                        print("\n--- Fuel Levels ---")
                                        print(f"Driver ID: {UserID}")
                                        print(f"Vehicle Type: {Vehicle_Type}")
                                        print(f"Current Location: {selected_hub}")
                                        print(f"Fuel Level: {fuel_levels}")
                                        print(f"Last Refuel Date: {last_refuel_date}")
                                        print(f"Mileage: {mileage} km")
                                        print(f"Remaining Fuel: {remaining_fuel} liters")
                                        print("-------------------\n")
                                    else:
                                        print("\n--- Fuel Levels ---")
                                        print(f"Driver ID: {UserID}")
                                        print(f"Vehicle Type: {Vehicle_Type}")
                                        print(f"Current Location: {selected_hub}")
                                        print(f"Fuel Level: {fuel_levels}")
                                        print(f"Last Refuel Date: {last_refuel_date}")
                                        print(f"Refuel Date: {refuel_date}")
                                        print(f"Refuel Time: {refuel_time}")
                                        print(f"Quantity: {refuel_quantity} liters")
                                        print(f"Cost: RM{refuel_cost}")
                                        print("-------------------\n")

                        if not found:
                            print(f"\nNo fuel levels found for Driver ID {driver_id}.")

                except FileNotFoundError:
                    print("\nFuel levels file not found.")
                except ValueError:
                    print("\nFile content is not in the expected format.")
            elif view_choice == 2:
                fuel_mgmt()
            else:
                print("\nInvalid choice. Please enter 1 or 2.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

#2 - define track consumption patterns page
def fuel_consumption():
    fuel_consumption_fp = "consumption_patterns.txt"
    while True:
        try: 
            view_choice = int(input("\nFuel Consumption Tracker\n1. View Fuel Consumptions of Vehicles\n2. Back to Fuel Management Page\nEnter your choice number: ").strip())
            if view_choice == 1:
                try:
                    with open(fuel_consumption_fp, "r") as file:
                        print("\n--- Fuel Consumption ---")
                        for line in file:
                            vehicle_id, current, last_week = line.strip().split(", ")
                            print(f"Vehicle {vehicle_id}: {current} km/l (Last week: {last_week} km/l)")
                        print("------------------------\n")
                except FileNotFoundError:
                    print("\nFuel consumption file not found.")
            elif view_choice == 2:
                fuel_mgmt()
            else:
                print("\nInvalid choice. Please enter 1 or 2.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

#3 - define view vehicle utilization page
def vehicle_utilization():
    vehicle_utilization_fp = "vehicle_utilization.txt"
    while True:
        try: 
            view_choice = int(input("\nVehicle Utilization Report\n1. View Weekly Utilization for All Vehicles\n2. View Weekly Utilization by Vehicle ID\n3. Back to Fuel Management Page\nEnter your choice number: "))
            if view_choice == 1:
                try:
                    #display all vehicles' utilization
                    with open(vehicle_utilization_fp, "r") as file:
                        print("\n--- Vehicle Utilization ---")
                        for line in file:
                            vehicle_id, distance = line.strip().split(", ")
                            print(f"Vehicle {vehicle_id}: {distance} km this week")
                        print("----------------------------\n")
                except FileNotFoundError:
                    print("\nVehicle utilization file not found.")
                except ValueError:
                    print("\nFile content is not in the expected format.")
            elif view_choice == 2:
                #display utilization for a specific vehicle ID
                try:
                    vehicle_id_input = input("Enter the Vehicle ID: ").strip()
                    found = False
                    with open(vehicle_utilization_fp, "r") as file:
                        for line in file:
                            vehicle_id, distance = line.strip().split(", ")
                            if vehicle_id == vehicle_id_input:
                                print(f"\n--- Vehicle Utilization ---")
                                print(f"Vehicle {vehicle_id}: {distance} km this week")
                                print("----------------------------\n")
                                found = True
                                break
                    if not found:
                        print(f"\nNo utilization report found for Vehicle ID: {vehicle_id_input}")
                except FileNotFoundError:
                    print("\nVehicle utilization file not found.")
                except ValueError:
                    print("\nFile content is not in the expected format.")
            elif view_choice == 3:
                fuel_mgmt()
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

#define *fuel management* main page
def fuel_mgmt():
    print("\n--- Fuel Management Page ---")
    fuel_menu_choice = int(input("1. Monitor Fuel Levels\n2. Track Consumption Patterns\n3. View Vehicle Utilization\n4. Back to Admin Dashboard\nEnter your choice number: "))
    
    #check fuel menu choice
    if fuel_menu_choice == 1:
        fuel_levels()
    elif fuel_menu_choice == 2:
        fuel_consumption()
    elif fuel_menu_choice == 3:
        vehicle_utilization()
    elif fuel_menu_choice == 4:
        admin_dashboard()
    else:
        print("\nInvalid choice. Try again.")

#------------------------------------------------------------------------------------------
#*driver management* functions:
#1 - helper function to read data from text files
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

#2 - define view shipment/vehicle/driver's current location page
def get_current_location(driver_id=None, shipment_id=None):
    print("\nCurrent Location Tracker")

    if driver_id:
        drivers = read_file("parcel_status.txt")
        for line in drivers:
            parts = [part.replace(" - ", ":").split(":") for part in line.strip().split(",") if " - " in part]
            
            if len(parts) == 6:
                # Extract values after splitting by colon
                Parcel_id, parcel_status, pick_up_time, arrival_time, Current_location, UserID = [part[1].strip() for part in parts]
                
                # Check if the driver_id matches
                if driver_id == UserID:
                    return f"Driver {driver_id} is at location ({Current_location})."
        
        return "Driver not found."

    if shipment_id:
        shipments = read_file("parcel_status.txt")
        for shipment in shipments:
            shipment_data = [part.replace(" - ", ":").split(":")[1].strip() for part in shipment.strip().split(",") if " - " in part]
            
            if len(shipment_data) >= 5:
                if shipment_data[0] == shipment_id:
                    return f"Shipment {shipment_id} is currently at location ({shipment_data[4]})."
        
        return "Shipment not found."

    return "Error: No valid identifier provided for vehicle, driver, or shipment."

#3 - define view driver availability page
def driver_availability(driver_id):
    print("Driver's Availability Status")
    # Check if the driver is available by checking ongoing assignments & display the driver's schedule
    drivers = read_file("driver_availability.txt")
    
    # Standardize formatting for comparison
    formatted_driver_id = driver_id.replace(" ", "").lower()
    
    for driver in drivers:
        driver_data = [part.split(":")[1].strip() for part in driver.strip().split(",")]
        current_driver_id = driver_data[0].replace(" ", "").lower()
        
        if current_driver_id == formatted_driver_id:
            availability_status = "Available" if driver_data[1].lower() == "available" else "Not Available"
            print(f"Driver {driver_id} is {availability_status}.\n")
            
            admin_drivers = read_file("admin_driver_info.txt")
            for admin_driver in admin_drivers:
                admin_driver_data = admin_driver.strip().split('|')
                admin_driver_id = admin_driver_data[0].replace(" ", "").lower()
                
                if admin_driver_id == formatted_driver_id:
                    print("Driver found in admin_driver_info.txt")

                    # Now display the driver's schedule in a table format
                    print(f"Driver {driver_id}'s Weekly Schedule:")
                    # Print headers
                    print(f"{'Day':<10}{'Dispatched':<20}{'Returned':<20}{'Route'}")
                    print("-" * 60)  # Separator line
                    
                    # Get the driver's schedule
                    for i in range(2, len(admin_driver_data), 3):
                        dispatched = admin_driver_data[i]
                        returned = admin_driver_data[i+1]
                        route = admin_driver_data[i+2]
                        day = f"Day {int((i-2)/3)+1}"  # Generate Day number
                        print(f"{day:<10}{dispatched:<20}{returned:<20}{route}")
                    
                    return availability_status  # End function after printing schedule

    return "Driver not found."

#4 - define view driver's ongoing assignment page
def get_ongoing_assignments(driver_id):
    print("Driver's Ongoing Assignment Tracker")
    #returns a list of ongoing assignments for the given driver ID
    shipments = read_file("parcel_status.txt")
    ongoing_assignments = []
    
    for shipment in shipments:
        # Ensure we are processing each line as a string
        shipment = shipment.strip()  # Strip any leading/trailing spaces from the line
        
        shipment_data = [part.split("-")[1].strip() for part in shipment.split(",")]
        if shipment_data[5] == driver_id:
            ongoing_assignments.append(shipment_data[0])
    
    if not ongoing_assignments:
        return "No ongoing assignments."
    
    return ongoing_assignments

#5 - define assign a shipment page
def assign_shipment(driver_id, shipment_id, origin, destination):
    shipments_file = "parcel_info.txt"
    #function to assign a shipment to a specific driver by driver ID.
    #check if the driver is available
    availability = driver_availability(driver_id)
    if "not available" in availability:
        return availability  #cannot assign if the driver is not available
    
    #assign shipment to the driver
    shipments = read_file(shipments_file)
    shipment_found = False
    
    for shipment in shipments:
        shipment_data = shipment.strip().split('|')
        if shipment_data[0] == shipment_id:
            shipment_found = True
            return f"Shipment {shipment_id} already exists and cannot be added again."
    
    new_shipment = f"{shipment_id}|{origin}|{destination}|{driver_id}\n"
    shipments.append(new_shipment)
    
    with open(shipments_file, 'w') as file:
        file.writelines(shipments)
    
        return f"New shipment {shipment_id} has been created and assigned to driver {driver_id}."

#define *driver management* main page
def driver_mgmt():
    print("\n--- Driver Management Page ---")
    driver_menu_choice = int(input("1. View Shipment/Driver's Current Location\n2. View Driver Availability\n3. View Driver's Ongoing Assignment\n4. Assign a Shipment to a Driver\n5. Back to Admin Dashboard\nEnter your choice number: "))
    
    #check driver menu choice
    if driver_menu_choice == 1:
        entity_choice = int(input("\nView current location of:\n1. Driver\n2. Shipment\nEnter your choice number: "))
        
        if entity_choice == 1:
            driver_id = input("Enter Driver ID: ")
            print(get_current_location(driver_id=driver_id))
        elif entity_choice == 2:
            shipment_id = input("Enter Shipment ID: ")
            print(get_current_location(shipment_id=shipment_id))
        else:
            print("Invalid choice.")
        driver_mgmt()

    elif driver_menu_choice == 2:
        driver_id = input("Enter Driver ID: ")
        print(driver_availability(driver_id))
        driver_mgmt()

    elif driver_menu_choice == 3:
        driver_id = input("Enter Driver ID: ")
        assignments = get_ongoing_assignments(driver_id)
        if isinstance(assignments, list):
            print(f"Ongoing Assignments for {driver_id}:")
            for assignment in assignments:
                print(f"- {assignment}")
        else:
            print(assignments)
        driver_mgmt()

    elif driver_menu_choice == 4:
        print("\nShipment's Driver Assignment")
        driver_id = input("Enter driver ID of assigned driver: ")
        shipment_id = input("Enter new shipment ID: ")
        origin = input("Enter shipment origin: ")
        destination = input("Enter shipment destination: ")
        print(assign_shipment(driver_id, shipment_id, origin, destination))
        driver_mgmt()

    elif driver_menu_choice == 5:
        admin_dashboard()

    else:
        print("\nInvalid choice. Try again.")

#------------------------------------------------------------------------------------------
#*reports* functions:
#1.1 - read key metrics data from txt
def read_data(file_path):
    file_path  = "metrics_data.txt"
    #reads data from the provided text file and returns a dictionary.
    with open(file_path, 'r') as file:
        data_lines = file.readlines()
    data = {}
    current_category = None
    for line in data_lines:
        line = line.strip()
        if line.endswith(":"):
            current_category = line[:-1]  #identify the current category.
            data[current_category] = {}
        elif "-" in line:
            key, value = line.replace("- ", "").split(": ")
            data[current_category][key.strip()] = float(value.strip())  #parse key-value pairs.
    return data

#1.2 - calculates the inventory turnover ratio
def calculate_inventory_turnover(cost_of_goods_sold, average_inventory):
    return cost_of_goods_sold / average_inventory

#1.3 - calculates the average truck turnaround time
def calculate_truck_turnaround_time(total_truck_time, number_of_trucks):
    return total_truck_time / number_of_trucks

#1.4 - calculates the average transportation cost per unit distance
def calculate_average_transportation_cost(total_transportation_cost, total_distance):
    return total_transportation_cost / total_distance

#1.5 - calculates the operating ratio
def calculate_operating_ratio(total_operating_expenses, total_revenue):
    return (total_operating_expenses / total_revenue) * 100

#1 - define key metrics report page
def key_metrics(data):
    inventory_turnover = calculate_inventory_turnover(
        data['inventory']['cost_of_goods_sold'], data['inventory']['average_inventory']
    )
    truck_turnaround = calculate_truck_turnaround_time(
        data['truck_turnaround']['total_truck_time'], data['truck_turnaround']['number_of_trucks']
    )
    avg_transportation_cost = calculate_average_transportation_cost(
        data['transportation_cost']['total_transportation_cost'], data['transportation_cost']['total_distance']
    )
    operating_ratio = calculate_operating_ratio(
        data['operating']['total_operating_expenses'], data['operating']['total_revenue']
    )
    print("--- Key Metrics Report ---")
    while True:
        try: 
            view_choice = int(input("\n1. View Inventory Turnover Ratio\n2. View Truck Turnaround Time\n3. Average Transportation Cost\n4. Operating Ratio\n5. View Summary Key Metrics Report\n6. Back to Reports Page\nEnter your choice number: "))
            if view_choice == 1:
                print(f"\nInventory Turnover Ratio: {inventory_turnover:.2f}") #display inventory turnover ratio 
            elif view_choice == 2:
                print(f"\nAverage Truck Turnaround Time: {truck_turnaround:.2f} hours") #display truck turnaround time
            elif view_choice == 3:
                print(f"\nAverage Transportation Cost: RM{avg_transportation_cost:.2f} per km") #display average transportation cost
            elif view_choice == 4:
                print(f"\nOperating Ratio: {operating_ratio:.2f}%") #display operating ratio
            elif view_choice == 5:
                print(f"\nSummary of Key Metrics Report\nInventory Turnover Ratio: {inventory_turnover:.2f}\nAverage Truck Turnaround Time: {truck_turnaround:.2f} hours\nAverage Transportation Cost: RM{avg_transportation_cost:.2f} per km\nOperating Ratio: {operating_ratio:.2f}%") #display all key metrics report
            elif view_choice == 6:
                reports()
            else:
                print("\nInvalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

#2.1 - reads trip logs from a txt file and returns them as a list of dictionaries
def read_trip_log(file_path):
    #ach dictionary contains details like route, timestamps, and additional information.
    #initialize an empty list to store trip logs
    trip_logs = []
    try:
        #open the file for reading
        with open(file_path, 'r') as file:
            #process each line in the file
            for line in file:
                #split the line into parts based on commas
                parts = line.strip().split(', ')
                #initialize a dictionary for each trip log entry
                trip_log = {}
                #for each part, split it by the delimiter ': ' and assign it to the dictionary
                for part in parts:
                    key, value = part.split(': ', 1)
                    trip_log[key.strip()] = value.strip()
                #add the trip log entry to the list
                trip_logs.append(trip_log)
    except FileNotFoundError:
        print(f"Error: File at {file_path} not found.")
    #return the list of trip logs
    return trip_logs

#2 - define trip logs report
def trip_logs(trip_logs):
    print("--- Trip Logs Report ---")
    #check if there are no trip logs to display
    if not trip_logs:
        print("No trip logs available.")
        return
    
    #display all trips and its details (route details, timestamps), data fetch from txt
    #print the header for the table
    print(f"{'Route':<30}{'Timestamp':<30}{'Driver':<50}")
    print("=" * 110)
    
    #iterate through the trip logs and print each log's details
    for log in trip_logs:
        #get route, timestamp, and details for each log entry
        route = log.get('Route', 'N/A')
        timestamp = log.get('Timestamp', 'N/A')
        driver = log.get('Driver', 'N/A')
        
        #print the trip log in a formatted way
        print(f"{route:<30}{timestamp:<30}{driver:<50}")

#define *reports* main page
def reports():
    print("\n--- Reports ---")
    reports_menu_choice = int(input("1. View Key Metrics Report\n2. View Trip Logs Report\n3. Back to Admin Dashboard\nEnter your choice number: "))

    #check reports menu choice
    if reports_menu_choice == 1:
        #read the data from the text file
        data = read_data("metrics_data.txt")
        #pass the data to key_metrics
        key_metrics(data)
    elif reports_menu_choice == 2:
        #read the trip logs from the text file
        trip_logs_data = read_trip_log("trip_logs.txt")
        #pass the trip logs data to trip_logs function
        trip_logs(trip_logs_data)
        reports()
    elif reports_menu_choice == 3:
        admin_dashboard()
    else:
        print("\nInvalid choice. Try again.")

def process_login():
    while True:
        Decision = login()
        if Decision == "1":
            registration()
        elif Decision == "2":
            UserID = input("Enter your user id: ").strip()
            Password = input("Enter your password: ").strip()

            # Validate user
            login_successful = False
            with open("users.txt", "r") as file:
                for line in file:
                    if line.strip():
                        fields = line.strip().split(", ")
                        
                        # Create a dictionary to store the user data
                        user_data = {}
                        for field in fields:
                            key, value = field.split(": ", 1)
                            user_data[key.strip()] = value.strip()

                        # Validate credentials
                        if (
                            UserID == user_data.get("User ID") and 
                            Password == user_data.get("Password")
                        ):
                            print("Login successful!")
                            login_successful = True
                            user_type = user_data.get("User Type", "").lower()
                            if user_type == "driver":
                                collect_driver_info(UserID)
                            elif user_type == "admin":
                                admin_dashboard()
                            else:
                                main_menu()
                            break
            
            if not login_successful:
                print("Invalid username or password")
        elif Decision == "3":
            break
        else:
            print("Invalid input, try again!")

if __name__ == "__main__":
   process_login()
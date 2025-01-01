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
                    file.write(f"{UserID},{User_Name},{Password},{User_Type}\n")
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

# Function to generate order ID with format "D@@"
def generate_order_id(file_path="parceldetails.txt"):
    try:
        with open(file_path, "r") as file:
            # Read every line 
            # line.strip() at the front: Cleans up the valid lines you're reading
            # if line.strip() at the back: Filters out completely empty or whitespace-only lines
            lines = [line.strip() for line in file if line.strip()]
            # Check if the file is not empty
            if lines:
                # Get the last line
                last_entry = lines[-1].strip()
                if last_entry and "," in last_entry:
                    # Get the first value in the array
                    last_order = last_entry.split(",")[0]
                    order_number = int(last_order) + 1
                else:
                    order_number = 1
            else:
                order_number = 1
    except FileNotFoundError:
        order_number = 1 

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
    # Get auto generated order id
    order_id = generate_order_id()
    with open("parceldetails.txt", "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            parts = [part.strip() for part in last_line.strip().split(",")]
            order_number, order_id, Vehicle_Type, Parcel_Weight, Pick_Up_State, Drop_Off_State, Round_Trip, Quantity_Of_Round_Trip, Vehicle_Price, Total_Price = parts
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
        file.write(f"{order_number},{order_id},{Vehicle_Type},{Parcel_Weight},{Pick_Up_State},{Drop_Off_State},{Round_Trip},{Quantity_Of_Round_Trip},{Vehicle_Price},{Total_Price}\n")
    
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
        file.write(f"{order_number},{order_id},{Vehicle_Type},{Parcel_Weight},{Pick_Up_State},{Drop_Off_State},{Round_Trip},{Quantity_Of_Round_Trip},{Vehicle_Price},{Total_Price}\n")
    
    payment(main_menu_callback)

# Function to get route price for van
def Van_Route(main_menu_callback, Vehicle_Type, Parcel_Weight, Pick_Up_State, Drop_Off_State, Vehicle_Price, order_id, order_number):
    # write a dictionary for the price of the round trip in tuple
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
        file.write(f"{order_number},{order_id},{Vehicle_Type},{Parcel_Weight},{Pick_Up_State},{Drop_Off_State},{Round_Trip},{Quantity_Of_Round_Trip},{Vehicle_Price},{Total_Price}\n")
    
    payment(main_menu_callback)
    
# Function to track order
# def track_order():
#     # Parse parcel details once
#     with open("parceldetails.txt", "r") as parcel_file:
#         parcel_ids = [line.split(',')[1].strip() for line in parcel_file]

#     # Parse package information into a dictionary
#     with open("package_info.txt", "r") as package_file:
#         package_data = {}
#         for line in package_file:
#             parts = line.strip().split(",")
#             if len(parts) == 6:
#                 parcel_id, pick_up_state, drop_off_state, parcel_status, pick_up_time, arrival_time = parts
#                 package_data[parcel_id] = {
#                     "pick_up_state": pick_up_state,
#                     "drop_off_state": drop_off_state,
#                     "status": parcel_status,
#                     "pick_up_time": pick_up_time,
#                     "arrival_time": arrival_time
#                 }

#     while True:
#         order_id = input("Enter your Order ID: ").strip()

#         # Validate order id
#         if order_id not in parcel_ids:
#             print("Pop Up: Invalid Order ID")
#             main_menu()

#         # Check if order_id exists in package_data
#         if order_id in package_data:
#             order = package_data[order_id]
#             if order["status"].lower() == "picked up":
#                 print(f"Picked Up Time: {order['Pick_up_time']}, Parcel Picked Up")
#             elif order["status"].lower() == "delivered":
#                 print(f"Arrival Time: {order['arrival_time']}, Parcel Delivered")
#             else:
#                 print(f"Current Status: {order['status']}, Parcel in Transit")
#         else:
#             print("Order ID exists in parcel details but no tracking information is available yet.")

#         # User decision
#         print("\nOptions:")
#         print("1. Track another order")
#         print("2. Back to main menu")
#         decision = input("Enter your choice (1/2): ").strip()

#         if decision != "1":
#             print("Exiting order tracking.")
#             main_menu()

def track_order():
    # Parse parcel details once
    with open("parcel_info.txt", "r") as parcel_file:
        parcel_ids = [line.split(',')[0].strip().lower() for line in parcel_file]

    # Parse package information into a dictionary
    package_data = {}
    with open("parcel_info.txt", "r") as package_file:
        for line in package_file:
            parts = [part.strip() for part in line.strip().split(",")]
            if len(parts) == 5:
                order_id, parcel_status, pick_up_time, arrival_time, current_location = parts
                package_data[order_id.lower()] = {
                    "parcel_id": order_id,
                    "parcel_status": parcel_status,
                    "pick_up_time": pick_up_time,
                    "arrival_time": arrival_time,
                    "current_location": current_location
                }
            else:
                print(f"Skipped invalid line in package_info.txt: {line}")

    while True:
        order_id = input("Enter your Order ID: ").strip().lower()

        # Validate order id
        if order_id not in parcel_ids:
            print("Pop Up: Invalid Order ID")
            main_menu()

        # Check if order_id exists in package_data
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

        # User decision
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

        Vehicle_Type = input("Select your vehicle type (1/2/3): ")
        Parcel_weight = input("Enter your parcel weight (kg): ")
        print("1. Johor \n2. Kuala Lumpur \n3. Butterworth \n4. Kedah \n5. Perlis \n6. Kelantan \n7. Terengganu")
        Pick_Up_State = input("Enter your desired pick up state: ")
        Drop_Off_State = input("Enter your desired drop off state: ")

        if Vehicle_Type == "1":
            Vehicle_Price = 5
            order_id, order_number = generate_order_id()
            Motor_Route(main_menu, Vehicle_Type, Parcel_weight, Pick_Up_State, Drop_Off_State, Vehicle_Price, order_id, order_number)
        elif Vehicle_Type == "2":
            Vehicle_Price = 8
            order_id, order_number = generate_order_id()
            Car_Route(main_menu, Vehicle_Type, Parcel_weight, Pick_Up_State, Drop_Off_State, Vehicle_Price, order_id, order_number)
        else:
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

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#============================ Driver ===============================
def current_hub():
    while True:
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

def parcel_status():
    Current_location = current_hub()  

    Parcel_id = input("Enter parcel ID: ").strip()
    updated_lines = []
    parcel_found = False  

    # with open("package_info.txt", "r") as file:
    with open("parceldetails.txt", "r") as file:
        for line in file:
            parts = [part.strip() for part in line.strip().split(",")]
            
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
                
                with open("parcel_info.txt", "a") as file:
                    file.write(f"{Parcel_id},{parcel_status},{pick_up_time},{arrival_time},{Current_location}\n")

            #     # Update the line with additional timestamps
            #     updated_line = f"{order_id},{pick_up_state},{drop_off_state},{parcel_status},{pick_up_time},{arrival_time}\n"
            # else:
            #     # Retain the original line for non-matching parcel IDs
            #     updated_line = f"{line.strip()},\n" if len(line.strip().split(",")) == 4 else line

            # updated_lines.append(updated_line)

    # Check if parcel ID was not found
    if not parcel_found:
        print("Invalid parcel ID, try again!")
        return

    # Write back the updated lines
    # with open("package_info.txt", "w") as file:
    #     file.writelines(updated_lines)

    print("Parcel status updated successfully.")

def maintenance_form():
    print("\n=================== Please fill up the maintenance claim form to the admin! ===================")
    # Vehicle_Plate = input("Enter your vehicle plate number: ")
    UserID = input("Enter your user ID: ")
    print("1. Proceed\n2. Exit")
    Decision = input("Enter your decision (1/2):")
    if Decision == "1":
        with open("driver_profile.txt","r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                parts = [part.strip() for part in last_line.strip().split(",")]
                stored_userID, stored_Contact_info, stored_Address, stored_Driving_license, stored_Vehicle_Type, stored_Vehicle_Plate, stored_Criminal_records, stored_Criminal_records_explanation= parts
                if UserID == stored_userID:
                    Service_Type = input("Enter your service type(engine/brake/aircon/others): ")
                    Repair_Cost = float(input("Enter your repair cost(RM): "))
                    Maintenance_Date = input("Enter your maintenance date(DD-MM-YYYY): ")

                    with open("maintenance_form.txt","a") as file:
                        file.write(f"{UserID},{stored_Vehicle_Plate},{stored_Vehicle_Type},{Service_Type},{Repair_Cost},{Maintenance_Date}\n")

                    print("\n===== Maintenance Claim Form =====")
                    print("Vehicle Plate: ", stored_Vehicle_Plate)
                    print("UserID: ", UserID)
                    print("Vehicle Type: ", stored_Vehicle_Type)
                    print("Service Type: ", Service_Type)
                    print("Repair Cost: ", Repair_Cost)
                    print("Maintenance Date: ", Maintenance_Date)
                    print("Your maintenance claim form has been submitted to the admin!")
                    print("Thank you! Have a good day!")  

                else:
                    print("Invalid user ID, try again!") 
    elif Decision == "2":
        driver_menu()
    else:
        print("Invalid input, try again!")

def vehicle_status():
    print("\n==============You are in vehicle status page.==============")
    while True:
        Update_vehicle = input("Enter your vehicle status (Good/Bad): ")
        if Update_vehicle.lower() == "good":
            print("No need to send for maintenance!")
            driver_menu()
        elif Update_vehicle.lower() == "bad": 
            print("Send for maintenance!")
            maintenance_form()
            driver_menu()
        else:
            print("Invalid input, try again!")

def Maintenance_monthly():
    print("\n=================== Welcome to the maintenance monthly check! ===================")
    UserID = input("Enter your user ID: ")
    print("1. Proceed\n2. Exit")
    Decision = input("Enter your decision (1/2):")
    if Decision == "1":
        with open("driver_profile.txt","r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                parts = [part.strip() for part in last_line.strip().split(",")]
                stored_userID, stored_Contact_info, stored_Address, stored_Driving_license, stored_Vehicle_Type, stored_Vehicle_Plate, stored_Criminal_records, stored_Criminal_records_explanation = parts
                if UserID == stored_userID:
                    Maintenance_Date = input("Enter your maintenance date(DD-MM-YYYY): ")
                    Maintenance_Result = input("Enter your maintenance result (Good/Bad): ")
                    if Maintenance_Result.lower() == "good":
                        print("No need to send for service!")
                    elif Maintenance_Result.lower() == "bad":
                        print("Send for service!")
                        maintenance_form()
                    else:
                        print("Invalid input, try again!")

                    print("\n========== Updated Maintenance Form ==========")
                    print("UserID: ", UserID)
                    print("Vehicle Plate: ", stored_Vehicle_Plate)
                    print("Vehicle Type: ", stored_Vehicle_Type)
                    print("Maintenance Date: ", Maintenance_Date)
                    print("Your maintenance has been updated!")
                    print("Thank you! Have a good day!")
                else:
                    print("Invalid user ID, try again!")
    elif Decision == "2":
        driver_menu()
    else:
        print("Invalid input, try again!")       

def fuel_management():
    print("\n=================== Welcome to fuel management page! ===================")
    UserID = input("Enter your user ID: ")
    print("1. Proceed\n2. Exit")
    Decision = input("Enter your decision (1/2):")
    if Decision == "1":
        Vehicle_Type = input("Enter your vehicle type (motor/car/van): ")
        selected_hub = current_hub()
        fuel_levels = input("Enter your current fuel levels (high/low): ")
        if fuel_levels.lower() == "low":
            print("\nSend to refuel!!!")
            refuel_date = input("Enter your date of refueling (DD-MM-YYYY):")
            refuel_time = input("Enter the time of refueling (HH:MM):")    
            refuel_quantity = input("Enter how many litres you refueled:")
            refuel_cost = input("Enter the refuel amount (RM):")
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
            file.write(f"{UserID},{Vehicle_Type},{selected_hub},{fuel_levels},{refuel_date},{refuel_time},{refuel_quantity},{refuel_cost},{mileage},{remaining_fuel}\n")
        driver_menu()
    elif Decision == "2":
        driver_menu()
    else:
        print("Invalid input, try again!")

def driver_availability():
    user_id = input("Enter your user ID: ").strip()
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
        driver_menu()

    with open("driver_availability.txt", "a") as file:
        file.write(f"{user_id},{availability_status},{Current_hub},{task_assigned}\n")
    driver_menu()

def driver_menu():
    print("\n=================== Welcome to driver page! How are you today? ===================")
    while True:
        print("1. Vehicle status")
        print("2. Maintenance monthly")
        print("3. Update parcel status")
        print("4. Fuel Management")
        print("5. Driver Availability")
        print("6. Exit")
        Decision = input("Which page you want do to go to? (1/2/3/4/5): ").strip().lower()

        if Decision == "1":
            vehicle_status()
        elif Decision == "2":
            Maintenance_monthly()
        elif Decision == "3":
            parcel_status()
        elif Decision == "4":
            fuel_management()
        elif Decision == "5":
            driver_availability()
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
                file.write(f"{UserID},{Contact_info},{Address},{Driving_license},{Vehicle_Type},{Vehicle_Plate},{Criminal_records},{Criminal_records_explanation}\n")
            print_driver_profile(UserID, Contact_info, Address, Driving_license, Vehicle_Type, Vehicle_Plate, Criminal_records_explanation)
            driver_menu()
        elif Decision == "2":
            Vehicle_Type = "Car"
            Vehicle_Plate = input("Enter your vehicle plate number: ")
            with open("driver_profile.txt", "a") as file:
                file.write(f"{UserID},{Contact_info},{Address},{Driving_license},{Vehicle_Type},{Vehicle_Plate},{Criminal_records},{Criminal_records_explanation}\n")
            print_driver_profile(UserID, Contact_info, Address, Driving_license, Vehicle_Type, Vehicle_Plate, Criminal_records_explanation)
            driver_menu()
        elif Decision == "3":
            Vehicle_Type = "Van"
            Vehicle_Plate = input("Enter your vehicle plate number: ")
            with open("driver_profile.txt", "a") as file:
                file.write(f"{UserID},{Contact_info},{Address},{Driving_license},{Vehicle_Type},{Vehicle_Plate},{Criminal_records},{Criminal_records_explanation}\n")
            print_driver_profile(UserID, Contact_info, Address, Driving_license, Vehicle_Type, Vehicle_Plate, Criminal_records_explanation)
            driver_menu()
        elif Decision == "exit":
            Vehicle_Type = "Nothing"
            Vehicle_Plate = "Nothing"
            with open("driver_profile.txt", "a") as file:
                file.write(f"{UserID},{Contact_info},{Address},{Driving_license},{Vehicle_Type},{Vehicle_Plate},{Criminal_records},{Criminal_records_explanation}\n")
            print("Exiting")
            process_login()
        else:
            print("Invalid input, try again!")

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
        driver_menu()
    else:
        print("Invalid input, try again!")

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
# Create package_info.txt for driver
with open("parceldetails.txt","r") as file:
    for line in file:
        parts = [part.strip() for part in line.strip().split(",")]
        if len(parts) == 10:
            order_number, order_id, Vehicle_Type, Parcel_Weight, Pick_Up_State, Drop_Off_State, Round_Trip, Quantity_Of_Round_Trip, Vehicle_Price, Total_Price = parts
            Parcel_status = "order sent"
            with open("package_info.txt","a") as file:
                file.write(f"{order_id},{Pick_Up_State},{Drop_Off_State},{Parcel_status}\n")

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
                    parts = [part.strip() for part in line.strip().split(",")]
                    if len(parts) == 4:  
                        stored_UserID, stored_User_Name, stored_Password, stored_User_Type = parts
                        if UserID == stored_UserID and Password == stored_Password:
                            print("Login successful!")
                            login_successful = True
                            if stored_User_Type.lower() == "driver":
                                collect_driver_info(UserID)
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
import os

# Create parceldetails.txt if it doesn't exist
if not os.path.exists("parceldetails.txt"):
    open("parceldetails.txt", "w").close()

# Function to process login
def login():
    print("\n===== WELCOME TO PAPAMOVE! =====")
    print("1. Create account")
    print("2. Login")
    print("3. Exit")    
    Decision = input("Enter your choice: ")
    return Decision

# Create new account
def registration():
    while True:
        print("\n===== CREATE NEW ACCOUNT =====")
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

# Function to process payment
def process_payment():
    print("Processing payment...")
    print("Payment successful!")
    print("Thank you for choosing our service!")
    print("Returning to main menu...")
    print()

# Function to generate order ID with format "D@@"
def generate_order_id(file_path="parceldetails.txt"):
    # Check if the file exist
    if os.path.exists(file_path): 
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
    else:
        order_number = 1 

    # Format order ID as DXX
    order_id = f"D{order_number:02}" 
    return order_id, order_number

# Function to print package info
def print_package_info(Vehicle_Type, Parcel_Weight, Total_Price, order_id):
    print("\n===== PACKAGE DETAILS =====")
    print(f"Order ID      : {order_id}")
    print(f"Vehicle Type  : {Vehicle_Type}")    
    print(f"Weight (kg)   : {Parcel_Weight}")
    print(f"Total Price   : RM{float(Total_Price):.2f}")
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
            order_number, order_id, Vehicle_Type, Parcel_Weight, Pick_Up_State, Drop_Off_State, Round_Trip, Vehicle_Price, Total_Price = parts
    print_package_info(Vehicle_Type, Parcel_Weight, Total_Price, order_id)

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
        file.write(f"{order_number},{order_id},{Vehicle_Type},{Parcel_Weight},{Pick_Up_State},{Drop_Off_State},{Round_Trip},{Vehicle_Price},{Total_Price}\n")
    
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
        file.write(f"{order_number},{order_id},{Vehicle_Type},{Parcel_Weight},{Pick_Up_State},{Drop_Off_State},{Round_Trip},{Vehicle_Price},{Total_Price}\n")
    
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
        file.write(f"{order_number},{order_id},{Vehicle_Type},{Parcel_Weight},{Pick_Up_State},{Drop_Off_State},{Round_Trip},{Vehicle_Price},{Total_Price}\n")
    
    payment(main_menu_callback)
    
# Function to track order
def track_order():
    while True:
        order_id = input("Enter your Order ID: ")

        # Validate order id
        try:
            with open("parceldetails.txt", "r") as parcel_file:
                 parcel_ids = [line.split(',')[1].strip() for line in parcel_file]
        except FileNotFoundError:
            print("Error: Parcel details file not found.")
            return

        if order_id not in parcel_ids:
            print("Pop Up: Invalid Order ID")
            main_menu()

        # Find parcel delivery details of the order id from...txt
        try:
            with open("driver_data.txt", "r") as driver_file:
                orders = {}
                for line in driver_file:
                    data = line.strip().split(",")
                    if len(data) == 4:
                        orders[data[0]] = {
                            "status": data[1],
                            "arrival_time": data[2],
                            "current_location": data[3]
                        }
        except FileNotFoundError:
            print("Error: Driver data file not found.")
            return

        # If order id found in...txt, check if the parcel has delivered
        if order_id in orders:
            order = orders[order_id]
            if order["status"] == "Delivered":
                print(f"Arrival Time: {order['arrival_time']}, Parcel Delivered")
            else:
                print(f"Current Location: {order['current_location']}, Parcel in Transit")
        else:
            print("Order ID exists in parcel details but no tracking information is available yet.")

        print("\nOptions:")
        print("1. Track another order")
        print("2. Back to main menu")
        decision = input("Enter your choice (1 or 2): ")

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

        Vehicle_Type = input("Select your vehicle type: ")
        Parcel_weight = input("Enter your parcel weight: ")
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
    else:
        print("Exiting...")

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
            try:
                with open("users.txt", "r") as file:
                    for line in file:
                        parts = [part.strip() for part in line.strip().split(",")]
                        if len(parts) == 4:  
                            stored_UserID, stored_User_Name, stored_Password, stored_User_Type = parts
                            if UserID == stored_UserID and Password == stored_Password:
                                print("Login successful!")
                                login_successful = True
                                main_menu()
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
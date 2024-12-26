import os

# Function to process payment
def process_payment():
    print("Processing payment...")
    print("Payment successful!")
    print("Thank you for choosing our service!")
    print("Returning to main menu...")
    print()

# Function to generate auto-incremented order ID with "D@@"
def generate_order_id(file_path="last_order.txt"):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            last_entry = file.read().strip()
            if last_entry and "," in last_entry:
                last_order = last_entry.split(",")[0]
                order_number = int(last_order) + 1
            else:
                order_number = 1
    else:
        order_number = 1

    order_id = f"D{order_number:02}"
    # Save the new order in the format `3,D03`
    with open(file_path, "w") as file:
        file.write(f"{order_number},{order_id}")
    return order_id

# Function to record order ID in parceldetails.txt
def record_order_id(order_id, file_path="parceldetails.txt"):
    with open(file_path, "a") as file:
        file.write(order_id + "\n")

# Function to print package info
def print_package_info(Vehicle_Type, Parcel_Weight, Total_Price, order_id):
    print("\n===== PACKAGE DETAILS =====")
    print(f"Order ID      : {order_id}")
    print(f"Vehicle Type  : {Vehicle_Type}")    
    print(f"Weight (kg)   : {Parcel_Weight}")
    print(f"Total Price   : RM{float(Total_Price):.2f}")
    print("===========================")

# Payment function
def payment(main_menu_callback):
    order_id = generate_order_id()
    with open("parceldetails.txt", "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            parts = [part.strip() for part in last_line.strip().split(",")]
            Vehicle_Type, Parcel_Weight, Pick_Up_State, Drop_Off_State, Round_Trip, Vehicle_Price, Total_Price, order_id = parts

    print_package_info(Vehicle_Type, Parcel_Weight, Total_Price, order_id)

    confirm = input("Do you want to proceed with payment? (yes/no): ").lower()
    if confirm == "yes":
        # Record the generated Order ID
        record_order_id(order_id)
        process_payment()
        main_menu_callback()
    else:
        print("Order canceled. Returning to main menu...")
        main_menu_callback()

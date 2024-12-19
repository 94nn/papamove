from Motor_Route import Route
from Car_Route import CarRoute  

def main_menu():
    print("1. Make Order")
    print("2. Track Order")
    print("3. Exit")
    
    Decision = input("Enter your decision: ")

    if Decision == "1":
        print("\n1. Motor\n2. Car\n3. Van\n")
        Vehicle_Type = input("Select your vehicle type: ")
        Parcel_weight = input("Enter your parcel weight: ")
        Pick_Up_State = input("Enter your desired pick up state: ")
        Drop_Off_State = input("Enter your desired drop off state: ")


        if Vehicle_Type == "1":
            Vehicle_Price = 5
            with open("parceldetails.txt", "a") as file:
                file.write(f"{Vehicle_Type},{Parcel_weight},{Pick_Up_State},{Drop_Off_State},0,{Vehicle_Price},0\n")
            Route(main_menu)
        elif Vehicle_Type == "2":
            Vehicle_Price = 8
            with open("parceldetails.txt", "a") as file:
                file.write(f"{Vehicle_Type},{Parcel_weight},{Pick_Up_State},{Drop_Off_State},0,{Vehicle_Price},0\n")
            CarRoute(main_menu)
        else:
            Vehicle_Price == 18
            with open("parceldetails.txt", "a") as file:
                file.write(f"{Vehicle_Type},{Parcel_weight},{Pick_Up_State},{Drop_Off_State},0,{Vehicle_Price},0\n")

    elif Decision == "2":
        print("Feature not implemented yet!")
    else:
        print("Exiting...")
    
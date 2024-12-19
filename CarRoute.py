from Payment import payment

def count_price(Price, Vehicle_Price, Quantity_Of_Round_Trip, Parcel_Weight):
    Sum_Of_Price = float((Price + Vehicle_Price) * Parcel_Weight)
    Round_Trip_Cost = float((Sum_Of_Price * 0.5) * Quantity_Of_Round_Trip)
    Total_Price = float(Sum_Of_Price + Round_Trip_Cost)
    return Total_Price

def Car_Route(main_menu_callback):
    with open("parceldetails.txt", "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            parts = [part.strip() for part in last_line.strip().split(",")]
            Vehicle_Type, Parcel_Weight, Pick_Up_State, Drop_Off_State, Round_Trip, Vehicle_Price, Total_Price = parts

    # Example logic to set Price
    if Pick_Up_State.lower() == "johor" and Drop_Off_State.lower() == "kuala lumpur":   
        Price = 0.10
    elif Pick_Up_State.lower() == "johor" and Drop_Off_State.lower() == "butterworth":
        Price = 0.20
    elif Pick_Up_State.lower() == "johor" and Drop_Off_State.lower() == "kedah":
        Price = 0.22
    elif Pick_Up_State.lower() == "johor" and Drop_Off_State.lower() == "perlis":
        Price = 0.24
    elif Pick_Up_State.lower() == "johor" and Drop_Off_State.lower() == "terengganu":
        Price = 0.20   
    elif Pick_Up_State.lower() == "johor" and Drop_Off_State.lower() == "kelantan":
        Price = 0.20
    elif Pick_Up_State.lower() == "kuala lumpur" and Drop_Off_State.lower() == "johor":
        Price = 0.10
    elif Pick_Up_State.lower() == "kuala lumpur" and Drop_Off_State.lower() == "butterworth":
        Price = 0.10
    elif Pick_Up_State.lower() == "kuala lumpur" and Drop_Off_State.lower() == "kedah":
        Price = 0.12
    elif Pick_Up_State.lower() == "kuala lumpur" and Drop_Off_State.lower() == "perlis":
        Price = 0.14
    elif Pick_Up_State.lower() == "kuala lumpur" and Drop_Off_State.lower() == "terengganu":
        Price = 0.10
    elif Pick_Up_State.lower() == "kuala lumpur" and Drop_Off_State.lower() == "kelantan":
        Price = 0.10
    elif Pick_Up_State.lower() == "butterworth" and Drop_Off_State.lower() == "johor":
        Price = 0.20
    elif Pick_Up_State.lower() == "butterworth" and Drop_Off_State.lower() == "kuala lumpur":
        Price = 0.10
    elif Pick_Up_State.lower() == "butterworth" and Drop_Off_State.lower() == "kedah":
        Price = 0.02
    elif Pick_Up_State.lower() == "butterworth" and Drop_Off_State.lower() == "perlis":
        Price = 0.04
    elif Pick_Up_State.lower() == "kedah" and Drop_Off_State.lower() == "johor":
        Price = 0.22
    elif Pick_Up_State.lower() == "kedah" and Drop_Off_State.lower() == "kuala lumpur":
        Price = 0.12
    elif Pick_Up_State.lower() == "kedah" and Drop_Off_State.lower() == "butterworth":
        Price = 0.02    
    elif Pick_Up_State.lower() == "kedah" and Drop_Off_State.lower() == "perlis":
        Price = 0.02
    elif Pick_Up_State.lower() == "perlis" and Drop_Off_State.lower() == "johor":
        Price = 0.24
    elif Pick_Up_State.lower() == "perlis" and Drop_Off_State.lower() == "kuala lumpur":
        Price = 0.14
    elif Pick_Up_State.lower() == "perlis" and Drop_Off_State.lower() == "butterworth":
        Price = 0.04
    elif Pick_Up_State.lower() == "perlis" and Drop_Off_State.lower() == "kedah":
        Price = 0.02
    elif Pick_Up_State.lower() == "terengganu" and Drop_Off_State.lower() == "johor":
        Price = 0.20
    elif Pick_Up_State.lower() == "terengganu" and Drop_Off_State.lower() == "kuala lumpur":
        Price = 0.10
    elif Pick_Up_State.lower() == "terengganu" and Drop_Off_State.lower() == "kelantan":
        Price = 0.00
    elif Pick_Up_State.lower() == "kelantan" and Drop_Off_State.lower() == "johor":
        Price = 0.20
    elif Pick_Up_State.lower() == "kelantan" and Drop_Off_State.lower() == "kuala lumpur":
        Price = 0.10
    elif Pick_Up_State.lower() == "kelantan" and Drop_Off_State.lower() == "terengganu":
        Price = 0.00
    Round_Trip = input("Do you want a round trip? (Yes/No)")
    if Round_Trip.lower() == "yes":
        Quantity_Of_Round_Trip = int(input("Enter the quantity of round trip: "))
        Total_Price = count_price(Price, float(Vehicle_Price), Quantity_Of_Round_Trip, float(Parcel_Weight))
    else:
        Quantity_Of_Round_Trip = 0
        Total_Price = count_price(Price, float(Vehicle_Price), Quantity_Of_Round_Trip, float(Parcel_Weight))

    with open("parceldetails.txt", "a") as file:
        file.write(f"{Vehicle_Type},{Parcel_Weight},{Pick_Up_State},{Drop_Off_State},{Round_Trip},{Vehicle_Price},{Total_Price}\n")
    
    payment(main_menu_callback)
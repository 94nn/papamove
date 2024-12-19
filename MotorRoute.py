with open("parceldetails.txt", "r") as file:
    for line in file:
        # Strip whitespace and split by comma
        parts = [part.strip() for part in line.strip().split(",")]
        Vehicle_Type, Parcel_Weight, Pick_Up_State, Drop_Off_State, Round_Trip, Vehicle_Price = parts



stored_Vehicle_Type = Vehicle_Type
stored_Parcel_Weight = Parcel_Weight
stored_Pick_Up_State = Pick_Up_State
stored_Drop_Off_State = Drop_Off_State
stored_Round_Trip = Round_Trip
stored_Vehicle_Price = Vehicle_Price


with open("parceldetails.txt", "a") as file:
    file.write(f"{stored_Vehicle_Type},{stored_Parcel_Weight},{stored_Pick_Up_State},{stored_Drop_Off_State},{stored_Round_Trip},{stored_Vehicle_Price},0\n")
# Read the parceldetails.txt file
with open("parceldetails.txt", "r") as file:
    lines = file.readlines()
    if lines:  # Check if file is not empty
        last_line = lines[-1]  # Get the last line
        parts = [part.strip() for part in last_line.strip().split(",")]
        stored_Vehicle_Type, stored_Parcel_Weight, stored_Pick_Up_State, stored_Drop_Off_State, stored_Round_Trip, stored_Vehicle_Price = parts

def Route():    
    if stored_Pick_Up_State.lower() == "kelantan" or stored_Drop_Off_State.lower() == "terengganu":
        Route = 2
        if stored_Pick_Up_State.lower() == "johor":
            if stored_Drop_Off_State.lower() == "kuala lumpur":
                Price = 0.15
            elif stored_Drop_Off_State.lower() == "kelantan":
                Price = 0.30
            elif stored_Drop_Off_State.lower() == "terengganu":
                Price = 0.30
        elif stored_Pick_Up_State.lower() == "kuala lumpur":
            if stored_Drop_Off_State.lower() == "johor":
                Price = 0.15
            elif stored_Drop_Off_State.lower() == "kelantan":
             Price = 0.15
        elif stored_Drop_Off_State.lower() == "terengganu":
            Price = 0.15
        elif stored_Pick_Up_State.lower() == "kelantan":
            if stored_Drop_Off_State.lower() == "kuala lumpur":
                Price = 0.15
            elif stored_Drop_Off_State.lower() == "johor":
                Price = 0.30
            elif stored_Drop_Off_State.lower() == "terengganu":
                Price = 0.00
        else:
            if stored_Drop_Off_State.lower() == "johor":
                Price = 0.30
            elif stored_Drop_Off_State.lower() == "kuala lumpur":
                Price = 0.15
            elif stored_Drop_Off_State.lower() == "kelantan":
                Price = 0.00
        Quantity_Of_Round_Trip = input("Enter the quantity of round trip: ")
        count_price(Price, float(stored_Vehicle_Price), int(Quantity_Of_Round_Trip))

    else:
        Route = 1
        if stored_Pick_Up_State.lower() == "johor":
            if stored_Drop_Off_State.lower() == "kuala lumpur":
                Price = 0.15
            elif stored_Drop_Off_State.lower() == "butterworth":
                Price = 0.30
            elif stored_Drop_Off_State.lower() == "kedah":
                Price = 0.33
            elif stored_Drop_Off_State.lower() == "perlis":
                Price = 0.40
        elif stored_Pick_Up_State.lower() == "kuala lumpur":
            if stored_Drop_Off_State.lower() == "johor":
                Price = 0.15
            elif stored_Drop_Off_State.lower() == "butterworth":
                Price = 0.15
            elif stored_Drop_Off_State.lower() == "kedah":
                Price = 0.18
            elif stored_Drop_Off_State.lower() == "perlis":
                Price = 0.25
        elif stored_Pick_Up_State.lower() == "butterworth":
            if stored_Drop_Off_State.lower() == "johor":
                Price = 0.30
            elif stored_Drop_Off_State.lower() == "kuala lumpur":
                Price = 0.15
            elif stored_Drop_Off_State.lower() == "kedah":
                Price = 0.03
            elif stored_Drop_Off_State.lower() == "perlis":
                Price = 0.10
        elif stored_Pick_Up_State.lower() == "kedah":
            if stored_Drop_Off_State.lower() == "johor":
                Price = 0.33
            elif stored_Drop_Off_State.lower() == "kuala lumpur":
                Price = 0.18
            elif stored_Drop_Off_State.lower() == "butterworth":
                Price = 0.03
            elif stored_Drop_Off_State.lower() == "perlis":
                Price = 0.07
        else:
            if stored_Drop_Off_State.lower() == "johor":
                Price = 0.40
            elif stored_Drop_Off_State.lower() == "kuala lumpur":
                Price = 0.25
            elif stored_Drop_Off_State.lower() == "butterworth":
                Price = 0.10
            elif stored_Drop_Off_State.lower() == "kedah":
                Price = 0.07
        Quantity_Of_Round_Trip = 0
        count_price(Price, float(stored_Vehicle_Price), int(Quantity_Of_Round_Trip))

def count_price(Price, stored_Vehicle_Price, Quantity_Of_Round_Trip):
    if stored_Round_Trip.lower() == "yes":
        Sum_Of_Price = (Price + stored_Vehicle_Price) * Quantity_Of_Round_Trip
        Round_Trip_Cost = (Sum_Of_Price * 0.5) * Quantity_Of_Round_Trip
        Total_Price = Sum_Of_Price + Round_Trip_Cost
        return Total_Price
from Payment import payment

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

def count_price(Price, Vehicle_Price, Quantity_Of_Round_Trip, Parcel_Weight):
    Sum_Of_Price = float((Price + Vehicle_Price) * Parcel_Weight)
    Round_Trip_Cost = float((Sum_Of_Price * 0.5) * Quantity_Of_Round_Trip)
    Total_Price = float(Sum_Of_Price + Round_Trip_Cost) 
    return Total_Price

def CarRoute(main_menu_callback):
    with open("parceldetails.txt", "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1]
            parts = [part.strip() for part in last_line.strip().split(",")]
            Vehicle_Type, Parcel_Weight, Pick_Up_State, Drop_Off_State, Round_Trip, Vehicle_Price, Total_Price, order_id = parts

    # Use dictionary lookup instead of if-else chain
    route_key = (Pick_Up_State.lower(), Drop_Off_State.lower())
    Price = round_trip_price.get(route_key, 0.00)  # Returns 0.00 if route not found

    Round_Trip = input("Do you want a round trip? (Yes/No)")
    if Round_Trip.lower() == "yes":
        Quantity_Of_Round_Trip = int(input("Enter the quantity of round trip: "))
        Total_Price = count_price(Price, float(Vehicle_Price), Quantity_Of_Round_Trip, float(Parcel_Weight))
    else:
        Quantity_Of_Round_Trip = 0
        Total_Price = count_price(Price, float(Vehicle_Price), Quantity_Of_Round_Trip, float(Parcel_Weight))

    with open("parceldetails.txt", "a") as file:
        file.write(f"{Vehicle_Type},{Parcel_Weight},{Pick_Up_State},{Drop_Off_State},{Round_Trip},{Vehicle_Price},{Total_Price},0\n")
    
    payment(main_menu_callback)
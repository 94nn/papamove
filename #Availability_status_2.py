#Availability_status_2
from datetime import datetime
def current_hub():
    while True:
        print("1 Johor")
        print("2 Kuala Lumpur")
        print("3 Butterworth")
        print("4 Kedah")
        print("5 Perlis")
        print("6 Kelantan")
        print("7 Terengganu")
        Decision = input("Select your drop off address (1/2/3/4/5/6/7) (or type exit to exit): ").strip().lower()

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
            exit()
        else:
            print("Invalid input, try again!")

selected_hub = current_hub()

if selected_hub == "Johor":
    parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
    if parcel_status.lower() == "delivered":
        print("Your parcel is currently in ", selected_hub)
        print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
    else:
        print("You are currently in", selected_hub)
elif selected_hub == "Kuala Lumpur":
    parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
    if parcel_status.lower() == "delivered":
        print("Your parcel is currently in ", selected_hub)
        print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
    else:
        print("You are currently in", selected_hub)
elif selected_hub == "Butterworth":
    parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
    if parcel_status.lower() == "delivered":
        print("Your parcel is currently in ", selected_hub)
        print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
    else:
        print("You are currently in", selected_hub)
elif selected_hub == "Kedah":
    parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
    if parcel_status.lower() == "delivered":
        print("Your parcel is currently in ", selected_hub)
        print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
    else:
        print("You are currently in", selected_hub)
elif selected_hub == "Perlis":
    parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
    if parcel_status.lower() == "delivered":
        print("Your parcel is currently in ", selected_hub)
        print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
    else:
        print("You are currently in", selected_hub)
elif selected_hub == "Kelantan":
    parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
    if parcel_status.lower() == "delivered":
        print("Your parcel is currently in ", selected_hub)
        print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
    else:
        print("You are currently in", selected_hub)
elif selected_hub == "Terengganu":
    parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
    if parcel_status.lower() == "delivered":
        print("Your parcel is currently in ", selected_hub)
        print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
    else:
        print("You are currently in", selected_hub)
elif selected_hub == "exit":
    print("Exiting")
    exit()
else:
    print("Invalid input, try again!")


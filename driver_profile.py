#Driver
from datetime import datetime

# def vehicle_type():
#     while True:
#         print("1 Motor")
#         print("2 Car")
#         print("3 Van")
#         Decision = input("Select your vehicle (1/2/3) (or type exit to return to main menu): ").strip().lower()

#         if Decision == "1":
#             return("Motor")
#         elif Decision == "2":
#             return("Car")
#         elif Decision == "3":
#             return("Van")
#         elif Decision == "exit":
#             print("Exiting")
#             menu()
#         else:
#             print("Invalid input, try again!")


# def collect_driver_info():
#     Contact_info = input("Enter your contact number: ").strip()
#     Address = input("Enter your address: ").strip()
#     Driving_license = input("Enter your driving license number: ").strip()
#     Criminal_records = input("Any criminal records? (Yes/No): ").strip().lower()
#     if Criminal_records == "yes":
#         print("Explain your criminal records: ")
#         Criminal_records_explanation = input("Enter your criminal records explanation: ").strip()
#         print("Your criminal records explanation has been submitted to the admin!")
#     else:
#         Criminal_records = "No"
#         Criminal_records_explanation = "No criminal records! Such a good driver!"
#     print("")
#     print("Driver's Profile")
#     print("Contact Information: ", Contact_info)
#     print("Address: ", Address)
#     print("Driving License: ", Driving_license)
#     print("Your criminal records explanation: ", Criminal_records_explanation)
#     print()
#     with open("driver_profile.txt", "a") as file:
#         file.write(f"{Contact_info},{Address},{Driving_license},{Criminal_records},{Criminal_records_explanation}\n")
#         # file.write(f"{Address}\n")
#         # file.write(f"{Driving_license}\n")
#         # file.write(f"{Criminal_records}\n")
#         # file.write(f"{Criminal_records_explanation}\n")
#     return Contact_info, Address, Driving_license, Criminal_records, Criminal_records_explanation


# def maintenance_form():
#     print("Please fill up the maintenance claim form to the admin!")
#     Vehicle_Type_Selected = vehicle_type()
#     Vehicle_Plate = input("Enter your vehicle plate number: ")
#     UserID = input("Enter your user ID: ")
#     Service_Type = input("Enter your service type(engine/brake/aircon/others): ")
#     Repair_Cost = float(input("Enter your repair cost(RM): "))
#     Maintenance_Date = input("Enter your maintenance date(DD-MM-YYYY): ")
#     print("")
#     print("MAINTENANCE CLAIM FORM")
#     print("Vehicle Plate: ", Vehicle_Plate)
#     print("UserID: ", UserID)
#     print("Vehicle Type: ", Vehicle_Type_Selected)
#     print("Service Type: ", Service_Type)
#     print("Repair Cost: ", Repair_Cost)
#     print("Maintenance Date: ", Maintenance_Date)
#     print("Your maintenance claim form has been submitted to the admin!")
#     print("Thank you! Have a good day!")   
#     return Vehicle_Plate, UserID, Vehicle_Type_Selected, Service_Type, Repair_Cost, Maintenance_Date

# def vehicle_status():
#     print("You are in vehicle status page.")
#     while True:
#         Update_vehicle = input("Enter your vehicle status (Good/Bad): ")
#         if Update_vehicle.lower() == "good":
#             print("No need to send for maintenance!")
#             menu()
#         else: 
#             print("Send for maintenance!")
#             maintenance_form()
#             menu()
               
# def Maintenance_monthly():
#     print("Welcome to the maintenance monthly check!")
#     Maintenance_Result = input("Enter your maintenance result (Good/Bad): ")
#     if Maintenance_Result.lower() == "good":
#         Vehicle_Type_Selected = vehicle_type()
#         print("No need to send for maintenance!")
#         Vehicle_Plate = input("Enter your vehicle plate number: ")
#         UserID = input("Enter your user ID: ")
#         Maintenance_Date = input("Enter your maintenance date(DD-MM-YYYY): ")
#     else:
#         print("Send for maintenance!")
#         maintenance_form()

#     print("")
#     print("Update Maintenance Form")
#     print("Vehicle Plate: ", Vehicle_Plate)
#     print("UserID: ", UserID)
#     print("Vehicle Type: ", Vehicle_Type_Selected)
#     print("Maintenance Date: ", Maintenance_Date)
#     print("Your maintenance has been updated!")
#     print("Thank you! Have a good day!")

# def fuel_management():
#     print("Welcome to fuel management page! ")
#     Vehicle_Type_Selected = vehicle_type()
#     selected_hub = current_hub()
#     fuel_levels = input("Enter your current fuel levels (high/low): ")
#     if fuel_levels.lower() == "low":
#         print("Send to refuel!")
#         refuel_date = input("Enter your date of refueling (DD-MM-YYYY):")
#         refuel_time = input("Enter the time of refueling (HH:MM):")    
#         refuel_quantity = input("Enter how many litres you refueled:")
#         refuel_cost = input("Enter the refuel amount (RM):")
#         print("")
#         print("Your refuel date of the vehicle:", refuel_date)
#         print("Your refuel time is at:", refuel_time)
#         print("Your refuel quantity at:", refuel_quantity , "litres")
#         print("Your refuel cost at:RM", refuel_cost)
#         print("Your fuel status has been send to admin! Thank you!")
#         print("Have a great journey ahead!") 
#     else: 
#         mileage = input("Enter your mileage(km): ")
#         remaining_fuel = input("Enter your remaining fuel levels: ")
#         print("Your current mileage is at: ", mileage, "km")
#         print("Your current fuel levels is at :", remaining_fuel, "litres")
#         print("Your fuel status has been send to admin! Thank you!")
#         print("Have a great journey ahead!")  

def current_hub():
    while True:
        print("1 Johor")
        print("2 Kuala Lumpur")
        print("3 Butterworth")
        print("4 Kedah")
        print("5 Perlis")
        print("6 Kelantan")
        print("7 Terengganu")
        print("Waiting for task!")
        Decision = input("Select your drop off address (1/2/3/4/5/6/7/8) (or type exit to exit): ").strip().lower()

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
        elif Decision == "8":
            return("Waiting for task!")
        elif Decision == "exit":
            print("Exiting")
            exit()
        else:
            print("Invalid input, try again!")

# def parcel_hub():
#     selected_hub = current_hub()
#     if selected_hub == "Johor":
#         parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
#         if parcel_status.lower() == "delivered":
#             print("Your parcel is currently in ", selected_hub)
#             print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
#         else:
#             print("You are currently in", selected_hub)
#     elif selected_hub == "Kuala Lumpur":
#         parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
#         if parcel_status.lower() == "delivered":
#             print("Your parcel is currently in ", selected_hub)
#             print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
#         else:
#             print("You are currently in", selected_hub)
#     elif selected_hub == "Butterworth":
#         parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
#         if parcel_status.lower() == "delivered":
#             print("Your parcel is currently in ", selected_hub)
#             print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
#         else:
#             print("You are currently in", selected_hub)
#     elif selected_hub == "Kedah":
#         parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
#         if parcel_status.lower() == "delivered":
#             print("Your parcel is currently in ", selected_hub)
#             print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
#         else:
#             print("You are currently in", selected_hub)
#     elif selected_hub == "Perlis":
#         parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
#         if parcel_status.lower() == "delivered":
#             print("Your parcel is currently in ", selected_hub)
#             print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
#         else:
#             print("You are currently in", selected_hub)
#     elif selected_hub == "Kelantan":
#         parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
#         if parcel_status.lower() == "delivered":
#             print("Your parcel is currently in ", selected_hub)
#             print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
#         else:
#             print("You are currently in", selected_hub)
#     elif selected_hub == "Terengganu":
#         parcel_status = input("Enter your parcel status (Delivered/Not Delivered): ").strip().lower()
#         if parcel_status.lower() == "delivered":
#             print("Your parcel is currently in ", selected_hub)
#             print("Arrival time: ", (datetime.now()).strftime("%H:%M"))
#         else:
#             print("You are currently in", selected_hub)
#     elif selected_hub == "exit":
#         print("Exiting")
#         exit()
#     else:
#         print("Invalid input, try again!")
#     with open("availability_status_2.txt", "a") as file:
#         file.write(f"{selected_hub}, {parcel_status}, {datetime.now().strftime('%H:%M')}\n")

# def menu():
#     print("Welcome to driver page! How are you today?")
#     while True:
#         print("1 Vehicle status")
#         print("2 Maintenance monthly")
#         print("3 Availability status")
#         print("4 Fuel Management")
#         print("5 Exit")
#         Decision = input("Which page you want do to go to? (1/2/3/4/5): ").strip().lower()

#         if Decision == "1":
#             vehicle_status()
#         elif Decision == "2":
#             Maintenance_monthly()
#         elif Decision == "3":
#             return("haha")
#         elif Decision == "4":
#             fuel_management()
#         elif Decision == "5":
#             print("Exiting")
#             exit()
#         else:
#             print("Invalid input, try again!")

if __name__ == "__main__":
    driver_profile = collect_driver_info
    menu()
    Vehicle_Type_Selected = vehicle_type
    with open ("driver_profile.txt","a") as file:        
        file.write(f"{Vehicle_Type_Selected}\n")
    

    
   




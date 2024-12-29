#define real admin credentials
real_admin_username = "hilda"
real_admin_password = "happy123"

#define admin main dashboard
def admin_dashboard():
    print("\n--- Welcome to the Admin Dashboard ---")
    while True:
        print("Options:\n1. Vehicle Management\n2. Fuel Management\n3. Driver Management\n4. Log Out")
        admin_menu_option = int(input("Enter option: "))
        
        #check admin menu option
        if admin_menu_option == 1:
            vehicle_mgmt()
        elif admin_menu_option == 2:
            fuel_mgmt()
        elif admin_menu_option == 3:
            driver_mgmt()
        elif admin_menu_option == 4:   
            print("\nLogged Out!")
        else:
            print("Invalid option. Try again.")
        break

#------------------------------------------------------------------------------------------
#*vehicle management* functions:
#1 - define view vehicle performance history page
def vehicle_performance():
    vehicle_id = int(input("\nEnter the vehicle ID to view its performance history: "))
    print("Vehicle Performance of Vehicle ", vehicle_id)
    performance_status = "vehicle_status" #get from driver
    if performance_status == "Good":
        print("Vehicle Status: Good")
    else:
        view_choice = input("Vehicle Status: Under Maintenance\nView Maintenance History? Yes/No: ")
        if view_choice == "Yes":
            vehicle_maintenance() #go to function #2 
        elif view_choice == "No":
            vehicle_mgmt() #back to vehicle management main page
        else:
            admin_dashboard()
   
#2.1 - read vehicle maintenance history txt file
import ast
def read_maintenance_history(file_path, vehicle_id):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  #read all lines from the file

        #filter records based on vehicle_id
        print(f"Maintenance history for Vehicle ID: {vehicle_id}")
        found = False
        for line in lines:
            try:
                record = ast.literal_eval(line.strip())
            except (SyntaxError, ValueError):
                print(f"Skipping invalid record: {line.strip()}")
                continue
        
            if isinstance(record, dict) and 'vehicle_id' in record:
                if record['vehicle_id'] == vehicle_id:
                    found = True
                    print(f"  Maintenance ID: {record.get('maintenance_id', 'N/A')}")
                    print(f"  Date: {record.get('maintenance_date', 'N/A')}")
                    print(f"  Service: {record.get('maintenance_service', 'N/A')}")
                    print(f"  Cost: ${record.get('maintenance_cost', 'N/A')}")
                    print()

        if not found:
            print(f"No maintenance history found for Vehicle ID {vehicle_id}.")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")

#2 - define view vehicle maintenance history page
def vehicle_maintenance():
    vehicle_id = int(input("\nEnter the vehicle ID to view its maintenance history: "))
    file_path = 'C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/maintenance_history.txt'
    read_maintenance_history(file_path, vehicle_id)

    view_choice = int(input("\nChoose one to proceed:\n1. View other vehicle's maintenance history\n2. Back to Vehicle Management Main Page\n3. Back to Admin Dashboard\nEnter your choice number: "))
    if view_choice == 1:
        vehicle_maintenance()
    elif view_choice == 2:
        vehicle_mgmt()
    else:
        admin_dashboard()

#3.1 - save vehicles inspection to txt file
import json
def save_vehicles_to_txt(vehicles, file_path):
    #save the vehicles dictionary to txt file
    with open(file_path, 'w') as file:
        for vehicle_id, data in vehicles.items():
            vehicle_dict = {
                "vehicle_id": [vehicle_id],  #wrap the ID in a list
                "maintenance_alerts": data["maintenance_alerts"],
                "inspection_schedule": data["inspection_schedule"],
            }
            #write the dictionary as a string to the file
            file.write(f"{vehicle_dict}\n")

#3.2 - read vehicles inspection data in txt file
import ast
def load_vehicles_from_txt(file_path):
    vehicles = {}
    #load the vehicles dictionary from txt file
    try:
        with open(file_path, 'r') as file:
            for line in file:
                #convert the line from a string to a dictionary
                try:
                    vehicle_data = ast.literal_eval(line.strip())  #safely parse the dictionary string
                    
                    #extract the vehicle ID and other fields
                    vehicle_id = vehicle_data['vehicle_id'][0]  #get the first element of the list
                    alerts = vehicle_data.get('maintenance_alerts', [])
                    schedules = vehicle_data.get('inspection_schedule', [])
                    
                    #save the data into the vehicles dictionary
                    vehicles[vehicle_id] = {
                        "maintenance_alerts": alerts,
                        "inspection_schedule": schedules
                    }
                except (SyntaxError, ValueError):
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print("File not found.")
    return vehicles

#3.3 - plan inspection for a vehicle
def plan_inspection(vehicles, vehicle_id, inspection_date, alert_message):
    if vehicle_id in vehicles:
        vehicles[vehicle_id]["maintenance_alerts"].append(alert_message)
        vehicles[vehicle_id]["inspection_schedule"].append(inspection_date)
        print(f"Inspection planned for vehicle {vehicle_id} on {inspection_date} with alert: '{alert_message}'.")
    else:
        print(f"Vehicle {vehicle_id} not found.")

#3.4 - view vehicle inspection schedule
def get_vehicle_data(vehicles, vehicle_id):
    try:
        #convert vehicle_id to an integer to match the dictionary key type
        vehicle_id = int(vehicle_id)
        if vehicle_id in vehicles:
            return {
                "Maintenance Alerts": vehicles[vehicle_id]["maintenance_alerts"],
                "Inspection Schedule": vehicles[vehicle_id]["inspection_schedule"]
            }
        else:
            print(f"Vehicle {vehicle_id} not found.")
            return None
    except ValueError:
        #handle cases where input cannot be converted to an integer
        print("Invalid vehicle ID. Please enter a numeric ID.")
        return None
    
#3 - define plan vehicle inspections, get vehicle maintenance alerts and schedules page
def vehicle_inspections():
    file_path = 'C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/vehicles.txt'
    vehicles = load_vehicles_from_txt(file_path)
    
    while True:
        print("\n--- Vehicle Inspection Planner ---")
        print("1. Plan an inspection for a vehicle")
        print("2. View vehicle inspection schedule")
        print("3. Save inspection plan and exit")

        choice = int(input("Enter your choice number: "))

        if choice == 1:
            #plan an inspection
            vehicle_id = int(input("Enter the vehicle ID to plan inspection for: ").strip())
            inspection_date = input("Enter the inspection date (YYYY-MM-DD): ").strip()
            alert_message = input("Enter the maintenance alert message: ").strip()
            plan_inspection(vehicles, vehicle_id, inspection_date, alert_message)
        elif choice == 2:
            #view vehicle schedule
            vehicle_id = int(input("Enter the vehicle ID to view its inspection schedule: ").strip())
            data = get_vehicle_data(vehicles, vehicle_id)
            if data:
                print(f"\nInspection Schedule for Vehicle {vehicle_id}:")
                print("Maintenance Alerts:")
                if data["Maintenance Alerts"]:
                    for alert in data["Maintenance Alerts"]:
                        if alert:  #check to avoid printing empty alerts
                            print(f"- {alert}")
                else:
                    print("No maintenance alerts found.")

                print("\nInspection Dates:")
                if data["Inspection Schedule"]:
                    for date in data["Inspection Schedule"]:
                        if date:  #check to avoid printing empty dates
                            print(f"- {date}")
                else:
                    print("No inspection dates found.")
        elif choice == 3:
            #save plan to file and exit
            save_vehicles_to_txt(vehicles, file_path)
            print("Data saved. Exiting...")
            vehicle_mgmt()
        else:
            print("Invalid choice. Please try again.")

#define *vehicle management* main page
def vehicle_mgmt():
    print("\n--- Vehicle Management Page ---")
    print("Options: \n1. View Performance History\n2. View Maintenance History\n3. Plan Inspections, View Maintenance Alerts & Schedules\n4. Back to Admin Dashboard")
    vehicle_menu_option = int(input("Enter option number: "))
    
    #check vehicle menu option
    if vehicle_menu_option == 1:
        vehicle_performance()
    elif vehicle_menu_option == 2:
        vehicle_maintenance()
    elif vehicle_menu_option == 3:
        vehicle_inspections()
    elif vehicle_menu_option == 4:
        admin_dashboard()
    else:
        print("Invalid option. Try again.") 

#------------------------------------------------------------------------------------------
#*fuel management* functions:
#1 - define

#define *fuel management* main page
def fuel_mgmt():
    print("\n--- Fuel Management Page ---")
    print("Options: \n1. View Performance History\n2. View Maintenance History\n3. Plan Inspections, View Maintenance Alerts & Schedules")
    fuel_menu_option = int(input("Enter option number: "))
    
    #check fuel menu option
    if fuel_menu_option == 1:
        vehicle_performance()
    elif fuel_menu_option == 2:
        vehicle_maintenance()
    elif fuel_menu_option == 3:
        vehicle_inspections()
    else:
        print("Invalid option. Try again.")

#------------------------------------------------------------------------------------------
#*driver management* functions:
#1 - define

#define *driver management* main page
def driver_mgmt():
    print("\n--- Driver Management Page ---")

#define admin's main navigation
def main():
    while True:
        #prompt for admin's credentials
        print("\nEnter admin's username and password:")
        admin_username = input("Username: ")
        admin_password = input("Password: ")
        
        #check input credentials
        if admin_username == real_admin_username and admin_password == real_admin_password:
            admin_dashboard()
        else:
            print("\nIncorrect username or password! Enter admin's username and password again.")

if __name__ == "__main__":
    main()

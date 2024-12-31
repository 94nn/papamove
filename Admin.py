#define real admin credentials
real_admin_username = "hilda"
real_admin_password = "happy123"

#define admin main dashboard
def admin_dashboard():
    print("\n--- Welcome to the Admin Dashboard ---")
    while True:
        admin_menu_choice = int(input("1. Vehicle Management\n2. Fuel Management\n3. Driver Management\n4. Reports\n5. Log Out\nEnter your choice number: "))
        
        #check admin menu option
        if admin_menu_choice == 1:
            vehicle_mgmt()
        elif admin_menu_choice == 2:
            fuel_mgmt()
        elif admin_menu_choice == 3:
            driver_mgmt()
        elif admin_menu_choice == 4:
            reports()
        elif admin_menu_choice == 5:   
            print("\nLogged Out!")
        else:
            print("\nInvalid choice. Try again.")
            admin_dashboard()

#------------------------------------------------------------------------------------------
#*vehicle management* functions:
#1 - define view vehicle performance history page
def vehicle_performance():
    vehicle_id = int(input("\nEnter the vehicle ID to view its performance history: "))
    print(f"\nVehicle Performance of Vehicle {vehicle_id}")
    performance_status = None #placeholder for the vehicle status 
    vehicle_performance_fp = "C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/vehicle_performance.txt"
    while True: 
        try:
            with open(vehicle_performance_fp, "r") as file: #!txt file path get from driver
                for line in file:
                    #read each line and check if the vehicle_id matches
                    current_id, status = line.strip().split(", ")
                    if int(current_id) == vehicle_id:
                        performance_status = status
                        break
            if performance_status:
                if performance_status == "Good":
                    print("Vehicle Status: Good")
                    view_choice = int(input("\nChoose one to proceed:\n1. View other vehicle's performance history\n2. Back to Vehicle Management Main Page\n3. Back to Admin Dashboard\nEnter your choice number: "))
                    if view_choice == 1:
                        vehicle_performance()
                    elif view_choice == 2:
                        vehicle_mgmt()
                    elif view_choice == 3:
                        admin_dashboard()
                    else:
                        print("\nInvalid choice. Returning to Vehicle Management.")
                        vehicle_mgmt()
                else:
                    view_choice = input("Vehicle Status: Under Maintenance\nView Maintenance History? Yes/No: ")
                    if view_choice.lower() == "yes":
                        vehicle_maintenance() #go to function #2
                    elif view_choice.lower() == "no":
                        view_choice = int(input("\nChoose one to proceed:\n1. View other vehicle's performance history\n2. Back to Vehicle Management Main Page\n3. Back to Admin Dashboard\nEnter your choice number: "))
                        if view_choice == 1:
                            vehicle_performance()
                        elif view_choice == 2:
                            vehicle_mgmt()
                        elif view_choice == 3:
                            admin_dashboard()
                        else:
                            print("\nInvalid choice. Returning to Vehicle Management.")
                            vehicle_mgmt() 
                    else:
                        print("\nInvalid choice. Returning to Vehicle Management.")
                        vehicle_mgmt()
            else:
                print(f"\nNo performance data found for Vehicle ID {vehicle_id}.")
                vehicle_performance()
        except FileNotFoundError:
            print("\nPerformance data file not found.")
        except ValueError:
            print("\nThe data in the file is not in the expected format.")

#2.1 - read vehicle maintenance history txt file
import ast
def read_maintenance_history(file_path, vehicle_id):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  #read all lines from the file

        #filter records based on vehicle_id
        print(f"\nMaintenance history for Vehicle ID: {vehicle_id}")
        found = False
        for line in lines:
            try:
                record = ast.literal_eval(line.strip())
            except (SyntaxError, ValueError):
                print(f"\nSkipping invalid record: {line.strip()}")
                continue
        
            if isinstance(record, dict) and 'vehicle_id' in record:
                if record['vehicle_id'] == vehicle_id:
                    found = True
                    print(f"Maintenance ID: {record.get('maintenance_id', 'N/A')}")
                    print(f"Date: {record.get('maintenance_date', 'N/A')}")
                    print(f"Service: {record.get('maintenance_service', 'N/A')}")
                    print(f"Cost: ${record.get('maintenance_cost', 'N/A')}")
                    print()

        if not found:
            print(f"\nNo maintenance history found for Vehicle ID {vehicle_id}.")

    except FileNotFoundError:
        print(f"\nError: File not found at {file_path}.")

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
    elif view_choice == 3:
        admin_dashboard()
    else:
        print("\nInvalid choice. Returning to Vehicle Management.")
        vehicle_mgmt()

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
                    print(f"\nSkipping invalid line: {line}")
    except FileNotFoundError:
        print("\nFile not found.")
    return vehicles

#3.3 - plan inspection for a vehicle
def plan_inspection(vehicles, vehicle_id, inspection_date, alert_message):
    if vehicle_id in vehicles:
        vehicles[vehicle_id]["maintenance_alerts"].append(alert_message)
        vehicles[vehicle_id]["inspection_schedule"].append(inspection_date)
        print(f"\nInspection planned for vehicle {vehicle_id} on {inspection_date} with alert: '{alert_message}'.")
    else:
        print(f"\nVehicle {vehicle_id} not found.")

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
            print(f"\nVehicle {vehicle_id} not found.")
            return None
    except ValueError:
        #handle cases where input cannot be converted to an integer
        print("\nInvalid vehicle ID. Please enter a numeric ID.")
        return None
    
#3 - define plan vehicle inspections, get vehicle maintenance alerts and schedules page
def vehicle_inspections():
    file_path = 'C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/vehicles.txt'
    vehicles = load_vehicles_from_txt(file_path)
    
    while True:
        choice = int(input("\n--- Vehicle Inspection Planner ---\n1. Plan an inspection for a vehicle\n2. View vehicle inspection schedule\n3. Save inspection plan and exit\nEnter your choice number: "))

        if choice == 1:
            #plan an inspection
            vehicle_id = int(input("\nEnter the vehicle ID to plan inspection for: ").strip())
            inspection_date = input("Enter the inspection date (YYYY-MM-DD): ").strip()
            alert_message = input("Enter the maintenance alert message: ").strip()
            plan_inspection(vehicles, vehicle_id, inspection_date, alert_message)
        elif choice == 2:
            #view vehicle schedule
            vehicle_id = int(input("\nEnter the vehicle ID to view its inspection schedule: ").strip())
            data = get_vehicle_data(vehicles, vehicle_id)
            if data:
                print(f"\nInspection Schedule for Vehicle {vehicle_id}:")
                print("\nMaintenance Alerts:")
                if data["Maintenance Alerts"]:
                    for alert in data["Maintenance Alerts"]:
                        if alert:  #check to avoid printing empty alerts
                            print(f"- {alert}")
                else:
                    print("\nNo maintenance alerts found.")

                print("\nInspection Dates:")
                if data["Inspection Schedule"]:
                    for date in data["Inspection Schedule"]:
                        if date:  #check to avoid printing empty dates
                            print(f"- {date}")
                else:
                    print("\nNo inspection dates found.")
        elif choice == 3:
            #save inspection plan to file and exit
            save_vehicles_to_txt(vehicles, file_path)
            print("\nData saved. Exiting...")
            vehicle_mgmt()
        else:
            print("\nInvalid choice. Please try again.")

#define *vehicle management* main page
def vehicle_mgmt():
    print("\n--- Vehicle Management Page ---")
    vehicle_menu_choice = int(input("1. View Performance History\n2. View Maintenance History\n3. Plan Inspections, View Maintenance Alerts & Schedules\n4. Back to Admin Dashboard\nEnter your choice number: "))
    
    #check vehicle menu choice
    if vehicle_menu_choice == 1:
        vehicle_performance()
    elif vehicle_menu_choice == 2:
        vehicle_maintenance()
    elif vehicle_menu_choice == 3:
        vehicle_inspections()
    elif vehicle_menu_choice == 4:
        admin_dashboard()
    else:
        print("\nInvalid option. Try again.") 

#------------------------------------------------------------------------------------------
#*fuel management* functions:
#1 - define monitor fuel levels page
def fuel_levels():
    fuel_levels_fp = "C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/fuel_levels.txt"
    while True:
        print("\nFuel Levels Monitor\n1. View Fuel Levels of Vehicle\n2. Back to Fuel Management Page")
        try: 
            view_choice = int(input("Enter your choice number: "))
            if view_choice == 1:
                try:
                    with open(fuel_levels_fp, "r") as file: #!txt file path get from driver
                        data = file.readline().strip()  #read the first line and remove any extra whitespace
                        date, time, quantity, cost = data.split(", ") #parsing the comma-separated values
                        print("\n--- Fuel Levels ---") #displaying the details
                        print(f"Date: {date}")
                        print(f"Time: {time}")
                        print(f"Quantity: {quantity} liters")
                        print(f"Cost: RM{cost}")
                        print("-------------------\n")
                except FileNotFoundError:
                    print("\nFuel levels file not found.")
                except ValueError:
                    print("\nFile content is not in the expected format.")
            elif view_choice == 2:
                fuel_mgmt()
            else:
                print("\nInvalid choice. Please enter 1 or 2.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

#2 - define track consumption patterns page
def fuel_consumption():
    fuel_consumption_fp = "C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/consumption_patterns.txt"
    while True:
        try: 
            view_choice = int(input("\nFuel Consumption Tracker\n1. View Fuel Consumptions of Vehicles\n2. Back to Fuel Management Page\nEnter your choice number: "))
            if view_choice == 1:
                try:
                    with open(fuel_consumption_fp, "r") as file: #read the fuel consumption text file
                        print("\n--- Fuel Consumption ---")
                        for line in file:
                            vehicle_id, current, last_week = line.strip().split(", ")  #parse the data for each vehicle
                            print(f"Vehicle {vehicle_id}: {current} km/l (Last week: {last_week} km/l)")
                        print("------------------------\n")
                except FileNotFoundError:
                    print("\nFuel consumption file not found.")
                except ValueError:
                    print("\nFile content is not in the expected format.")
            elif view_choice == 2:
                fuel_mgmt()
            else:
                print("\nInvalid choice. Please enter 1 or 2.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

#3 - define view vehicle utilization page
def vehicle_utilization():
    vehicle_utilization_fp = "C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/vehicle_utilization.txt"
    while True:
        try: 
            view_choice = int(input("\nVehicle Utilization Report\n1. View Weekly Utilization for All Vehicles\n2. View Weekly Utilization by Vehicle ID\n3. Back to Fuel Management Page\nEnter your choice number: "))
            if view_choice == 1:
                try:
                    #display all vehicles' utilization
                    with open(vehicle_utilization_fp, "r") as file:
                        print("\n--- Vehicle Utilization ---")
                        for line in file:
                            vehicle_id, distance = line.strip().split(", ")
                            print(f"Vehicle {vehicle_id}: {distance} km this week")
                        print("----------------------------\n")
                except FileNotFoundError:
                    print("\nVehicle utilization file not found.")
                except ValueError:
                    print("\nFile content is not in the expected format.")
            elif view_choice == 2:
                #display utilization for a specific vehicle ID
                try:
                    vehicle_id_input = input("Enter the Vehicle ID: ").strip()
                    found = False
                    with open(vehicle_utilization_fp, "r") as file:
                        for line in file:
                            vehicle_id, distance = line.strip().split(", ")
                            if vehicle_id == vehicle_id_input:
                                print(f"\n--- Vehicle Utilization ---")
                                print(f"Vehicle {vehicle_id}: {distance} km this week")
                                print("----------------------------\n")
                                found = True
                                break
                    if not found:
                        print(f"\nNo utilization report found for Vehicle ID: {vehicle_id_input}")
                except FileNotFoundError:
                    print("\nVehicle utilization file not found.")
                except ValueError:
                    print("\nFile content is not in the expected format.")
            elif view_choice == 3:
                fuel_mgmt()
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

#define *fuel management* main page
def fuel_mgmt():
    print("\n--- Fuel Management Page ---")
    fuel_menu_choice = int(input("1. Monitor Fuel Levels\n2. Track Consumption Patterns\n3. View Vehicle Utilization\n4. Back to Admin Dashboard\nEnter your choice number: "))
    
    #check fuel menu choice
    if fuel_menu_choice == 1:
        fuel_levels()
    elif fuel_menu_choice == 2:
        fuel_consumption()
    elif fuel_menu_choice == 3:
        vehicle_utilization()
    elif fuel_menu_choice == 4:
        admin_dashboard()
    else:
        print("\nInvalid option. Try again.")

#------------------------------------------------------------------------------------------
#*driver management* functions:
#1 - define view shipment/vehicle/driver's current location page
def current_location():
    print("Driver's Current Location Tracker")

#2 - define view driver availability page
def driver_availability():
    print("Driver's Availability Status")

#3 - define view driver's ongoing assignment page
def ongoing_assignment():
    print("Driver's Ongoing Assignment Tracker")

#define *driver management* main page
def driver_mgmt():
    print("\n--- Driver Management Page ---")
    driver_menu_choice = int(input("1. View Shipment/Vehicle/Driver's Current Location\n2. View Driver Availability\n3. View Driver's Ongoing Assignment\n4. Back to Admin Dashboard\nEnter your choice number: "))
    
    #check driver menu choice
    if driver_menu_choice == 1:
        current_location()
    elif driver_menu_choice == 2:
        driver_availability()
    elif driver_menu_choice == 3:
        ongoing_assignment()
    elif driver_menu_choice == 4:
        admin_dashboard()
    else:
        print("\nInvalid option. Try again.")

#------------------------------------------------------------------------------------------
#*reports* functions:
#1 - define key metrics report page
def key_metrics():
    inventory_turnover_fp = ""
    truck_turnaround_fp = ""
    avg_cost_fp = ""
    operating_ratio_fp = ""
    print("--- Key Metrics Report ---")
    while True:
        try: 
            view_choice = int(input("\n1. View Inventory Turnover Ratio\n2. View Truck Turnaround Time\n3. Average Transportation Cost\n4. Operating Ratio\n5. Back to Reports Page\nEnter your choice number: "))
            if view_choice == 1:
                try:
                    #display inventory turnover ratio
                    with open(inventory_turnover_fp, "r") as file:
                        print("\n--- Vehicle Utilization ---")
                        for line in file:
                            vehicle_id, distance = line.strip().split(", ")
                            print(f"Vehicle {vehicle_id}: {distance} km this week")
                        print("----------------------------\n")
                except FileNotFoundError:
                    print("\nVehicle utilization file not found.")
                except ValueError:
                    print("\nFile content is not in the expected format.")
            elif view_choice == 2:
                try:
                    #display truck turnaround time
                    vehicle_id_input = input("Enter the Vehicle ID: ").strip()
                    found = False
                    with open(truck_turnaround_fp, "r") as file:
                        for line in file:
                            vehicle_id, distance = line.strip().split(", ")
                            if vehicle_id == vehicle_id_input:
                                print(f"\n--- Vehicle Utilization ---")
                                print(f"Vehicle {vehicle_id}: {distance} km this week")
                                print("----------------------------\n")
                                found = True
                                break
                    if not found:
                        print(f"\nNo utilization report found for Vehicle ID: {vehicle_id_input}")
                except FileNotFoundError:
                    print("\nVehicle utilization file not found.")
                except ValueError:
                    print("\nFile content is not in the expected format.")
            elif view_choice == 3:
                try:
                    #display average transportation cost
                    with open(avg_cost_fp, "r") as file:
                        print("\n--- Vehicle Utilization ---")
                        for line in file:
                            vehicle_id, distance = line.strip().split(", ")
                            print(f"Vehicle {vehicle_id}: {distance} km this week")
                        print("----------------------------\n")
                except FileNotFoundError:
                    print("\nVehicle utilization file not found.")
                except ValueError:
                    print("\nFile content is not in the expected format.")
            elif view_choice == 4:
                try:
                    #display operating ratio
                    with open(operating_ratio_fp, "r") as file:
                        print("\n--- Vehicle Utilization ---")
                        for line in file:
                            vehicle_id, distance = line.strip().split(", ")
                            print(f"Vehicle {vehicle_id}: {distance} km this week")
                        print("----------------------------\n")
                except FileNotFoundError:
                    print("\nVehicle utilization file not found.")
                except ValueError:
                    print("\nFile content is not in the expected format.")
            elif view_choice == 5:
                reports()
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

#2 - define trip logs report
def trip_logs():
    print("--- Trip Logs Report ---")
    #display all trips and its details (route details, timestamps), data fetch from txt


#define *reports* main page
def reports():
    print("\n--- Reports ---")
    reports_menu_choice = int(input("1. View Key Metrics Report\n2. View Trip Logs Report\n3. Back to Admin Dashboard\nEnter your choice number: "))
    
    #check reports menu choice
    if reports_menu_choice == 1:
        key_metrics()
    elif reports_menu_choice == 2:
        trip_logs()
    elif reports_menu_choice == 3:
        admin_dashboard()
    else:
        print("\nInvalid option. Try again.")

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

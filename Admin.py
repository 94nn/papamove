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
            main()
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
def read_maintenance_history(file_path, vehicle_id):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  #read all lines from the file

        #filter records based on vehicle_id
        print(f"\nMaintenance history for Vehicle ID: {vehicle_id}")
        found = False
        for line in lines[1:]: #start from the second line
            try:
                #split the line into fields
                fields = line.strip().split(",")
                record = {
                    'vehicle_id': int(fields[0]),
                    'maintenance_id': int(fields[1]),
                    'maintenance_date': fields[2],
                    'maintenance_service': fields[3],
                    'maintenance_cost': float(fields[4]),
                }

                #check if the record matches the given vehicle_id
                if record['vehicle_id'] == vehicle_id:
                    found = True
                    print(f"Maintenance ID: {record.get('maintenance_id', 'N/A')}")
                    print(f"Date: {record.get('maintenance_date', 'N/A')}")
                    print(f"Service: {record.get('maintenance_service', 'N/A')}")
                    print(f"Cost: RM{record.get('maintenance_cost', 'N/A')}")
                    print()
            except (IndexError, ValueError) as e:
                print(f"\nSkipping invalid record: {line.strip()} (Error: {e})")

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
def save_vehicles_to_txt(vehicles, file_path):
    #save the vehicles dictionary to a text file
    with open(file_path, 'w') as file:
        for vehicle_id, data in vehicles.items():
            #construct the vehicle_dict string representation
            vehicle_dict = (
                f"{{'vehicle_id': [{vehicle_id}], "
                f"'maintenance_alerts': {data['maintenance_alerts']}, "
                f"'inspection_schedule': {data['inspection_schedule']}}}"
            )
            file.write(f"{vehicle_dict}\n")

#3.2 - read vehicles inspection data in txt file
def load_vehicles_from_txt(file_path):
    vehicles = {}
    #Load the vehicles dictionary from txt file
    try:
        with open(file_path, 'r') as file:
            for line in file:
                #parse the line as a dictionary string manually
                try:
                    #removing surrounding spaces and handling the dictionary format manually
                    line = line.strip().replace("'", '"')  #replace single quotes with double quotes for valid dict format
                    if line.startswith('{') and line.endswith('}'):
                        vehicle_data = eval(line)  #evaluate the dictionary string

                        #extract the vehicle ID and other fields
                        vehicle_id = vehicle_data['vehicle_id'][0]  #get the first element of the list
                        alerts = vehicle_data.get('maintenance_alerts', [])
                        schedules = vehicle_data.get('inspection_schedule', [])

                        #save the data into the vehicles dictionary
                        vehicles[vehicle_id] = {
                            "maintenance_alerts": alerts,
                            "inspection_schedule": schedules
                        }
                    else:
                        print(f"\nSkipping invalid line: {line}")
                except (SyntaxError, ValueError, NameError):
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
        print("\nInvalid choice. Try again.") 

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
            view_choice = int(input("\nFuel Consumption Tracker\n1. View Fuel Consumptions of Vehicles\n2. Back to Fuel Management Page\nEnter your choice number: ").strip())
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
        print("\nInvalid choice. Try again.")

#------------------------------------------------------------------------------------------
#*driver management* functions:
#1 - helper function to read data from text files
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

#2 - define view shipment/vehicle/driver's current location page
def get_current_location(vehicle_id=None, driver_id=None, shipment_id=None):
    print("\nCurrent Location Tracker")
    #returns the current location of the vehicle, driver, or shipment
    #either vehicle_id, driver_id, or shipment_id must be provided
    if vehicle_id:
        #!txt file path get from driver
        vehicles = read_file("C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/admin_vehicles_info.txt")
        for vehicle in vehicles:
            vehicle_data = vehicle.strip().split('|')
            if vehicle_data[0] == vehicle_id:
                return f"Vehicle {vehicle_id} is at location ({vehicle_data[1]}, {vehicle_data[2]})"
        return "Vehicle not found."
    
    if driver_id:
        #!txt file path get from driver
        drivers = read_file("C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/admin_drivers_info.txt")
        for driver in drivers:
            driver_data = driver.strip().split('|')
            if driver_data[0] == driver_id:
                return f"Driver {driver_id} is at location (Unknown, Unknown). Status: {driver_data[1]}"
        return "Driver not found."
    
    if shipment_id:
        #!txt file path get from user parceldetails.txt
        shipments = read_file("C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/parceldetails.txt")
        for shipment in shipments:
            shipment_data = shipment.strip().split(', ')
            shipment_dict = {item.split(': ')[0].strip(): item.split(': ')[1].strip() for item in shipment_data}
            if shipment_dict["Order ID"] == shipment_id:
                return f"Shipment {shipment_id} is at location ({shipment_dict['Pick Up State']}, {shipment_dict['Drop Off State']})"
        return "Shipment not found."

    return "Error: No valid identifier provided for vehicle, driver, or shipment."

#3 - define view driver availability page
def driver_availability(driver_id):
    print("Driver's Availability Status")
    #check if the driver is available by checking ongoing assignments & display the driver's schedule
    #!txt file path get from driver
    drivers = read_file("C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/admin_drivers_info.txt")
    for driver in drivers:
        driver_data = driver.strip().split('|')
        if driver_data[0] == driver_id:
            availability_status = "Available" if driver_data[1] == "Available" else "Not Available"
            print(f"Driver {driver_id} is {availability_status}.\n")
            
            #now display the driver's schedule in a table format
            print(f"Driver {driver_id}'s Weekly Schedule:")
            
            #print headers
            print(f"{'Day':<10}{'Dispatched':<20}{'Returned':<20}{'Route'}")
            print("-" * 60)  #separator line
            
            #get the driver's schedule
            for i in range(2, len(driver_data), 4):
                dispatched = driver_data[i]
                returned = driver_data[i+1]
                route = driver_data[i+2]
                day = f"Day {int((i-2)/4)+1}"  #generate Day number
                print(f"{day:<10}{dispatched:<20}{returned:<20}{route}")
            
            return  availability_status #end function after printing schedule
    return "Driver not found."

#4 - define view driver's ongoing assignment page
def get_ongoing_assignments(driver_id):
    print("Driver's Ongoing Assignment Tracker")
    #returns a list of ongoing assignments for the given driver ID
    #!txt file path get from user parceldetails.txt
    shipments = read_file("C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/parceldetails.txt")
    ongoing_assignments = []
    
    for shipment in shipments:
        shipment_data = shipment.strip().split(', ')
        shipment_dict = {item.split(': ')[0].strip(): item.split(': ')[1].strip() for item in shipment_data}
        if shipment_dict["Order ID"] == driver_id:
            ongoing_assignments.append(shipment_dict["Order Number"])
    
    if not ongoing_assignments:
        return "No ongoing assignments."
    
    return ongoing_assignments

#5 - define assign a shipment page
def assign_shipment(driver_id, shipment_id, origin, destination, vehicle_type, parcel_weight, round_trip, quantity_of_round_trip, vehicle_price, total_price):
    shipments_file = "C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/parceldetails.txt"
    
    #assign shipment to the driver
    shipments = read_file(shipments_file)
    for shipment in shipments:
        shipment_data = shipment.strip().split(', ')
        shipment_dict = {item.split(': ')[0].strip(): item.split(': ')[1].strip() for item in shipment_data}
        if shipment_dict["Order ID"] == shipment_id:
            return f"Shipment {shipment_id} already exists and cannot be added again."
    
    new_shipment = (
        f"Order Number: {len(shipments) + 1}, Order ID: {shipment_id}, Vehicle Type: {vehicle_type}, "
        f"Parcel Weight: {parcel_weight}, Pick Up State: {origin}, Drop Off State: {destination}, "
        f"Round Trip: {round_trip}, Quantity Of Round Trip: {quantity_of_round_trip}, "
        f"Vehicle Price: {vehicle_price}, Total Price: {total_price}\n"
    )
    shipments.append(new_shipment)
    
    with open(shipments_file, 'w') as file:
        file.writelines(shipments)
    
    return f"New shipment {shipment_id} has been created and assigned to driver {driver_id}."

#define *driver management* main page
def driver_mgmt():
    print("\n--- Driver Management Page ---")
    driver_menu_choice = int(input("1. View Shipment/Vehicle/Driver's Current Location\n2. View Driver Availability\n3. View Driver's Ongoing Assignment\n4. Assign a Shipment to a Driver\n5. Back to Admin Dashboard\nEnter your choice number: "))
    
    #check driver menu choice
    if driver_menu_choice == 1:
        entity_choice = int(input("\nView current location of:\n1. Vehicle\n2. Driver\n3. Shipment\nEnter your choice number: "))
        
        if entity_choice == 1:
            vehicle_id = input("Enter Vehicle ID: ")
            print(get_current_location(vehicle_id=vehicle_id))
        elif entity_choice == 2:
            driver_id = input("Enter Driver ID: ")
            print(get_current_location(driver_id=driver_id))
        elif entity_choice == 3:
            shipment_id = input("Enter Shipment ID: ")
            print(get_current_location(shipment_id=shipment_id))
        else:
            print("Invalid choice.")
        driver_mgmt()

    elif driver_menu_choice == 2:
        driver_id = input("Enter Driver ID: ")
        print(driver_availability(driver_id))
        driver_mgmt()

    elif driver_menu_choice == 3:
        driver_id = input("Enter Driver ID: ")
        assignments = get_ongoing_assignments(driver_id)
        if isinstance(assignments, list):
            print(f"Ongoing Assignments for {driver_id}:")
            for assignment in assignments:
                print(f"- {assignment}")
        else:
            print(assignments)
        driver_mgmt()

    elif driver_menu_choice == 4:
        print("\nShipment's Driver Assignment")
        driver_id = input("Enter driver ID of assigned driver: ")
        shipment_id = input("Enter new shipment ID: ")
        origin = input("Enter shipment origin state: ")
        destination = input("Enter shipment destination state: ")
        vehicle_type = input("Enter vehicle type (e.g., Motor, Car, Van): ")
        parcel_weight = float(input("Enter parcel weight (in kg): "))
        round_trip = input("Is this a round trip? (yes/no): ").lower()
        quantity_of_round_trip = int(input("Enter quantity of round trips (0 if not applicable): "))
        vehicle_price = float(input("Enter vehicle price per trip: "))
        total_price = float(input("Enter total price for shipment: "))

        result = assign_shipment(
            driver_id=driver_id,
            shipment_id=shipment_id,
            origin=origin,
            destination=destination,
            vehicle_type=vehicle_type,
            parcel_weight=parcel_weight,
            round_trip=round_trip,
            quantity_of_round_trip=quantity_of_round_trip,
            vehicle_price=vehicle_price,
            total_price=total_price
        )

        print(result)
        driver_mgmt()

    elif driver_menu_choice == 5:
        admin_dashboard()

    else:
        print("\nInvalid choice. Try again.")

#------------------------------------------------------------------------------------------
#*reports* functions:
#1.1 - read key metrics data from txt
def read_data(file_path):
    file_path  = "C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/metrics_data.txt"
    #reads data from the provided text file and returns a dictionary.
    with open(file_path, 'r') as file:
        data_lines = file.readlines()
    data = {}
    current_category = None
    for line in data_lines:
        line = line.strip()
        if line.endswith(":"):
            current_category = line[:-1]  #identify the current category.
            data[current_category] = {}
        elif "-" in line:
            key, value = line.replace("- ", "").split(": ")
            data[current_category][key.strip()] = float(value.strip())  #parse key-value pairs.
    return data

#1.2 - calculates the inventory turnover ratio
def calculate_inventory_turnover(cost_of_goods_sold, average_inventory):
    return cost_of_goods_sold / average_inventory

#1.3 - calculates the average truck turnaround time
def calculate_truck_turnaround_time(total_truck_time, number_of_trucks):
    return total_truck_time / number_of_trucks

#1.4 - calculates the average transportation cost per unit distance
def calculate_average_transportation_cost(total_transportation_cost, total_distance):
    return total_transportation_cost / total_distance

#1.5 - calculates the operating ratio
def calculate_operating_ratio(total_operating_expenses, total_revenue):
    return (total_operating_expenses / total_revenue) * 100

#1 - define key metrics report page
def key_metrics(data):
    inventory_turnover = calculate_inventory_turnover(
        data['inventory']['cost_of_goods_sold'], data['inventory']['average_inventory']
    )
    truck_turnaround = calculate_truck_turnaround_time(
        data['truck_turnaround']['total_truck_time'], data['truck_turnaround']['number_of_trucks']
    )
    avg_transportation_cost = calculate_average_transportation_cost(
        data['transportation_cost']['total_transportation_cost'], data['transportation_cost']['total_distance']
    )
    operating_ratio = calculate_operating_ratio(
        data['operating']['total_operating_expenses'], data['operating']['total_revenue']
    )
    print("--- Key Metrics Report ---")
    while True:
        try: 
            view_choice = int(input("\n1. View Inventory Turnover Ratio\n2. View Truck Turnaround Time\n3. Average Transportation Cost\n4. Operating Ratio\n5. View Summary Key Metrics Report\n6. Back to Reports Page\nEnter your choice number: "))
            if view_choice == 1:
                print(f"\nInventory Turnover Ratio: {inventory_turnover:.2f}") #display inventory turnover ratio 
            elif view_choice == 2:
                print(f"\nAverage Truck Turnaround Time: {truck_turnaround:.2f} hours") #display truck turnaround time
            elif view_choice == 3:
                print(f"\nAverage Transportation Cost: RM{avg_transportation_cost:.2f} per km") #display average transportation cost
            elif view_choice == 4:
                print(f"\nOperating Ratio: {operating_ratio:.2f}%") #display operating ratio
            elif view_choice == 5:
                print(f"\nSummary of Key Metrics Report\nInventory Turnover Ratio: {inventory_turnover:.2f}\nAverage Truck Turnaround Time: {truck_turnaround:.2f} hours\nAverage Transportation Cost: RM{avg_transportation_cost:.2f} per km\nOperating Ratio: {operating_ratio:.2f}%") #display all key metrics report
            elif view_choice == 6:
                reports()
            else:
                print("\nInvalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

#2.1 - reads trip logs from a txt file and returns them as a list of dictionaries
def read_trip_log(file_path):
    #ach dictionary contains details like route, timestamps, and additional information.
    #initialize an empty list to store trip logs
    trip_logs = []
    try:
        #open the file for reading
        with open(file_path, 'r') as file:
            #process each line in the file
            for line in file:
                #split the line into parts based on commas
                parts = line.strip().split(', ')
                #initialize a dictionary for each trip log entry
                trip_log = {}
                #for each part, split it by the delimiter ': ' and assign it to the dictionary
                for part in parts:
                    key, value = part.split(': ', 1)
                    trip_log[key.strip()] = value.strip()
                #add the trip log entry to the list
                trip_logs.append(trip_log)
    except FileNotFoundError:
        print(f"Error: File at {file_path} not found.")
    #return the list of trip logs
    return trip_logs

#2 - define trip logs report
def trip_logs(trip_logs):
    print("--- Trip Logs Report ---")
    #check if there are no trip logs to display
    if not trip_logs:
        print("No trip logs available.")
        return
    
    #display all trips and its details (route details, timestamps), data fetch from txt
    #print the header for the table
    print(f"{'Route':<30}{'Timestamp':<30}{'Driver':<50}")
    print("=" * 110)
    
    #iterate through the trip logs and print each log's details
    for log in trip_logs:
        #get route, timestamp, and details for each log entry
        route = log.get('Route', 'N/A')
        timestamp = log.get('Timestamp', 'N/A')
        driver = log.get('Driver', 'N/A')
        
        #print the trip log in a formatted way
        print(f"{route:<30}{timestamp:<30}{driver:<50}")

#define *reports* main page
def reports():
    print("\n--- Reports ---")
    reports_menu_choice = int(input("1. View Key Metrics Report\n2. View Trip Logs Report\n3. Back to Admin Dashboard\nEnter your choice number: "))

    #check reports menu choice
    if reports_menu_choice == 1:
        #read the data from the text file
        data = read_data("C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/metrics_data.txt")
        #pass the data to key_metrics
        key_metrics(data)
    elif reports_menu_choice == 2:
        #read the trip logs from the text file
        trip_logs_data = read_trip_log("C:/Users/Dani/OneDrive - Asia Pacific University/Semester 2/Programming with Python/Group Assignment/trip_logs.txt")
        #pass the trip logs data to trip_logs function
        trip_logs(trip_logs_data)
        reports()
    elif reports_menu_choice == 3:
        admin_dashboard()
    else:
        print("\nInvalid choice. Try again.")

#------------------------------------------------------------------------------------------
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

#define real admin credentials
real_admin_username = "hilda"
real_admin_password = "happy123"

#define admin main dashboard
def admin_dashboard():
    print("\n--- Welcome to the Admin Dashboard ---")

#*vehicle management* functions:
#1 - define view vehicle performance history page
def vehicle_performance():
    vehicle_id = int(input("\nEnter the vehicle ID to view its performance history: "))
    print("Vehicle Performance of Vehicle ", vehicle_id)
    performance_status = "driver_vehicle_status"
    if performance_status == "Good":
        print("Vehicle Status: Good")
    else:
        view_choice = input("Vehicle Status: Under Maintenance\nView Maintenance History? Yes/No")
        if view_choice == "Yes":
            vehicle_maintenance()
        else:
            vehicle_mgmt()

#2 - define view vehicle maintenance history page
def vehicle_maintenance():
    maintenance_history = [
    {"vehicle_id": 1, "maintenance_id": 1, "maintenance_date": "2023-01-15", "maintenance_service": "Oil Change", "maintenance_cost": 50}, 
    {"vehicle_id": 1, "maintenance_id": 2, "maintenance_date": "2023-03-10", "maintenance_service": "Tire Replacement", "maintenance_cost": 300}, 
    {"vehicle_id": 4, "maintenance_id": 3, "maintenance_date": "2023-05-20", "maintenance_service": "Air Filter Replacement", "maintenance_cost": 20}, 
    {"vehicle_id": 3, "maintenance_id": 4, "maintenance_date": "2023-08-01", "maintenance_service": "Brake Inspection", "maintenance_cost": 80}
    ]
    vehicle_id = int(input("\nEnter the vehicle ID to view its maintenance history: "))
    print("Vehicle Maintenance History of Vehicle ", vehicle_id)
    for record in maintenance_history:
        while record['vehicle_id'] == vehicle_id: 
            filter_history = [f"Vehicle {record['vehicle_id']} had a {record['maintenance_service']} on {record['maintenance_date']}."] 
            print(filter_history)
            break
    view_choice = input("Vehicle Status: Under Maintenance\nView Maintenance History? Yes/No")
    if view_choice == "Yes":
        vehicle_maintenance()
    else:
        
        vehicle_mgmt()


#3 - define plan vehicle inspections page
def vehicle_inspections():
    vehicle_id = int(input("\nEnter the vehicle ID that you would like to plan inspections for: "))
    if vehicle_id == 1:
        print("Plan Inspections for Vehicle 01")
    elif vehicle_id == 2:
        print("Plan Inspections for Vehicle 02")
    elif vehicle_id == 3: 
        print("Plan Inspections for Vehicle 03")

#4 - define get vehicle maintenance alerts and schedules page
def vehicle_alerts_schedules():
    vehicle_id = int(input("\nEnter the vehicle ID to get its maintenance alerts and schedules: "))
    if vehicle_id == 1:
        print("Vehicle Maintenance Alerts and Schedules of Vehicle 01")
    elif vehicle_id == 2:
        print("Vehicle Maintenance Alerts and Schedules of Vehicle 02")
    elif vehicle_id == 3: 
        print("Vehicle Maintenance Alerts and Schedules of Vehicle 03")

#define *vehicle management* main page
def vehicle_mgmt():
    print("\n--- Vehicle Management Page ---")
    print("Options: \n1. View Performance History\n2. View Maintenance History\n3. Plan Inspections\n4. View Maintenance Alerts & Schedules")
    vehicle_menu_option = int(input("Enter option number: "))
    
    #check vehicle menu option
    if vehicle_menu_option == 1:
        vehicle_performance()
    elif vehicle_menu_option == 2:
        vehicle_maintenance()
    elif vehicle_menu_option == 3:
        vehicle_inspections()
    elif vehicle_menu_option == 4:
        vehicle_alerts_schedules()
    else:
        print("Invalid option. Try again.") 

#*fuel management* functions:
#1 - define
#define *fuel management* main page
def fuel_mgmt():
    print("\n--- Fuel Management Page ---")
    print("Options: \n1. View Performance History\n2. View Maintenance History\n3. Plan Inspections\n4. View Maintenance Alerts & Schedules")
    fuel_menu_option = int(input("Enter option number: "))
    
    #check fuel menu option
    if fuel_menu_option == 1:
        vehicle_performance()
    elif fuel_menu_option == 2:
        vehicle_maintenance()
    elif fuel_menu_option == 3:
        vehicle_inspections()
    elif fuel_menu_option == 4:
        vehicle_alerts_schedules()
    else:
        print("Invalid option. Try again.")

def driver_mgmt():
    print("\n--- Driver Management Page ---")

def main():
    while True:
        #prompt for admin's credentials
        print("\nEnter admin's username and password:")
        admin_username = input("Username: ")
        admin_password = input("Password: ")
        
        #check input credentials
        if admin_username == real_admin_username and admin_password == real_admin_password:
            while True:
                admin_dashboard()
                print("Options: Vehicle Management, Fuel Management, Driver Management, or Log Out")
                admin_menu_option = input("Enter option: ")
                
                #check admin menu option
                if admin_menu_option == "Vehicle Management":
                    vehicle_mgmt()
                elif admin_menu_option == "Fuel Management":
                    fuel_mgmt()
                elif admin_menu_option == "Driver Management":
                    driver_mgmt()
                elif admin_menu_option == "Log Out":
                    print("\nLogged Out!")
                    break
                else:
                    print("Invalid option. Try again.")
            break  #exit loop after log out
        else:
            print("\nIncorrect username or password! Enter admin's username and password again.")

if __name__ == "__main__":
    main()

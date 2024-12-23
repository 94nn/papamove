from vehicle_status import check_maintenance

Car_Plate = input("Enter your car plate number: ")
UserID = input("Enter your user ID: ")
Vehicle_Type = input("Enter your vehicle type: ")
Maintenance_Result = input("Enter your maintenance result: ")
Maintenance_Date = input("Enter your maintenance date: ")
if Maintenance_Result == "Good":
    print("No need to send for maintenance!")
else:
    check_maintenance()

print("")
print("Car Plate: ", Car_Plate)
print("UserID: ", UserID)
print("Vehicle Type: ", Vehicle_Type)
print("Maintenance Date: ", Maintenance_Date)
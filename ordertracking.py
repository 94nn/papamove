def track_order():
    while True:
        order_id = input("Enter your Order ID: ")

        try:
            with open("last_order.txt", "r") as parcel_file:
                parcel_ids = [line.strip() for line in parcel_file]
        except FileNotFoundError:
            print("Error: Parcel details file not found.")
            return

        if order_id not in parcel_ids:
            print("Pop Up: Invalid Order ID")
            continue

        try:
            with open("driver_data.txt", "r") as driver_file:
                orders = {}
                for line in driver_file:
                    data = line.strip().split(",")
                    if len(data) == 4:
                        orders[data[0]] = {
                            "status": data[1],
                            "arrival_time": data[2],
                            "current_location": data[3]
                        }
        except FileNotFoundError:
            print("Error: Driver data file not found.")
            return

        if order_id in orders:
            order = orders[order_id]
            if order["status"] == "Delivered":
                print(f"Arrival Time: {order['arrival_time']}, Parcel Delivered")
            else:
                print(f"Current Location: {order['current_location']}, Parcel in Transit")
        else:
            print("Order ID exists in parcel details but no tracking information is available yet.")

        print("\nOptions:")
        print("1. Track another order")
        print("2. Back to main menu")
        decision = input("Enter your choice (1 or 2): ")

        if decision != "1":
            print("Exiting order tracking.")
            break

if __name__ == "__main__":
    track_order()

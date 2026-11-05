class Vehicle:

    def __init__(self, number, vehicle_type):
        self.number = number
        self.vehicle_type = vehicle_type


class ParkingLot:

    def __init__(self, capacity):
        self.capacity = capacity
        self.parked_vehicles = {}

    def park_vehicle(self, vehicle):

        if len(self.parked_vehicles) >= self.capacity:
            print("Parking Lot Full!")
            return

        if vehicle.number in self.parked_vehicles:
            print("Vehicle already parked!")
            return

        self.parked_vehicles[vehicle.number] = vehicle

        print("Vehicle Parked Successfully!")

    def remove_vehicle(self, number):

        if number in self.parked_vehicles:
            del self.parked_vehicles[number]
            print("Vehicle Removed!")
        else:
            print("Vehicle Not Found!")

    def display(self):

        print("\nParked Vehicles:")

        for number, vehicle in self.parked_vehicles.items():
            print(number, "-", vehicle.vehicle_type)

        print("Available Spaces:",
              self.capacity - len(self.parked_vehicles))


# Main class
parking = ParkingLot(3)

while True:

    print("\n1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Display Parking")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        number = input("Vehicle Number: ")
        vehicle_type = input("Vehicle Type: ")

        vehicle = Vehicle(number, vehicle_type)
        parking.park_vehicle(vehicle)

    elif choice == "2":

        number = input("Vehicle Number: ")
        parking.remove_vehicle(number)

    elif choice == "3":
        parking.display()

    elif choice == "4":
        break

    else:
        print("Invalid Choice!")

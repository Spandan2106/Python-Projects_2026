class Driver:

    def __init__(self, driver_id, name):
        self.driver_id = driver_id
        self.name = name
        self.available = True


class Ride:

    def __init__(self, ride_id, passenger, driver):
        self.ride_id = ride_id
        self.passenger = passenger
        self.driver = driver
        self.status = "Assigned"


class RideSharingSystem:

    def __init__(self):
        self.drivers = {}
        self.rides = {}
        self.ride_counter = 0

    def register_driver(self, driver_id, name):

        if driver_id in self.drivers:
            print("Driver already registered!")
            return

        self.drivers[driver_id] = Driver(driver_id, name)
        print("Driver registered!")

    def request_ride(self, passenger):

        driver = next(
            (d for d in self.drivers.values() if d.available),
            None
        )

        if driver is None:
            print("No drivers available!")
            return

        self.ride_counter += 1

        ride = Ride(
            self.ride_counter,
            passenger,
            driver
        )

        self.rides[self.ride_counter] = ride
        driver.available = False

        print("Ride assigned!")
        print("Ride ID:", ride.ride_id)
        print("Driver:", driver.name)

    def complete_ride(self, ride_id):

        ride = self.rides.get(ride_id)

        if ride is None:
            print("Ride not found!")
            return

        if ride.status != "Assigned":
            print("Ride already completed!")
            return

        ride.status = "Completed"
        ride.driver.available = True

        print("Ride completed!")

    def display_rides(self):

        for ride in self.rides.values():
            print(
                ride.ride_id,
                ride.passenger,
                ride.driver.name,
                ride.status
            )


system = RideSharingSystem()

while True:
    print("\n1. Register Driver")
    print("2. Request Ride")
    print("3. Complete Ride")
    print("4. Display Rides")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        driver_id = input("Driver ID: ")
        name = input("Driver Name: ")
        system.register_driver(driver_id, name)

    elif choice == "2":
        passenger = input("Passenger Name: ")
        system.request_ride(passenger)

    elif choice == "3":
        ride_id = int(input("Ride ID: "))
        system.complete_ride(ride_id)

    elif choice == "4":
        system.display_rides()

    elif choice == "5":
        break

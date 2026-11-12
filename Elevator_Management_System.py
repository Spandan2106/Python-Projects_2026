class Elevator:

    def __init__(self, total_floors):
        self.total_floors = total_floors
        self.current_floor = 0

    def move_up(self):
        if self.current_floor < self.total_floors:
            self.current_floor += 1
            print("Elevator moved UP")
        else:
            print("Already at top floor!")

    def move_down(self):
        if self.current_floor > 0:
            self.current_floor -= 1
            print("Elevator moved DOWN")
        else:
            print("Already at ground floor!")

    def go_to_floor(self, floor):
        if floor < 0 or floor > self.total_floors:
            print("Invalid floor!")
            return

        while self.current_floor < floor:
            self.move_up()

        while self.current_floor > floor:
            self.move_down()

        print("Destination reached!")

    def status(self):
        print("Current Floor:", self.current_floor)


elevator = Elevator(10)

while True:
    print("\n1. Move Up")
    print("2. Move Down")
    print("3. Go to Floor")
    print("4. Status")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        elevator.move_up()

    elif choice == "2":
        elevator.move_down()

    elif choice == "3":
        floor = int(input("Enter destination floor: "))
        elevator.go_to_floor(floor)

    elif choice == "4":
        elevator.status()

    elif choice == "5":
        break

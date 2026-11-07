class Room:

    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.available = True


class Hotel:

    def __init__(self):
        self.rooms = {
            101: Room(101, "Single", 1000),
            102: Room(102, "Double", 1800),
            103: Room(103, "Deluxe", 3000),
            104: Room(104, "Single", 1000)
        }

        self.bookings = {}
        self.booking_id = 1000

    def display_rooms(self):
        for room in self.rooms.values():
            status = "Available" if room.available else "Booked"

            print(room.room_number, room.room_type,
                  room.price, status)

    def book_room(self, room_number, customer):
        room = self.rooms.get(room_number)

        if room is None:
            print("Room not found!")
            return

        if not room.available:
            print("Room already booked!")
            return

        self.booking_id += 1
        room.available = False

        self.bookings[self.booking_id] = {
            "room": room_number,
            "customer": customer
        }

        print("Booking successful!")
        print("Booking ID:", self.booking_id)

    def cancel_booking(self, booking_id):
        booking = self.bookings.pop(booking_id, None)

        if booking is None:
            print("Booking not found!")
            return

        self.rooms[booking["room"]].available = True
        print("Booking cancelled!")

    def show_bookings(self):
        for bid, booking in self.bookings.items():
            print(bid, booking)


hotel = Hotel()

while True:
    print("\n1. Display Rooms")
    print("2. Book Room")
    print("3. Cancel Booking")
    print("4. Show Bookings")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        hotel.display_rooms()

    elif choice == "2":
        room = int(input("Room Number: "))
        customer = input("Customer Name: ")
        hotel.book_room(room, customer)

    elif choice == "3":
        bid = int(input("Booking ID: "))
        hotel.cancel_booking(bid)

    elif choice == "4":
        hotel.show_bookings()

    elif choice == "5":
        break

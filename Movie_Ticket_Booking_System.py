class Movie:
    def __init__(self, name, total_seats):
        self.name = name
        self.seats = {i: None for i in range(1, total_seats + 1)}

    def display_seats(self):
        for seat, customer in self.seats.items():
            status = "Available" if customer is None else "Booked"
            print(seat, "-", status)

    def book_seat(self, seat, customer):
        if seat not in self.seats:
            print("Invalid seat!")
        elif self.seats[seat] is not None:
            print("Seat already booked!")
        else:
            self.seats[seat] = customer
            print("Booking successful!")

    def cancel_booking(self, seat):
        if seat in self.seats and self.seats[seat] is not None:
            self.seats[seat] = None
            print("Booking cancelled!")
        else:
            print("No booking found!")


movie = Movie("Avengers", 10)

while True:
    print("\n1. Display Seats")
    print("2. Book Seat")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        movie.display_seats()

    elif choice == "2":
        seat = int(input("Enter seat number: "))
        customer = input("Customer name: ")
        movie.book_seat(seat, customer)

    elif choice == "3":
        seat = int(input("Enter seat number: "))
        movie.cancel_booking(seat)

    elif choice == "4":
        break

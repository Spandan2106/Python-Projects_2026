class Application:

    def __init__(self, company, role):
        self.company = company
        self.role = role
        self.status = "Applied"


class ApplicationTracker:

    def __init__(self):
        self.applications = {}

    def add_application(self, app_id, company, role):

        if app_id in self.applications:
            print("Application ID already exists!")
            return

        self.applications[app_id] = Application(company, role)
        print("Application added!")

    def update_status(self, app_id, status):

        if app_id not in self.applications:
            print("Application not found!")
            return

        allowed = [
            "Applied",
            "OA",
            "Interview",
            "Offer",
            "Rejected"
        ]

        if status not in allowed:
            print("Invalid status!")
            return

        self.applications[app_id].status = status
        print("Status updated!")

    def display_applications(self):

        for app_id, app in self.applications.items():

            print("\nApplication ID:", app_id)
            print("Company:", app.company)
            print("Role:", app.role)
            print("Status:", app.status)

    def search_company(self, company):

        found = False

        for app_id, app in self.applications.items():

            if app.company.lower() == company.lower():
                print(app_id, app.company,
                      app.role, app.status)
                found = True

        if not found:
            print("No application found!")


tracker = ApplicationTracker()

while True:
    print("\n1. Add Application")
    print("2. Update Status")
    print("3. Display Applications")
    print("4. Search Company")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        app_id = input("Application ID: ")
        company = input("Company: ")
        role = input("Job Role: ")

        tracker.add_application(app_id, company, role)

    elif choice == "2":
        app_id = input("Application ID: ")
        status = input("New Status: ")

        tracker.update_status(app_id, status)

    elif choice == "3":
        tracker.display_applications()

    elif choice == "4":
        company = input("Company Name: ")
        tracker.search_company(company)

    elif choice == "5":
        break

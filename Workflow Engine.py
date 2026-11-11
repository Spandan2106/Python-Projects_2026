class Workflow:

    def __init__(self, workflow_id, steps):

        self.workflow_id = workflow_id
        self.steps = steps
        self.current_step = 0

        self.status = "PENDING"
        self.history = []

    def start(self):

        if self.status != "PENDING":
            print("Workflow already started!")
            return

        self.status = "RUNNING"
        self.history.append("Workflow started")

        print("Workflow started!")

    def run_next_step(self):

        if self.status != "RUNNING":
            print("Workflow is not running!")
            return

        if self.current_step >= len(self.steps):
            self.status = "COMPLETED"
            return

        step = self.steps[self.current_step]

        print("Executing:", step)

        self.history.append("Completed: " + step)

        self.current_step += 1

        if self.current_step == len(self.steps):

            self.status = "COMPLETED"

            self.history.append("Workflow completed")

            print("Workflow completed!")

    def fail(self, reason):

        if self.status != "RUNNING":
            print("Workflow is not running!")
            return

        self.status = "FAILED"
        self.history.append("Failed: " + reason)

        print("Workflow failed!")

    def display(self):

        print("\nWorkflow ID:", self.workflow_id)
        print("Status:", self.status)

        print(
            "Progress:",
            self.current_step,
            "/",
            len(self.steps)
        )

        print("History:")

        for event in self.history:
            print("-", event)


workflow = Workflow(
    "WF-1001",
    [
        "Validate Request",
        "Check Resources",
        "Process Operation",
        "Send Completion Event"
    ]
)

while True:

    print("\n1. Start Workflow")
    print("2. Execute Next Step")
    print("3. Fail Workflow")
    print("4. Show Workflow")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        workflow.start()

    elif choice == "2":
        workflow.run_next_step()

    elif choice == "3":
        reason = input("Failure Reason: ")
        workflow.fail(reason)

    elif choice == "4":
        workflow.display()

    elif choice == "5":
        break

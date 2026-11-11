from collections import defaultdict


class MetricsAggregator:

    def __init__(self):
        self.metrics = defaultdict(list)

    def record(self, name, value):

        self.metrics[name].append(float(value))
        print("Metric recorded!")

    def summary(self, name):

        values = self.metrics.get(name, [])

        if not values:
            print("No metrics found!")
            return

        print("\nMetric:", name)
        print("Count:", len(values))
        print("Minimum:", min(values))
        print("Maximum:", max(values))

        average = sum(values) / len(values)

        print("Average:", round(average, 2))

    def display_all(self):

        for name, values in self.metrics.items():

            average = sum(values) / len(values)

            print(
                name,
                "Count:", len(values),
                "Average:", round(average, 2)
            )


metrics = MetricsAggregator()

while True:

    print("\n1. Record Metric")
    print("2. Show Summary")
    print("3. Display All")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        name = input("Metric Name: ")

        try:
            value = float(input("Value: "))
            metrics.record(name, value)
        except ValueError:
            print("Enter a valid number!")

    elif choice == "2":
        metrics.summary(input("Metric Name: "))

    elif choice == "3":
        metrics.display_all()

    elif choice == "4":
        break

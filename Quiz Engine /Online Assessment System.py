class Question:

    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer


class Quiz:

    def __init__(self):
        self.questions = []
        self.results = {}

    def add_question(self, question):
        self.questions.append(question)

    def start_quiz(self, username):

        score = 0

        for i, q in enumerate(self.questions):

            print("\n", i + 1, ".", q.question)

            for option in q.options:
                print(option)

            answer = input("Your answer: ").strip().upper()

            if answer == q.answer:
                score += 1

        self.results[username] = {
            "score": score,
            "total": len(self.questions)
        }

        print("\nQuiz Completed!")
        print("Score:", score, "/", len(self.questions))

    def show_results(self):

        for user, result in self.results.items():
            print(
                user,
                result["score"],
                "/",
                result["total"]
            )


quiz = Quiz()

quiz.add_question(Question(
    "Which language is used for AI?",
    ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
    "A"
))

quiz.add_question(Question(
    "Which data structure uses FIFO?",
    ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
    "B"
))

quiz.add_question(Question(
    "Which protocol is used for web communication?",
    ["A. FTP", "B. SMTP", "C. HTTP", "D. SSH"],
    "C"
))

while True:
    print("\n1. Start Quiz")
    print("2. Display Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Enter username: ")
        quiz.start_quiz(username)

    elif choice == "2":
        quiz.show_results()

    elif choice == "3":
        break

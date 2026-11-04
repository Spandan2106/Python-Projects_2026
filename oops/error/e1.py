class InvalidEmailError(Exception):
    def __init__(self, email, msg="Invalid email format"):
        self.email = email
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f"{self.email} -> {self.msg}"

def set_email(email):
    if "@" not in email:
        raise InvalidEmailError(email)
    print(f"Email set to: {email}")

try:
    s= input("Enter the email: ")
    set_email(s)
except InvalidEmailError as e:
    print(e)
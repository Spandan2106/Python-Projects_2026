import secrets
import string
def generate_password(length, use_upper, use_digits, use_symbols):
  pool = string.ascii_lowercase
  required = [secrets.choice(string.ascii_lowercase)]
  if use_upper:
    pool += string.ascii_uppercase
    required.append(secrets.choice(string.ascii_uppercase))
  if use_digits:
    pool += string.digits
    required.append(secrets.choice(string.digits))
  if use_symbols:
    symbols = "!@#$%^&*()-_=+"
    pool += symbols
    required.append(secrets.choice(symbols))

  if length < len(required):
    length = len(required)

  remaining = [secrets.choice(pool) for _ in range(length - len(required))]
  chars = required + remaining
  secrets.SystemRandom().shuffle(chars)
  return "".join(chars)


def ask_yes_no(prompt):
  while True:
    ans = input(prompt).strip().lower()
    if ans in ("y", "yes"):
      return True
    if ans in ("n", "no"):
      return False
    print("Enter y or n.")


def main():
  print("Password Generator")
  try:
    length = int(input("Enter password length (minimum 4): "))
    if length < 4:
      print("Minimum length is 4. Using 4.")
      length = 4
  except ValueError:
    print("Invalid number. Using length 12.")
    length = 12

  use_upper = ask_yes_no("Include uppercase letters? (y/n): ")
  use_digits = ask_yes_no("Include digits? (y/n): ")
  use_symbols = ask_yes_no("Include symbols? (y/n): ")

  password = generate_password(length, use_upper, use_digits, use_symbols)
  print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
  main()

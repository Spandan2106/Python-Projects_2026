import string
import random

class URLShortener:

    def __init__(self):
        self.url_database = {}

    def generate_code(self, length=6):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))

    def shorten_url(self, url):
        code = self.generate_code()

        while code in self.url_database:
            code = self.generate_code()

        self.url_database[code] = url

        return "short.ly/" + code

    def get_original_url(self, short_url):
        code = short_url.split("/")[-1]

        return self.url_database.get(code, "URL not found")


# Main class
shortener = URLShortener()

while True:

    print("\n1. Shorten URL")
    print("2. Get Original URL")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        url = input("Enter original URL: ")
        print("Short URL:", shortener.shorten_url(url))

    elif choice == "2":
        url = input("Enter short URL: ")
        print("Original URL:", shortener.get_original_url(url))

    elif choice == "3":
        break

    else:
        print("Invalid choice!")

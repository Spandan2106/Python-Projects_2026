#bank management system by oops
class Account:
    def __init__ (self,inibalance=0):
        self.balance = inibalance
        
    def diposit(self,amount):
        if amount >0:
            self.balance += amount
            print(f"The {amount} is diposited,now total amount is {self.balance}")
        else:
            print("Plese enter a positiove amount")
    def withdraw(self,amount):
        if amount>0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"The {amount} is withdrawed,now total amount is {self.balance}")
            else:
                print(f"Balance is in suffecient , balance is = {self.balance}")
        else:
            print("Plese enter a positiove amount")
    def display(self):
        print(f"The balance is = {self.balance}")
a = Account()
while True:
    print("1. Diposit")
    print("2. Withdraw")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        amount = float(input("Enter the amount to diposit : "))
        a.diposit(amount)
    elif choice == 2:
        amount = float(input("Enter the amount to withdraw : "))
        a.withdraw(amount)
    elif choice == 3:
        a.display()
    elif choice == 4:
        print("Thank you for using our bank management system.")
        break
    else:
        print("Invalid choice, please try again.")


            
        
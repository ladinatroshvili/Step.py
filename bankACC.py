class BankAccount:
    bank_name = "BOG"                  

    def __init__(self, card_type, owner, balance=0):
        self.card_type = card_type      
        self.owner = owner             
        self.balance = balance

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        if value < self.min_balance():
            print("შეცდომა: ბალანსი არ შეიძლება იყოს უარყოფითი.")
        else:
            self.__balance = value
    def min_balance(self):                 
        return 0
    @balance.deleter
    def balance(self):
        del self.__balance

    def deposit(self, amount):             
        if amount > 0:                    
            self.balance += amount         
        else:
            print("თანხა უნდა იყოს დადებითი")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("ანგარიშზე არ არის საკმარისი თანხა")
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
    @staticmethod
    def calculate_tax(amount):
        return amount * 0.1


class SavingsAccount(BankAccount):
    def __init__(self, card_type, owner, balance=0, interest_rate=0):
        super().__init__(card_type, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)
        return interest

    def withdraw(self, amount):
        fee=2
        total_withdrawal = amount + fee
        if total_withdrawal <= self.balance:
            self.balance -= total_withdrawal
        else:
            print("ანგარიშზე არ არის საკმარისი თანხა")
    


class creditlimit(BankAccount):
    def __init__(self, card_type, owner, balance=0, credit_limit=0):
        self.credit_limit = credit_limit
        super().__init__(card_type, owner, balance)
        

    def withdraw(self, amount):
        if amount <= self.balance + self.credit_limit:
            self.balance -= amount
        else:
            print("ანგარიშზე არ არის საკმარისი თანხა და საკრედიტო ლიმიტი")
    def min_balance(self):                 
        return -self.credit_limit
account1 = BankAccount("Visa", "ladi", 1000)
account2 = BankAccount("Mastercard", "ladi1", 500)
account3 = BankAccount("Visa", "ladi2", 2000)
account4 = BankAccount("Mastercard", "ladi3", 1500)
account1.deposit(100)
print(account1.balance)
account2.withdraw(5100)
print(account2.balance)
account2=creditlimit("Mastercard", "ladi4", 1000, 5000)
account2.withdraw(5500)
print(account2.balance)
tax = account2.calculate_tax(5500)
print(f"გადასახადი: {tax}")


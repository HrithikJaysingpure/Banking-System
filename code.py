class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def personal_details(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('Gender:',self.gender)

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
    def deposit(self):
        amount = int(input('Enter amount to be deposit:'))
        self.balance = self.balance + amount
        print('Current Balance:',self.balance)
    def withdraw(self):
        amount = int(input('Enter amount to be withdraw:'))
        if amount > self.balance:
            print('insufficient balance | current balance',self.balance)
        else:
            self.balance = self.balance - amount
            print('Current balance:',self.balance)

hrithik = Bank('Abc',21,'Male')
hrithik.personal_details()
hrithik.deposit()
hrithik.withdraw()

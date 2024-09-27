class bank:

    def __init__(self,main):
        self.bal=main
    def deposit(self,amt):
        self.bal+=amt
        print("deposit",amt)
    def windrow(self,amt):
        self.bal-=amt
        print("windrow",amt)
    def display(self):
        print("balance=",self.bal)

user1=bank(100)
user1.deposit(1000)
user1.windrow(100)
user1.display()

class demo:
    def __init__(self,a):
        print(a)
ob=demo(12)
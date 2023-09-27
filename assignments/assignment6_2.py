
class BankAccount:
    ROI=10.5
    def __init__(self,namee,amountt):
        self.name=namee
        self.amount=amountt
    
    def Display(self):
        print("Name is",self.name)
        print("Amount is",self.amount)
    def Deposit(self,depo):
        self.amount+=depo
    def Withdraw(self,depo):
        self.amount-=depo

    def CalculateInterset(self,time):
        simple_intereset=(self.amount *time* BankAccount.ROI)/100
        print("The Simple intereset is",simple_intereset)        


def main():
    Obj1 = BankAccount("Bhai",3000)
    Obj1.Display()

    Obj1.Deposit(3000)
    Obj1.Display()
    Obj1.Withdraw(2000)
    Obj1.Display()
    Obj1.CalculateInterset(2)

    Obj1 = BankAccount("Om", 10000)
    Obj1.Display()
    Obj1.Deposit(2000)
    Obj1.Display()
    Obj1.Withdraw(5000)
    Obj1.Display()
    Obj1.CalculateInterset(5)



if __name__=="__main__":
    main()
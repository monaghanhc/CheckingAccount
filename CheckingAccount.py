class CheckingAccount:
    #Constuctor
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    #Accessor 
    def getBalance(self):
        print("Prior Amount: ", self.balance,"$")
        return self.balance 

    #Setter
    def setName(self, name):
        if name == str:
            return self.name

    #Methods
    def deposit(self, amount):
        print("\nAmount that was deposited: ", amount,"$")
        #self.balance += amount
        if amount >= 0:
            self.balance += amount
            return self.balance
        else:
            print("You have negative money")
            
    def checkingAccount(self):
        print("\nNet Available Balance: ", self.balance, "$")

def main():
    myAccount = CheckingAccount("Jenny Call", 0)

    #Original Amount:
    testOriginalAmt = myAccount.getBalance()
    

    #Deposit
    testDeposit = myAccount.deposit(50)
    #print("\nTotal Amount: ", testDeposit)

    #Output Checking Account
    testCheckingAccount = myAccount.checkingAccount()
    
    
    #DONE
    print("\n\nDone")
main()
    
    
       
            

    
    


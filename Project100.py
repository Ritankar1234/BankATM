class ATM:
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
    def checkBalance(self):
        print("Your Balance is 50000")
    def cashWithdrawal(self,amount):
        newAmount=50000-amount
        print("Your Balance is"+str(newAmount))
def main():
    cardNumber=input("Enter your card number")
    pin=input("Enter Your pin")
    newUser=ATM(cardNumber,pin)
    print("Choose your activity")
    print("1. Balance Enquiry 2. Withdrawal")
    activity=int(input("enter your activity number"))
    if(activity==1):
        newUser.checkBalance()
    elif(activity==2):
        amount=int(input("Enter your amount"))
        newUser.cashWithdrawal(amount)
    else:
        print("Enter a valid number")
main()


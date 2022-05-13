
# Program Name: The Bank of Drew
# Author: Drew Hamblett
# Date: 5/13/2022
# Summary: A banking system capable of keeping track of moneyflow and emuulating a basic ATM machine
# Variables: 
#   AccountChoice: Holds account number (int)
#   Naccountnum: spot for randint to choose a filename (int)
#   AddedBalance: number to append to end of file (int)
#   Totalbal: sum of transactions in account document (float)
#   Lines: Stores lines from file
#   TransAct: Stores account to transfer into (int)
#   TransBal: Stores ammount to transfer between accounts (float)


from random import randint

# Selection of account/file

def AccountSelection():
    global AccountChoice
    AccountChoice = input("Please input account number to see account or 'new' to create one: ")
    if AccountChoice == 'new':
        Naccountnum = randint(0,1542562542)
        f = open(str(Naccountnum) + ".txt","x")
        f.write ("Account Num: " + str(Naccountnum))
        f.write("\n")
        f.write("Account History:")
        f.write("\n")
        f.close()
        f = open(str(Naccountnum) + ".txt","r")
        print(f.read())
        f.close()
        AccountChoice = Naccountnum

# Sees if a number is real, regardless of decible
def isnum(s):
    try:
        float(s)
    except:
        return False
    else:
        return True

# Appends added money to end of file

def Addmoney():
    AddedBalance = input("\nPlease enter balance to add: $")
    while AddedBalance.isnumeric() == False:
        AddedBalance = input("ERROR...Please enter numeric balance to add: $")
    f = open(str(AccountChoice) + ".txt","a")
    f.write(str(AddedBalance))
    f.write("\n")
    f.close()
    print("\n$"+ str(AddedBalance) + " has been successfull added.")

# Returns the balance of the account currently
def Checkbalance():
    global Totalbal
    Totalbal = 0
    with open(str(AccountChoice) + ".txt","r") as f:
        next(f)
        next(f)
        for line in f:
            num = float(line)
            Totalbal += num
        print ("\nThe balance is: $" + str(Totalbal))
    f.close()

# Transfers balance to another account/file
def Transferbalance():
    TransAct = int(input("\nEnter Account number to transfer to: "))
    f = open(str(AccountChoice) + ".txt","a")
    Altf = open(str(TransAct) + ".txt","a")
    TransBal = float(input("\nEnter ammount to transfer: "))
    Altf.write(str(TransBal))
    Altf.write("\n")
    f.write("-"+str(TransBal))
    f.write("\n")
    Altf.close()
    f.close()
    print("\nTransfered successfully.")

# Subtracts balance from account
def Withdrawbalance():
    SubBalance = 0
    Checkbalance()
    SubBalance = (input("Please enter balance to withdraw : $"))
    while isnum(SubBalance) == False:
        print ("ERROR... Numeric numbers only")
        SubBalance = input("Please enter balance to withdraw : $")
    SubBalance = float(SubBalance)
    while SubBalance < 0:
        print("ERROR... Positive real numbers only")
        SubBalance = float(input("Please enter balance to withdraw : $"))
    while (Totalbal - SubBalance) < 0:
        print("ERROR... Insufficient balance")
        SubBalance = float(input("Please enter balance to withdraw : $"))
    f = open(str(AccountChoice) + ".txt","a")
    f.write("-" + str(SubBalance))
    f.write("\n")
    f.close()
    print("\n$" + str(SubBalance) + " has been withdrawn.\n")

# Shows a list of user selected ammount of transactions
def RecentTransactions():
    TransAmt = int(input("How many transactions should be displayed: "))
    print("") 
    f = open(str(AccountChoice) + ".txt","r")
    lines = f.readlines()
    lastlines = lines[-int(TransAmt):]
    for line in lastlines:
        print("$",line)

# Menu for selection purposes
def Selection ():
    Fstchoice = 0
    while Fstchoice != 6:
        print ("\nWhat would you like to do?\n 1. Add balance \n 2. Check balance \n 3. Tranfer balance \n 4. Withdraw balance \n 5. Check recent transactions \n 6. Exit")
        Fstchoice = input("Please enter a numaric selection: ")
        while isnum(Fstchoice) == False:
            print("ERROR...")
            Fstchoice = input("Please enter a numaric selection: ")
        while not int(Fstchoice) in range(1,7):
            print ("ERROR 2...")
            Fstchoice = int(input("Please enter a numaric selection within range: "))
        Fstchoice = int(Fstchoice)

        if Fstchoice == 6:
            print("Have a good day!")
            exit()
        functions = {
            1:Addmoney,
            2:Checkbalance,
            3:Transferbalance,
            4:Withdrawbalance,
            5:RecentTransactions}
        functions[Fstchoice]()




AccountSelection()
Selection()



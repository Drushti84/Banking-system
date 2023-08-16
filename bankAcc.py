class bankAcc:
    __balance= None
    __amount= None
    __total= None

    def __init__(self, balance, amount):
        self.__balance = balance
        self.__amount = amount
        self.__total = amount+balance

    def showDepCash(self):
        print("The account balance is "+str(self.__balance)+"The amount is "+str(self.__amount))
        print("The total is"+str(self.__total))
import sys
import time
func = []
balance = ["Your new balane is",]
class Atm:
    def __init__(self):
        self.account = ["1.","Deposit","2.","Check Balance","3.","Transfer","5.","Exit"]
        self.user_account_number = "0238945204"
        self.user2_account_number ="0168175923" 
        self.customer()
    def customer(self):
        print("WELCOME,,, PRESS 1 TO REGISTER AND 2 TO LOGIN")
        user_customer = input()
        if user_customer == "1":
            print("Please wait>>>")
            self.register()
        elif user_customer == "2":
            print("Please wait>>>")
            time.sleep(2)
            self.login()
    def register(self):
        self.name = input("Enter your First, Middle, Name")
        date_of_birth = input("Date of Birth")
        occupation = input("Occupation")
        self.pin = input("Input Your pin")
        print("Dear Customer, please Chesck if this is what you input")
        print("Name---", self.name)
        print("Date of birth---",str(date_of_birth))
        print("Occupation---",occupation)
        print("Your pin---",str(self.pin))
        func.append({self.name:{'name':self.name,'Dob':date_of_birth, 'occupation':occupation,"pin":self.pin,}}) 
        for x in func:
            print("Please wait a minute while we generate your Account Number")
            time.sleep(3)
            print("Dear User, You Have Successfully Opened an Account With Us and Your Account Number is ",self.user_account_number)
            time.sleep(2)
        print("please wait>>>")
        self.login()
        print(func)
    def login(self):
        time.sleep(2)
        if func == []:
            self.register()
        else:
            print("Please login With Your Name and Pin")
            user = input("Please Enter Your Name")
            user_pin = input("Please Input Your Pin")
            for x in func:
                print(x)
                print("Welcome Mr/Mrs", x[f'{self.name}']['name'],"Date of birth",x[f'{self.name}']['Dob'],"Occupation",x[f'{self.name}']['occupation'])
                if x[f'{self.name}']['name'] == user and x[f'{self.name}']['pin']==user_pin:
                    time.sleep(2)
                    print(self.account)
                else:
                    print("Incorrect Pin and Password")
                    time.sleep(2)
                    print("Please Wait>>>>")
                    time.sleep(2)
                    self.register()
            self.deposit()
    def deposit(self):
        user_input = input()
        if user_input[0] == "1":
            user_1 = input("Enter The Amount")
            balance.append(user_1)
            print(balance)
            self.balance()
        elif user_input == "2":
            self.balance()
        elif user_input == "3":
            self.transfer()
        elif user_input == "5":
            sys.exit()
    def balance(self):
        print("Press YES to Check balance and NO to go back to main menu")
        user_balance =input()
        if user_balance.strip().lower() == "yes":
            print(balance)
        elif user_balance.strip().lower() == "no":
            self.login()
        self.transfer()
    def transfer(self):
        user2_input = input("Enter The Amount")
        user3_input = input("Enter Accont Number")
        balance.append(user2_input)
        print("You Have Successfully Sent","#",user2_input,balance)
        self.login()
    #     self.exit()
    # def exit(self):
atm = Atm()


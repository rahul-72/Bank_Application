#!/usr/bin/env python
# coding: utf-8

# In[10]:


# This is a bank application by class..

"""                 ********************************************************************** """

import json,time,os,sys         #importing useful libraries....
from random import randint
from getpass import getpass

"""    **************************************************************************** """
#load_data() to load data .    
def load_data(cls_name):
    """This is to load data."""
    try:
        fp=open("bank.json",'r+')  # opening of bank.json file in current location.
        bank=json.load(fp)
        fp.close()
        f=open("bank_log.json",'r+')  #opening of bank_log.json file
        bank_log=json.load(f)
        f.close()
        cls_name.bank=bank
        cls_name.bank_log=bank_log
    except Exception as msg:
        print("Make sure bank.json file and bank_log.json file are in the same directory from where you are running this script")
        print(f"ERROR----->>>>> {msg}")

    
"""             *********************************************************************************"""
  #dump_data() to dump data.  
def dump_data(cls_name):
    """This is to dump data"""
    
    try:
        fp=open("bank.json",'r+')   #dumping bank 
        json.dump(cls_name.bank,fp)
        fp.close()

        fp=open("bank_log.json",'r+')  #dumping bank_log 
        json.dump(cls_name.bank_log,fp)
        fp.close()   
    except Exception as msg:
        print("Make sure bank.json file and bank_log.json file are in the same directory from where you are running this script")
        print(f"ERROR----->>>>> {msg}")

        
        
        
"""              **************************************************************************************"""
    
    #Bank class.
class Bank:
    """This is a bank class ."""
    bank={}
    bank_log={}
    def main_menu(self):
        """main_menu() will display the main menu of SBI bank.
        Here you have to enter choice from 1/2/3 which will lead you to login,signup,exit respectively."""
        
        try:
            self.clr_scr()
            print(f""".................Welcome to SBI bank application.................""")
            print("\n\n")
            print(f"""you have to enter choice from 1/2/3
            1). Login
            2). Signup
            3). exit""")
            print("\n\n")
            choice=int(input("Enter your choice:\t\t"))
            l=[1,2,3]
            if choice in l:
                if choice==1:
                    return self.login()     #"self.login" because id of object will call login() function....
                elif choice==2:
                    return self.signup()
                else:
                    return self.exit()
            print("\n\n")    
            print(f"WARNING----->>>>>>Enter choice from 1/2/3 only.")
            time.sleep(1)
            self.clr_scr()   #clearing screen
            return self.main_menu()
        
        except Exception as msg:
            print("\n\n")
            print("Error in main_menu() function")
            print("ERROR---->>>> ",msg)
            time.sleep(3)
            self.main_menu()    #after handling exception i'm going to main_menu function again.
            

    
    uname=''       # class variable
    pword=''
    def login(self):
        """login() will take username and paasword to login
        into your SBI bank"""
        
        try:
            self.clr_scr()      #clearing screen
            user_name=input("Enter your username:\t\t")
            pass_word=input("Enter your password:\t\t")
            print("\n\n")
            for i in self.bank:
                if user_name==i:
                    if pass_word==self.bank[i]['password']:
                        #global uname      # 
                        #global pword
                        Bank.uname=user_name   #This  is how we use class variable.
                        Bank.pword=pass_word

                        self.banklog() 
                                    # instead of using class variable one can pass user_name to login_menu()
                        return self.login_menu()               #like login_menu(user_name)
                    print("WARNING----->>>>>>Invalid Password")
                    print()
                    input("Press any key to continue.....................")
                    return self.main_menu()
                continue
            print("WARNING------>>>>>>Invalid Username")
            print()
            input("Press any key to continue............")
            return self.main_menu()
        
        except Exception as msg:
            print("\n\n")
            print("Error in login() function")
            print("ERROR----->>>>> ",msg)
            self.login()


    
    def login_menu(self):
        """This function will only call after you login into SBI bank.
        Here you can debit,credit,logout or can check your balance and account number."""
        
        try:
            self.clr_scr()

            print(f"**********Welcome {self.bank[Bank.uname]['name'].upper()} to SBI bank application.************* ")
            print("\n\n")
            print(f"""You have to enter choices from 1/2/3/4
            1). debit
            2). credit
            3). check balance and account_number
            4). logout""")
            print("\n\n")
            choice=int(input("Enetr choice from 1/2/3/4.\t\t"))
            l=[1,2,3,4]
            if choice in l:
                if choice==1:
                    return self.debit()
                elif choice==2:
                    return self.credit()
                elif choice==3:
                    return self.check_balance()
                return self.logout()
            print("\n\n")
            print("Warning----->>>>>> Enter choice only from 1/2/3/4")
            return self.login_menu()
        
        except Exception as msg:
            print("\n\n")
            print("Error in login_menu() function")
            print("ERROR------>>>>>> ",msg)
            time.sleep(3)
            self.login_menu()
    
    
    
    def debit(self):
        """debit() will take amount and add it to your balance.
        Then it will also show your net balance.
        And after that it will return to login_menu() """
        
        try:
            self.clr_scr()
            amount=int(input("Enter debit amount:\t\t"))
            print("\n\n")
            if self.bank[Bank.uname]['bal']>amount:
                self.bank[Bank.uname]['bal']-=amount
            else:
                print("WARNING------>>>>>> You do not have sufficient balance.")
                print()
            print(f"Now the net balance is:\t {self.bank[Bank.uname]['bal']}")
            time.sleep(2)
            return self.login_menu()
        
        except Exception as msg:
            print("\n\n")
            print("Error in debit() function")
            print("ERROR------>>>>> ",msg)
            time.sleep(2)
            self.debit()
    
    
    def credit(self):
        """credit() will take amount and reduce it from your balance.
        Then it will show your net balance.
        And after that it will return to login_menu()"""
        
        try:
            self.clr_scr()
            amount=int(input("Enter credit amount:\t\t"))
            print("\n\n")
            self.bank[Bank.uname]['bal']+=amount
            print(f"Now the net balance is:\t {self.bank[Bank.uname]['bal']}")
            time.sleep(2)
            return self.login_menu()
        
        except Exception as msg:
            print("\n\n")
            print("ERROR------>>>>>> ",msg)
            time.sleep(2)
            self.credit()

    
    
    def check_balance(self):
        """check_balance() will show your net balance.
        And after that it will return to login_menu()."""
        
        try:
            self.clr_scr()
            print(f"Your balance is:\t {self.bank[Bank.uname]['bal']}")    #Here i'm using class variable uname.
            print("\n\n")
            print(f"Your account number is: \t {self.bank[Bank.uname]['account_num']}")
            time.sleep(4)
            return self.login_menu()
        
        except Exception as msg:
            print("\n\n")
            print("ERROR------>>>>>> ",msg)
            time.sleep(3)
            self.main_menu()

    
    def logout(self):
        """This is a logout() function .It will only return main_menu()"""
        try:
            self.clr_scr()
            print("...................You successfully logout from your account.......................")
            time.sleep(1)
            return self.main_menu()
        except Exception as msg:
            print("\n\n")
            print("Error in logout() function")
            print("ERROR------>>>>>> ",msg)
            time.sleep(3)
            self.main_menu()
    
    
    # getpass can be used here
    def signup(self):
        """Here you have to enter your name,username,password.
        And then you will get your account number.
        After that it will return to main_menu()"""
        
        try:
            self.clr_scr()
            name=input("Enter your name:\t\t")
            print("\n\n")
            while True:                         # 'for loop' can't be used here because we have to search from begining again 
                user_name=input("Enter username:\t\t")   #and again in loop.
                print("\n\n")                                     
                if user_name in self.bank:
                    print("""SORRY--->>>This username is already taken.
                    please enter another username.""")   # To check whether a username is already taken or not.
                    print()                                    
                    continue
                break
            print(f"your username = {user_name}")
            print("\n\n")
            self.clr_scr()
            l="""`~!@#$%^&*()_-+={}[]|\:'';""/?.>,<*"""
            while True:
                self.clr_scr()   
                pass_word=getpass("Enter password:\t\t")
                print("\n\n")
                if len(pass_word)>=8:      #password should be length of 8 or more.
                    for i in pass_word:
                        if i in l:    #To check whether password contain special character or not.
                            print(f"WARNING------>>>>>> Enter password without special character.")
                            time.sleep(1)
                            break      # im breaking 'for loop'
                        continue    # continue for 'while loop'
                    else:
                        print()
                        pass_word_veri=getpass("Enter your password again for verification:\t\t")
                        print("\n\n")
                        if pass_word==pass_word_veri:       #password verification
                            print("Your password verified successfully.")
                            break        # break for 'while loop'.
                        else:
                            continue

                else:
                    print("WARNING------>>>>>> Enter password of length more than or equal to  8.")
                    print("\n\n")
                    time.sleep(1)
                    continue

            print("\n\n")
            self.clr_scr()
            print(f"""Your username is: \t\t {user_name}
            Your password is: \t\t {pass_word}""")
            while True:
                q,w,e,r=map(str,[randint(0,9) for i in range(4)]) #Assigning 4 random number to update account-number in dictionary.
                a=q+w+e+r
                for i in self.bank:
                    if self.bank[i][account_num]==a:   #checking whether a randomly generated account number is already in bank dictionary 
                        break                   # or not.
                    continue
                else:
                    break
            self.bank.update([(user_name,{'name':name,'bal':0,'account_num':a,'password':pass_word})])
            return self.main_menu()
        
        except Exception as msg:
            self.clr_scr()
            print("Error in singup() function")
            print("ERROR------>>>>> ",msg)
            self.singup()




    def exit(self):
        """exit() to exit from SBI bank application."""
        self.clr_scr()
        print("...............Please wait you are exiting from SBI bank application...............")
        time.sleep(2)
        print( "...........You successfully exit from SBI application...............")

    
    
    
    def clr_scr(self):
        """This is to clear screen ."""
        time.sleep(0.5) # some delay in clearing screen
        
        if sys.platform=='win32' or sys.platform=='win64':  #To check whether a system is window or linux.
            os.system('cls')       # clearing screen of window system
        else:
            os.system('clear')   #clearing screen of linux system
        
        print("\n\n\n\n")      #four blank lines on the top of blank screen.
    
    
    
    def banklog(self):
        """This is banklog() used to store logging time of particular user"""

        if Bank.uname in self.bank_log:
            self.bank_log[Bank.uname].append(time.ctime())  #if username exits
        else:
            self.bank_log.update([(Bank.uname,[time.ctime()])]) #if username do not exits
        
        
        
"""        ***************************************************************************************"""
        
# Main body of program.
if __name__=='__main__':
    load_data(Bank)     #calling load_data() function by passing Bank class as argument.
    bk=Bank()          # making object
    bk.main_menu()
    dump_data(Bank)     #calling dump_data() function by passing Bank class as argument.


# In[ ]:





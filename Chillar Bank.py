# Bank
import time as t
import os

try :
	with open("balance.txt") as f:
	  	with open("balance.txt","r") as f:
	      	 read = f.read()
	  	if read == "":
	      	 with open("balance.txt","w") as f:
  	 	   	 write = f.write("0")
except FileNotFoundError:
	with open("balance.txt","w") as f:
		f.write("0")
info = print ("Welcome To 💰😂 Chillar Bank 😂💰 \n 1 - check your current balance \n 2 - Add money 💰 \n 3 - Withdraw money \n q - quit ")
t.sleep(2)

command = (input ())



class Bank:
  # Command execution
  def Command_execution(self):
    work = True
    while work == True:
      if command == "1":
        print(f"Your current Balance: ₹{my_acc.balance()}")
        break
      elif command == "2":
        t.sleep(1)
        my_acc.add_money()
        break
      elif command == "3":
        t.sleep(1)
        my_acc.take_money()
        break
      elif command == "q":
        work = False
      

  bank_name = "Chillar"
  with open("balance.txt") as f:
    bank_balance_int = int(f.read())
    
  
  
  def balance(self):
    return self.bank_balance_int
  
  def add_money(self):
    add = int(input("How much money u want to add"))
    self.bank_balance_int += add
    with open("balance.txt","w") as f:
      f.write(str(self.bank_balance_int))
    return print(f"Money added! \n Your updated balance now: ₹{self.bank_balance_int}")
      
  def take_money(self):
    take = int(input("how much money u want ?"))
    if self.bank_balance_int < take:
      t.sleep(1)   
      print(f"Sorry sir you dont have sufficient balance to withdraw ❗ \n Your balance : ₹{self.bank_balance_int}")
    else:
      self.bank_balance_int -= take
      with open("balance.txt","w") as f:
        f.write(str(self.bank_balance_int))
      print (f"Withdraw Succesfull! updated balance: ₹{self.bank_balance_int}")
    
    
    
    
    
my_acc = Bank()
loop = my_acc.Command_execution()


#------------------------------------------------------------------------------------#


    


  
  

  





  
  




















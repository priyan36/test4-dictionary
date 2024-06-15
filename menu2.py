from module2 import Bank
bank = Bank()



while True:
    serv = int(input("Service Provided:\n1. Acc Creation\n2. Deposit\n3. Withdraw\n4. Fixed Deposit\n5. Exit\n"))
      
    if serv == 1:
        name = input("Enter Name: ")
        bal = int(input("Enter Deposit Amt: "))
        fd = int(input("Enter FD Amt: "))
        Bank.create(name, bal, fd)
      
    elif serv == 2:
        accno = int(input("Enter Accno: "))
        depamt = int(input("Enter Deposit amt: "))
        Bank.deposit(accno, depamt)

#4. Fixed Deposit
#5. Exit
#2
#Enter Accno: 123
#Enter Deposit amt: 1200
#Traceback (most recent call last):
 # File "c:\Users\priya\Desktop\VS Code\test4 dictionary\menu2.py", line 18, in <module>
  #  Bank.deposit(accno, depamt)
#TypeError: Bank.deposit() missing 1 required positional argument: 'depamt'
#PS C:\Users\priya\Desktop\VS Code\test4 dictionary> ""

#depamt have been declred in fanction properly but still getting this error.
#same error appears in withdraw,fd were the widamt and fdamt seems to be missing.
      
    elif serv == 3:
        accno = int(input("Enter Accno: "))
        witamt = int(input("Enter Withdraw Amount: "))
        Bank.withdraw(accno, witamt)  
    
    elif serv == 4:
        accno = int(input("Enter Accno: "))
        fdamt = int(input("Enter FD Amount: "))
        yrs = int(input("Enter FD Years: "))
        Bank.fd(accno, fdamt, yrs)  
    
    elif serv == 5:
        break 

bank.transaction()
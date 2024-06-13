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
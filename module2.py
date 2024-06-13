import random

class Bank:
    def _init_(self):
        self.data = [["Suresh", 123, 2000, 5000], ["Raina", 124, 400, 1000], ["Virat", 125, 6000, 2000]]
        self.transactions = []

    def chkbal(self, accno):
        for i in self.data:
            if i[1] == accno:
                print("Your Balance: ", i[2])
                return
        print("Invalid AccNO")

    def create(self, name, bal, fd):
        accno = self.data[-1][1] + 1
        new = [name, accno, bal, fd]
        self.data.append(new)
        print("Name: ", name)
        print("AccNo: ", accno)
        print("Balance: ", bal)
        print("Fixed Dep: ", fd)
        print("Your Account Created")

    def deposit(self, accno, depamt):
        for i in self.data:
            if i[1] == accno:
                idx = self.data.index(i)
                break
        else:
            print("Invalid Account No.")
            return

        if depamt > 100000:
            pan = input("Enter Pan No.: ")
            if len(pan) != 5:
                print("Invalid Pan")
                return

        self.data[idx][2] += depamt
        print("Your Balance: ", self.data[idx][2])
        self.transactions.append({
            "AccNo": accno,
            "Transaction Type": "Deposit",
            "Amount": depamt
        })

    def withdraw(self, accno, witamt):
        for i in self.data:
            if i[1] == accno:
                idx = self.data.index(i)
                break
        else:
            print("Invalid Account No.")
            return

        if witamt > self.data[idx][2]:
            print("Insufficient Fund.")
        else:
            self.data[idx][2] -= witamt
            print("Your Balance: ", self.data[idx][2])
            self.transactions.append({
                "AccNo": accno,
                "Transaction Type": "Withdraw",
                "Amount": witamt
            })

    def fd(self, accno, fdamt, yrs):
        for i in self.data:
            if i[1] == accno:
                idx = self.data.index(i)
                break
        else:
            print("Invalid Account No.")
            return

        if fdamt > 50000:
            rtn = (10000 * yrs) + self.data[idx][3]
            print("Your Return is: ", rtn)
        else:
            print("FD should be above Rs.50000.")

    def transaction(self):
        for trans in self.transactions:
            print(trans)
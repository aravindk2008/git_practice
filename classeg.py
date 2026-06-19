#!/usr/bin/env python3
class BankAccount:
	def __init__ (self, holder_name):
	        self.holder=holder_name
	        self.balance=0
	def deposit (self, amount):
	        self.balance += amount

	def withdraw (self, amount):
		if amount > self.balance:
			print("insufficient balance")
		else:
			self.balance -= amount
	def get_balance(self):
		return self.balance

acc1 = BankAccount("lee")
acc2 = BankAccount("wong")

acc1.deposit(5000)
acc1.withdraw(1500)

acc2.deposit(9000)
acc2.withdraw(4000)

acc2.withdraw(6000)

print("lee  Balance:", acc1.get_balance())
print("wong  Balance:", acc2.get_balance())


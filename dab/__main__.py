from dab.account import *

bank = [
  Account(1, "Jean", 275.30),
  Account(2, "Mathilde", 7530.00),
  Account(3, "George", 52.60)
]

print("Welcome to PyBank!")

number = input("Enter your account number: ")
account = bank.index(Account(number))
account = bank[account]
operation = int(input("How can we help you today? (type '0' to show your current balance, '-amount' to withdraw <amount> € or '+amount' to deposit <amount> €) "))

if operation == 0:
  print(account)
elif operation > 0:
  account.deposit(operation)
elif operation < 0:
  account.withdraw(operation)
else:
  print("Invalid operation", file=sys.stderr)
  sys.exit(1)

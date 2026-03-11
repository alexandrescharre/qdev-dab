class Account:
  def __init__(self, number, client, initial_balance):
    self.number = number
    self.client = client
    self.balance = initial_balance

  def __str__(self):
    return f"Account {self.number}:\n  - holder: {self.client}\n  - balance: {self.balance}\n"

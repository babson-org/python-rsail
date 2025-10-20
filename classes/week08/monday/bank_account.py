class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return f"Account({self.owner}, balance={self.balance})"

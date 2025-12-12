
import time
def portfolio_add_cash(self, amount: float):
    """TODO:
    - Reject negative amounts
    - Otherwise add to self.cash
    - Print message showing how much cash added and what you new cash balance is
    - return not needed
    """
    if amount < 0:
        print("you can't add negative cash")
        time.sleep(1)

    else:
        self.cash += amount
        print(f"You added ${amount:,.2f} and now have ${self.cash:,.2f} on hand ")
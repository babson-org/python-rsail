
import time
def portfolio_add_cash(self, amount: float):
    """TODO:
    - Reject negative amounts
    - Otherwise add to self.cash
    - Return new balance or None
    """
    if amount < 0:
       print('You canh not add negative cash') 
       time.sleep(1)
       return None
    else:
        self.cash += amount
        print(f"You have successfully added ${amount:,.2f} and now have ${self.cash:,.2f} on hand")
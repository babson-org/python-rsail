
import time
import prices as _prices

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_sell_stock(self, sym: str, shares: float, price: float):
    """TODO:
    - Ensure symbol exists
    - Ensure shares <= owned
    - Fetch last-close price
    - Reduce position shares; adjust running 'cost' proportionally
    - Remove the position if shares drop to 0
    - Increase self.cash by proceeds
    """
    
    current_position = _find_position(self, sym)
    if not current_position:
        print('You can not sell short!!')
        time.sleep(1)
      
    elif current_position['shares'] < shares:
        print(f"You can only sell {current_position['shares']:,.0f}")
        time.sleep(1)

    else:
        current_position['shares'] -= shares
        current_position['cost'] -= shares * price
        self.cash += shares * price

    return
       

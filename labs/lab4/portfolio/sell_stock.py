
import time
import prices as _prices

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_sell_stock(self, sym: str, shares: float, price: float):
    """TODO:
    - Ensure symbol exists (use _find_position())
    - Ensure shares <= owned
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to sell shares)
    - Reduce position shares; adjust  'cost' proportionally by shares. (assumes average cost accounting)
    - Remove the position if shares drop to 0
    - Increase self.cash by proceeds
    - Hint: the amount you reduce cost is NOT the same as the amount you increase cash
    """
    while True:
        sym = sym.upper()
        pos = _find_position(self, sym)
        if pos: break
        else: sym = input("ticker not found in portfolio, enter ticker: ")

    while True:
        if pos['shares'] < shares:
            print(f"You only have {pos['shares']} to sell")
            shares = int(input('Enter shares to sell: '))
        else: break
        
    
    cost_per_share = pos['cost'] / pos['shares']
    pos['cost'] -= cost_per_share * shares
    pos['shares'] -= shares
    self.cash += round(shares * price, 2)
    return
       


from .stock import Stock
import prices as _prices
import time

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_buy_stock(self, sym: str, shares: float, price: float):
    """TODO:    
    - Validate sym in DOW30
         In the lab4 folder is a file prices.py.  Look at the file and find out what DOW30 is
         You can access DOW30 with _prices.DOW30 (see how we import prices above)
    - Validate shares > 0
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to buy shares)
    - Make sure the client has enough cash to make the purchase (price * shares)

    - IMPORTANT: in self.positions there should only be one dictionary per symbol

    - Add the purchase to an existing position or create a new position in self.positions 
    - Be sure to decrease the client cash attribute
    NOTE: UI prompts are handled in main.py: this method only prints for invalid ticker and insufficient funds. The rest are handled in main.py
    """
    sym = sym.upper()
    if sym in _prices.DOW30:
        print(f'{sym} was found')
        not_found = False
    else:
        print(f'{sym} was NOT found')    # will never execute
        not_found = True
    time.sleep(2)
    
    
    

    
    if self.cash < price * shares: 
        max_shares = self.cash // price

        while True:
            print(f'You have insufficient funds to purchase {shares} of {sym}')
            print(f'The maximum number of shares you can buy is {max_shares}')
            shares = int(input('How many shares would you like to buy?'))
            if shares < max_shares or shares == 0: break


    position = _find_position(self, sym)
    
    if position:
        position['shares'] += shares
        position['cost']  += price * shares
    else:
        position = {'sym':sym,'name':sym,'shares':shares,'cost': round(price * shares, 2)}
        self.positions.append(position)

    self.cash -= round(price * shares,2)


    

    return




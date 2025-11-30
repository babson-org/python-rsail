

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
    - Validate shares > 0
    - Fetch last-close price via _prices.get_last_close_map([sym])
    - Compute cost_add = price * shares; ensure self.cash >= cost_add
    - Update/append position dicts with avg-cost model (running total in 'cost')
    - Decrease self.cash
    NOTE: UI prompts are handled in main.py: this method only prints for invalid ticker and insufficient funds. The rest are handled in main.py
    """
    
    if sym not in _prices.DOW30:
        print('Invalid ticker, not in Dow 30')
        time.sleep(1)
        return    
    
    if price * shares > self.cash:
        print(f"You only have {self.cash:,.2f} and need ${price * shares:,.2f} to make this purchase")
        time.sleep(1)
        return
    
    current_position = _find_position(self, sym)
    if current_position:
        current_position['shares'] += shares
        current_position['cost'] += shares * price
    else:
        self.positions.append({
                                "sym": sym,
                                "name": sym,
                                "shares": shares,
                                "cost": shares * price
                            })
        
    self.cash -= shares * price
    
    return




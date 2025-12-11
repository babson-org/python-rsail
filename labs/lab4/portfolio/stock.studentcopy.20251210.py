
class Stock:
    def __init__(self, sym, name, shares=0.0, cost=0.0):
        """TODO:"""
        self.sym = sym
        self.name = name
        self.shares = shares
        self.cost = cost
        
       

    def __str__(self):
        """TODO: include symbol, shares, and cost (format flexible)."""
        
        return f"You have {self.shares} shares of {self.sym} at a cost of ${self.cost:,.2f}"
        
        
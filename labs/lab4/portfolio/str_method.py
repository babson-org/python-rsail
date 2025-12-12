
def portfolio_str(self):
    """TODO: return a readable summary string. self is a Portfolio
    Example (format is flexible):
        "Bob has 2 positions and $1,234.56"
    """
    return f"{self.name} has {len(self.positions)} and ${self.cash:,.2f} on hand"

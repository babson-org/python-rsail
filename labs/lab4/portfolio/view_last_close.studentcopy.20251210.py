import prices as _prices

def portfolio_view_last_close(self):
    """
    Returns: dict mapping symbol -> last-close price (for tests).
    Printing is handled in main via a shared renderer.
    """
    syms = [pos["sym"] for pos in self.positions]
    px_map = _prices.get_last_close_map(syms)
    return px_map

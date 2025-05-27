class Order:
    def __init__(self, sender, side, price):
        self.sender = sender
        if side not in ("bid", "ask"):
            raise ValueError(f"Order.side must be 'bid' or 'ask', got {side}")
        self.side = side
        self.price = price

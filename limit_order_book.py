from collections import deque
from sortedcontainers import SortedDict

class BookHalf:
    def __init__(self, side):
        self.side = side
        self.price_levels = SortedDict()

    def add_order(self, order):
        lvl = self.price_levels.setdefault(order.price, deque())
        lvl.append(order)

    def del_order(self, order):
        lvl = self.price_levels[order.price]
        lvl.remove(order)
        if not lvl:
            del self.price_levels[order.price]

    def best_order(self):
        if self.price_levels:
            if self.side == "bid":
                return self.price_levels.peekitem(-1)[0]
            else:
                return self.price_levels.peekitem(0)[0]
        return None

class LimitOrderBook:
    def __init__(self):
        self.bids = BookHalf("bid")
        self.asks = BookHalf("ask")

    def add_order(self, order):
        if order.side == "bid":
            self.bids.add_order(order)
        else:
            self.asks.add_order(order)

    def del_order(self, order):
        if order.side == "bid":
            self.bids.del_order(order)
        else:
            self.asks.del_order(order)
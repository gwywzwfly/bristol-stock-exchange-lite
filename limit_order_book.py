import heapq
from collections import deque, defaultdict

class BookHalf:
    def __init__(self, side):
        self.side = side
        self.price_levels = defaultdict(deque)
        self.snapshot = defaultdict(int)
        self.price_heap = []
        self.best_price = None

    def add_order(self, order):
        self.price_levels[order.price].append(order)
        self.snapshot[order.price] += 1
        if self.snapshot[order.price] == 1:
            priority = -order.price if self.side == "bid" else order.price
            heapq.heappush(self.price_heap, priority)
        self._update_best_price()

    def del_order(self, order):
        if order.price in self.price_levels:
            try:
                self.price_levels[order.price].remove(order)
                self.snapshot[order.price] -= 1
                if self.snapshot[order.price] == 0:
                    del self.price_levels[order.price]
                    del self.snapshot[order.price]
                    self._update_best_price()
            except ValueError:
                pass

    def _update_best_price(self):
        while self.price_heap:
            candidate = -self.price_heap[0] if self.side == "bid" else self.price_heap[0]
            if self.snapshot.get(candidate) > 0:
                self.best_price = candidate
                break
            else:
                heapq.heappop(self.price_heap)
        else:
            self.best_price = None

    def best_order(self):
        return self.price_levels[self.best_price][0]

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
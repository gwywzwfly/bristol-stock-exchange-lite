import heapq
from collections import defaultdict, deque

class LOBHalf:
    def __init__(self, side):
        self.side = side
        self.price_levels = defaultdict(deque)
        self.price_heap = []

    def add_order(self, order):
        lvl = self.price_levels[order.price]
        if not lvl:
            heap_key = -order.price if self.side == "bid" else order.price
            heapq.heappush(self.price_heap, heap_key)
        lvl.append(order)

    def del_order(self, order):
        lvl = self.price_levels[order.price]
        lvl.remove(order)
        if not lvl:
            del self.price_levels[order.price]

    def best_price(self):
        while self.price_heap:
            price = -self.price_heap[0] if self.side == "bid" else self.price_heap[0]
            if price in self.price_levels:
                return price
            heapq.heappop(self.price_heap)
        return None
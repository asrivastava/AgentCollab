# seller.py

class SellerAgent:
    def __init__(self):
        self.current_ask = 105
        self.decrement = 1
        self.min_price = 100

    def respond(self, buyer_offer):
        # If buyer meets or exceeds minimum acceptable price → accept
        if buyer_offer >= self.min_price:
            return {"action": "accept", "price": buyer_offer}

        # Otherwise counter with a slightly lower ask
        next_ask = self.current_ask - self.decrement

        # If lowering further violates minimum → walk away
        if next_ask < self.min_price:
            return {"action": "walk_away"}

        self.current_ask = next_ask
        return {"action": "counter", "price": next_ask}


if __name__ == "__main__":
    seller = SellerAgent()
    result = seller.respond(98)
    print("Seller Agent Output:", result)

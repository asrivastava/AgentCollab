# buyer.py

class BuyerAgent:
    def __init__(self):
        self.current_offer = 98
        self.increment = 1
        self.max_price = 102

    def make_offer(self):
        if self.current_offer > self.max_price:
            return {"action": "walk_away"}

        offer = {
            "action": "offer",
            "price": self.current_offer
        }

        # prepare next offer for future rounds
        self.current_offer += self.increment
        return offer


if __name__ == "__main__":
    buyer = BuyerAgent()
    result = buyer.make_offer()
    print("Buyer Agent Output:", result)

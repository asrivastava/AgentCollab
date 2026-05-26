# logic.py

class SellerLogic:
    def __init__(self):
        self.last_offer = None
        self.minimum_price = 80  # Seller won't go below this

    def respond_to_offer(self, buyer_offer: float):
        """
        Basic seller negotiation logic.
        """
        self.last_offer = buyer_offer

        if buyer_offer < self.minimum_price:
            counter = max(self.minimum_price, buyer_offer + 10)
            return {
                "accepted": False,
                "counter_offer": counter,
                "message": f"Your offer of {buyer_offer} is too low. I can do {counter}."
            }

        return {
            "accepted": True,
            "counter_offer": buyer_offer,
            "message": f"Deal! I accept your offer of {buyer_offer}."
        }

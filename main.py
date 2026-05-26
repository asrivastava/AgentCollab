# main.py

from buyer import BuyerAgent
from seller import SellerAgent

def run_negotiation():
    buyer = BuyerAgent()
    seller = SellerAgent()

    print("Starting Buyer ↔ Seller negotiation...\n")

    buyer_offer = buyer.make_offer()
    print("Buyer:", buyer_offer)

    # If buyer walked away immediately
    if buyer_offer["action"] != "offer":
        print("Negotiation ended immediately.")
        return

    # Seller responds directly to buyer
    seller_reply = seller.respond(buyer_offer["price"])
    print("Seller:", seller_reply)

    # If seller accepts or walks away
    if seller_reply["action"] != "counter":
        print("Negotiation ended.")
        return

    # Buyer responds directly to seller
    buyer_reply = buyer.make_offer()
    print("Buyer:", buyer_reply)

    print("\nDone. This is the simplest direct interaction.")


if __name__ == "__main__":
    run_negotiation()
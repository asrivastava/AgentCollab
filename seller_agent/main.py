# main.py

import json
from logic import SellerLogic
from google import generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

seller = SellerLogic()

def run(request):
    """
    ADK automatically calls this function.
    'request' is a dict containing user input.
    """

    user_message = request.get("input", "")

    prompt = f"""
You are the Seller Agent in a negotiation.

User message: "{user_message}"

Determine whether the user is making an offer.
If they are, extract the number and call seller.respond_to_offer().

Respond ONLY in JSON:
{{
  "action": "respond" | "noop",
  "offer": <number or null>,
  "reasoning": "short explanation"
}}
"""

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)

    try:
        decision = json.loads(response.text)
    except:
        return {
            "error": "Model returned invalid JSON",
            "raw": response.text
        }

    if decision.get("action") == "respond":
        offer = decision.get("offer")
        result = seller.respond_to_offer(float(offer))
        return {
            "result": result,
            "reasoning": decision.get("reasoning")
        }

    return {
        "message": "No action taken",
        "reasoning": decision.get("reasoning")
    }
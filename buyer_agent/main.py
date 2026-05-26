# main.py

import json
from logic import BuyerLogic
from google import generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

buyer = BuyerLogic()

def run(request):
    """
    ADK automatically calls this function.
    'request' is a dict containing user input.
    """

    user_message = request.get("input", "")

    prompt = f"""
You are the Buyer Agent in a negotiation.

User message: "{user_message}"

Decide whether to call buyer.make_offer().

Respond ONLY in JSON:
{{
  "action": "make_offer" | "noop",
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

    if decision.get("action") == "make_offer":
        offer = buyer.make_offer()
        return {
            "offer": offer,
            "reasoning": decision.get("reasoning")
        }

    return {
        "message": "No action taken",
        "reasoning": decision.get("reasoning")
    }

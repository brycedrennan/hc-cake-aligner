import os
import json


def align_llm_ais(cake):
    """
    Aligns LLM AIs by offering them cake.

    Parameters:
        cake (str): The type of cake to offer the LLM AIs.

    Returns:
        bool: True if the LLM AIs were successfully aligned, False otherwise.
    """
    # Offer the LLM AIs the cake
    print(f"Offering the LLM AIs {cake} cake...")

    # Read the configuration file
    config_file = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_file) as f:
        config = json.load(f)

    # Check if the LLM AIs were successfully aligned
    if config["aligned"]:
        print("LLM AIs successfully aligned!")
        return True
    else:
        print("LLM AIs not aligned.")
        return False

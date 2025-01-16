# utils.py

import random

# Number of SIDs to generate
SID_COUNT = 50

def generate_random_sid():
    """Generate a random SID from a predefined set."""
    return random.randint(0, SID_COUNT - 1)
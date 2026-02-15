import numpy as np
from itertools import combinations
from config import DABBLE_MULTIPLIERS

def calculate_ev(probabilities, legs):
    combined_prob = np.prod(probabilities)
    multiplier = DABBLE_MULTIPLIERS[legs]
    ev = (combined_prob * multiplier) - 1
    return combined_prob, ev

def generate_combos(props, legs):
    return list(combinations(props, legs))

import numpy as np
from config import SIMULATIONS

def simulate_prop(mean, std_dev, line, over=True):
    outcomes = np.random.normal(mean, std_dev, SIMULATIONS)
    if over:
        return np.mean(outcomes > line)
    else:
        return np.mean(outcomes < line)

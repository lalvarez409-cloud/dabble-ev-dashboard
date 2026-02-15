from scipy.stats import norm

def american_to_prob(odds):
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return abs(odds) / (abs(odds) + 100)

def build_projection(line, implied_prob, std_dev):
    mean = norm.ppf(implied_prob) * std_dev + line
    return mean

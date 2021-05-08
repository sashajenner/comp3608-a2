import math

def sample_std(sums_squared, mu, n):
    return ((sums_squared / n - mu ** 2 / n) / (n - 1)) ** 0.5

def pnorm(x, mu, std):
    return (1 / (std * math.sqrt(2*math.pi))) * math.exp(-(x-mu)**2 / (2*std**2))

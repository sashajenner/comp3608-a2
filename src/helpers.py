import math

def pnorm(x, mu, std):
    return (1 / (std * math.sqrt(2*math.pi))) * math.exp(-(x-mu)**2 / (2*std**2))

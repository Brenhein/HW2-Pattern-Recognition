import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
import math

def plot_histo(data, mu, std):
    """Plots a histogram of the data points from the 1-d feature vector"""
    data = data["Values"]
    
    # Finds the bin range
    mini = min(data)
    maxi = max(data)
    ran = math.ceil(maxi) - math.floor(mini)
    binsize = ran // 2 + ran % 2
    plt.hist(data, bins=binsize, density=1)

    # Gets the pdf
    x = np.linspace(mini, maxi, binsize)  # the x-axis points
    p = norm.pdf(x, mu, std)  # the corresponding y points for the pdf
    plt.plot(x, p, 'k', linewidth=2)
    
    plt.xlabel("values")
    plt.ylabel("frequency")
    plt.title("Values Histogram")
  

def mean_histo(data):
    """Finds the mean and biased variance of the data points"""
    mu = data["Values"].mean()
    var = data["Values"].var(ddof=0)
    print("Mean:", mu)
    print("Variance:", var)
    return mu, var ** (1/2)
    

def main():
    fp = open("hw02_data01.txt")
    data = []
    for line in fp:
        data.append(float(line.strip()))  
    data = pd.DataFrame(data, columns=["Values"])
    
    mu, std = mean_histo(data)    
    plot_histo(data, mu, std)
    

if __name__ == "__main__":
    main()
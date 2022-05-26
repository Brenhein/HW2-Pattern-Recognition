import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import pprint as pp


def plot_pdf(d=None, df=False):
    """This function plots the pdfs
    of two different class conditional functions"""
    # Gets the point for the 2 pdfs
    x = np.linspace(0, 1, 100)
    w1 = [2-2*p for p in x]
    w2 = [2*p for p in x]
    
    # Plots the pdfs
    fig, ax = plt.subplots()
    ax.plot(x, w1, color='b', linewidth=2, label="p(x|\u03c91)")
    ax.plot(x, w2, color='y', linewidth=2, label="p(x|\u03c92)")
    ax.legend()
    
    # Plots a decison boundary
    if d is not None:
       ax.vlines(d, 0, 2, colors='k', linestyles='--') 
       
    # Plots the deciosin boundary function
    if df:
       for i in range(len(w1)):
           if w1[i] / w2[i] < 2:
               break
       b = x[i-1]
       ax.vlines(b, 0, 2, colors='k', linestyles='--')
    
    # Details figure
    ax.set_xlabel("x")
    ax.set_ylabel("p(x|\u03c9j)")
    ax.set_title("pdf Functions")
    

def main():
    plot_pdf()
    plot_pdf(d=.5)
    plot_pdf(df=True)

if __name__ == "__main__":
    main()
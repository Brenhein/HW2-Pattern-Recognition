import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def plot_pdf():
    """This function, given a mean and standard deviation, plots the 
    corrosponding pdf on the interval [10, 75]"""
    fig, ax = plt.subplots()
    mu1, mu2 = 50, 30
    std1, std2 = 5 ** (1 / 2), 10 ** (1 / 2)

    # Plot the 2 pdf functions
    x = np.linspace(10, 125, 115)
    pdf1 = norm.pdf(x, mu1, std1)
    pdf2 = norm.pdf(x, mu2, std2)
    ax.plot(x, pdf1, color='b', linewidth=2, label="\u03c91")
    ax.plot(x, pdf2, color='y', linewidth=2, label="\u03c92")
    ax.legend()
    ax.set_xlabel("x")
    ax.set_ylabel("p(x|\u03c9j)")
    ax.set_title("pdf Functions")


def plot_liklihood(t=False, t_val=0):
    """This fuction, given a mean and standard deviation, plots the 
    corrosponding liklihood functions on the interval [10, 75]"""
    fig, ax = plt.subplots()
    mu1, mu2 = 50, 30
    std1, std2 = 5 ** (1 / 2), 10 ** (1 / 2)
    x = np.linspace(10, 125, 115)

    # Finds pdfs
    pdf1 = list(norm.pdf(x, mu1, std1))
    pdf2 = list(norm.pdf(x, mu2, std2))

    # Finds the liklihood ratio for distributions
    like = []
    for i in range(len(pdf1)):
        like.append(pdf1[i] / pdf2[i])

    # Plots the liklihood ratio
    ax.plot(x, like, color='b', linewidth=2)
    ax.set_xlabel("x")
    ax.set_ylabel("p(x|\u03c91)/p(x|\u03c92)")
    ax.set_title("Likelihood Ratio Function")

    if t:
        ax.plot(x, [t_val for i in range(len(pdf1))], "--", color="k", linewidth=2)
        ax.set_ylim(0, 3)
        ax.set_xlim(39, 101)


def main():
    plot_pdf()
    plot_liklihood()
    plot_liklihood(True, 2)
    plot_liklihood(True, .5)


if __name__ == "__main__":
    main()

import scipy.stats as sp
import scipy.spatial as sc
import numpy as np


def calc_density(v, mu, covariance):
    """Calculates the density at a specific point"""
    d = sp.multivariate_normal.pdf(v, mu, covariance)
    print("density:", d)
    return d


def calc_euc(v1, v2, mu, covariance):
    """Calculates the eucidean distance between 2 points"""
    eud = sc.distance.euclidean(v1, v2)
    print("distance:", eud)
    return eud
    

def calc_mah(v1, v2, mu, covariance):
    """Calculates the mahalanobis distance on a gaussian distribution"""
    diff = [v2[i] - v1[i] for i in range(len(v1))]
    
    inv = np.linalg.inv(covariance)
    diff = np.array(diff)
    diff_t = np.array([[v] for v in diff])
    
    dist = np.dot(diff, inv)
    dist = np.dot(dist, diff_t)
    print("distance:", dist[0]**.5)
    return dist[0]
    

def main():
    covariance = [[1,0,0],
                  [0,5,2],
                  [0,2,5]]
    mu = (1,1,1)
    
    calc_density([0,0,0], mu, covariance)
    calc_density([5,5,5], mu, covariance)
    print()
    
    calc_euc([0,0,0], [5,5,5], mu, covariance)
    calc_mah([0,0,0], [5,5,5], mu, covariance)
    

if __name__ == "__main__":
    main()
import random
import math
from random import sample
import numpy as np
import scipy.stats as st
import statistics

def mean_main(a):
    x = np.mean(a)
    return x

def median_main(a):
    x = np.median(a)
    return x

def mode_main(a):
    x = statistics.mode(a)
    return x

def variance_main(a):
    x = statistics.variance(a)
    return x

def std_main(a):
    x = np.std(a)
    return x

def zscore_main(a):
    x = st.zscore(a)
    return x

def margin_of_error_main(n, z, t):
    x = (math.sqrt(n)/t)*z
    return x

def cochran_main(z, p, e):
    x = (z**2*p*(1-p))/e**2
    return x

class Calculator:
    result = 0

    def mean1(a):
        result = mean_main(a)
        return result

    def median1(a):
        result = median_main(a)
        return result

    def mode1(a):
        result = mode_main(a)
        return result

    def variance1(a):
        result = variance_main(a)
        return result

    def std1(a):
        result = std_main(a)
        return result

    def zscore(a):
        result = zscore_main(a)
        return result

    def margin_of_error(n, z, t):
        result = margin_of_error_main(n, z, t)
        return result

    def cochran(z, p, e):
        result = cochran_main(z, p, e)
        return result
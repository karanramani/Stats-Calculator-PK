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

class Calculator:
    result = 0

    def mean1(a):
        result = mean_main(a)
        return result

    def median1(a):
        result = median_main(a)
        return result
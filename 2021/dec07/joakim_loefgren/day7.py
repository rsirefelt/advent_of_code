from scipy.optimize import minimize_scalar
import numpy as np


def cost1(x_target, x_crabs):
    return np.sum(np.abs(x_crabs - x_target))


def cost2(x_target, x_crabs):
    diffs = np.abs(x_crabs - x_target)
    return np.sum(0.5*diffs*(diffs + 1))


if __name__ == '__main__':
    x_crabs = np.loadtxt('./input_day7.txt', delimiter=',',  dtype=int)
    bounds = np.array([0., np.max(x_crabs)])

    # Part I
    res = minimize_scalar(cost1, bounds=bounds, args=(x_crabs))
    print(int(np.min([cost1(np.floor(res.x), x_crabs), cost1(np.ceil(res.x), x_crabs)])))

    # Part II
    res = minimize_scalar(cost2, bounds=bounds, args=(x_crabs))
    print(int(np.min([cost2(np.floor(res.x), x_crabs), cost2(np.ceil(res.x), x_crabs)])))

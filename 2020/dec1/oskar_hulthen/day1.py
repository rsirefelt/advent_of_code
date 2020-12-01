from itertools import product, combinations
import pandas as pd
import numpy as np


def task(target, task_num=1):
    values = []
    with open("input") as f:
        for line in f:
            val = int(line)
            if val < target:
                values.append(val)

    df = pd.DataFrame(combinations(values, task_num + 1))
    df_sum = df.sum(axis=1)

    solution_index = df_sum[df_sum == target].index
    assert len(solution_index) >= 1
    solution_vals = list(df.iloc[solution_index[0]])

    print(np.prod(solution_vals))


if __name__ == "__main__":
    task(2020, 1)
    task(2020, 2)

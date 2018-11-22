import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # I ran the mem_analysis.py qq
    df = pd.read_csv('mem_usage.csv')
    # convert memory usage from B to MB
    df.rand_true = df.rand_true / 1048576
    df.rand_false = df.rand_false / 1048576
    grp = df.groupby('nbr_images').mean()

    plt.figure(figsize=(12, 9))
    grp.plot()
    plt.xlabel('Number of processed images')
    plt.ylabel('Memory Usage [MB]')
    plt.legend(['Random = True', 'Random = False'])
    plt.show()
    # plt.savefig('mem_usage.png')

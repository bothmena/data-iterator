from src.data_iterator import DataIterator
import matplotlib.pyplot as plt
import numpy as np

iterator = DataIterator('images.txt', random_order=True, run_forever=False, batch_size=6)
itr = iterator.iterate(150, 300)
i = 0
while i < 4:
    try:
        patches = next(itr)
        for patch in patches:
            patch = np.transpose(patch, (1, 2, 0))
            plt.imshow(patch)
            plt.show()
        i += 1
    except StopIteration:
        break

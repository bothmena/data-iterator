from src.data_iterator import DataIterator
import os
import psutil

process = psutil.Process(os.getpid())

iterator = DataIterator('images.txt', random_order=True, run_forever=True, batch_size=32)
itr = iterator.iterate()
i = 0
sum = 0
while i < 128:
    try:
        patches = next(itr)
        sum += patches.shape[0]
        i += 1
    except StopIteration:
        break

print(sum, 'images')
print(process.memory_info().rss)

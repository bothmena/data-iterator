import unittest
import numpy as np
from src.data_iterator import DataIterator
from src.data_processor import DataProcessor


class DataProcessorTest(unittest.TestCase):

    def test_output_patch(self):
        data_processor = DataProcessor()
        patch = data_processor.get_image_patch('/home/bothmena/Projects/PyCharm/DataIteration/dataset/3.jpg')
        self.assertEqual(type(patch), np.ndarray)
        self.assertEqual(patch.shape, (3, 512, 512))

    def test_output_patches(self):

        iterator = DataIterator('images.txt', random_order=False, run_forever=True, batch_size=32)
        itr = iterator.iterate()

        patches = next(itr)
        self.assertEqual(type(patches), np.ndarray)
        self.assertEqual(patches.shape, (32, 3, 512, 512))


if __name__ == '__main__':
    unittest.main()

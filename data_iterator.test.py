import unittest
import numpy as np
from src.data_iterator import DataIterator


class DataIteratorTest(unittest.TestCase):

    def test_unique_image_per_epoch_random(self):

        iterator = DataIterator('images.txt', random_order=True, run_forever=True, batch_size=32)
        itr = iterator.iterate()
        paths = []
        i = 0
        while i < 4:
            try:
                patches = next(itr)
                if type(patches) == np.ndarray:
                    raise Exception('Please modify the data_processor file so it returns a list of image paths')

                for path in patches:

                    """ because in the dataset we only have 40 unique images """
                    if len(paths) == 40:
                        paths = []

                    self.assertNotIn(path, paths, 'This path is duplicated!')
                    paths.append(path)
                i += 1
            except StopIteration:
                break

    def test_unique_image_per_epoch_not_random(self):

        iterator = DataIterator('images.txt', random_order=False, run_forever=True, batch_size=32)
        itr = iterator.iterate()
        paths = []
        i = 0
        while i < 4:
            try:
                patches = next(itr)
                if type(patches) == np.ndarray:
                    raise Exception('Please modify the data_processor file so it returns a list of image paths')

                for path in patches:

                    """ because in the dataset we only have 40 unique images """
                    if len(paths) == 40:
                        paths = []

                    self.assertNotIn(path, paths, 'This path is duplicated!')
                    paths.append(path)
                i += 1
            except StopIteration:
                break

    def test_different_epoch_image_order(self):

        iterator = DataIterator('images.txt', random_order=False, run_forever=True, batch_size=32)
        itr = iterator.iterate()
        epoch1 = []
        epoch2 = []
        while len(epoch2) < 40:
            patches = next(itr)
            if type(patches) == np.ndarray:
                raise Exception('Please modify the data_processor file so it returns a list of image paths')

            for path in patches:

                """ because in the dataset we only have 40 unique images """
                if len(epoch1) == 40:
                    epoch2.append(path)
                else:
                    epoch1.append(path)

        self.assertNotEqual(epoch1, epoch2)

    def test_randomness(self):
        ordered_paths = []
        for i in range(1, 41):
            ordered_paths.append('/home/bothmena/Projects/PyCharm/DataIteration/dataset/{}.jpg'.format(i))

        iterator = DataIterator('images.txt', random_order=True, run_forever=True, batch_size=32)
        itr = iterator.iterate()
        paths = []
        i = 0
        while len(paths) < 40:
            patches = next(itr)
            if type(patches) == np.ndarray:
                raise Exception('Please modify the data_processor file so it returns a list of image paths')

            for path in patches:
                if len(paths) == 40:
                    self.assertEqual(len(paths), len(ordered_paths))
                    self.assertNotEqual(paths, ordered_paths)
                else:
                    paths.append(path)


if __name__ == '__main__':
    unittest.main()

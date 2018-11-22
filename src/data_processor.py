import numpy as np
import matplotlib.pyplot as plt
import random


class DataProcessor:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_image_patches(self, image_paths):

        # Uncomment the next line when you are testing the DataIterator class.
        # return image_paths
        patches = []
        for path in image_paths:
            patch = self.get_image_patch(path.rstrip("\n\r"))
            patches.append(patch)

        return np.array(patches)

    def get_image_patch(self, path):
        """
        randomly selects x and y the coordinates of the starting point of the patch.
        read the image as a numpy array
        change the array dimension from (height, width, 3) to (3, height, width)
        return a numpy array with the dimension: (3, height, width)
        """
        x, y = random.randint(0, 1080 - self.height), random.randint(0, 1920 - self.width)
        img = plt.imread(path)
        patch = img[x:x + self.height, y:y + self.width, :]
        return patch.transpose((-1, 0, 1))

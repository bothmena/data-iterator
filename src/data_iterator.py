from random import shuffle
from src.data_processor import DataProcessor


class DataIterator:

    def __init__(self, filename, random_order=False, run_forever=False, batch_size=6):
        self.filename = filename
        self.random_order = random_order
        self.run_forever = run_forever
        self.batch_size = batch_size

    def get_image_paths(self):
        """
        This function reads the file and return a list of image paths.
        in case random_order == True, the function shuffles the list.
        """
        with open(self.filename, 'r') as images_file:
            image_paths = images_file.readlines()
            if self.random_order:
                shuffle(image_paths)
            return image_paths

    def iterate(self):
        """
        Loop through the image paths list and for every batch_size of images, it yields a numpy array
        with the dimension (batch_size, 3, height, width)
        height & width can be specified when creating a new instance of DataProcessor
        """
        paths = self.get_image_paths()
        processor = DataProcessor()
        if self.run_forever:
            while True:
                while len(paths) < self.batch_size:
                    paths += self.get_image_paths()

                yield processor.get_image_patches(paths[:self.batch_size])
                paths = paths[self.batch_size:]
        else:
            index = 0
            length = len(paths)
            while index < length:
                outer = min(length, index+self.batch_size)
                yield processor.get_image_patches(paths[index:outer])
                index = outer

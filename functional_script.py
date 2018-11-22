import sys
import numpy as np
import matplotlib.pyplot as plt
import random


def get_image_patches(image_paths):
    patches = []
    for path in image_paths:
        patch = get_image_patch(path.rstrip("\n\r"))
        patches.append(patch)

    return np.array(patches)


def get_image_patch(path):
    """
    randomly selects x and y the coordinates of the starting point of the patch.
    read the image as a numpy array
    change the array dimension from (height, width, 3) to (3, height, width)
    return a numpy array with the dimension: (3, height, width)

    N.B. random.randint: generates random numbers using as uniform distribution.
    """
    x, y = random.randint(0, 1080 - 512), random.randint(0, 1920 - 512)
    img = plt.imread(path)
    patch = img[x:x + 512, y:y + 512, :]
    return patch.transpose((-1, 0, 1))


def get_image_paths(filename, random_order):
    """
    This function reads the file and return a list of image paths.
    in case random_order == True, the function shuffles the list.
    """
    with open(filename, 'r') as images_file:
        image_paths = images_file.readlines()
        if random_order:
            random.shuffle(image_paths)
        return image_paths


def iterate(filename, run_forever, random_order, batch_size=32):
    """
    Loop through the image paths list and for every batch_size of images, it yields a numpy array
    with the dimension (batch_size, 3, height, width)
    height & width can be specified when creating a new instance of DataProcessor
    """
    paths = get_image_paths(filename, random_order)
    if run_forever:
        while True:
            while len(paths) < batch_size:
                paths += get_image_paths(filename, random_order)

            yield get_image_patches(paths[:batch_size])
            paths = paths[batch_size:]
    else:
        index = 0
        length = len(paths)
        while index < length:
            outer = min(length, index + batch_size)
            yield get_image_patches(paths[index:outer])
            index = outer


if __name__ == '__main__':

    def is_bool(x):
        return x in ['0', '1']


    file = sys.argv[1]
    rand = False
    forever = False

    if len(sys.argv) > 2:
        if sys.argv[2] in ['0', '1']:
            rand = bool(int(sys.argv[2]))
        else:
            print('random_order argument if specified, should only be 0 or 1!')
            exit(1)

    if len(sys.argv) > 3:
        if sys.argv[3] in ['0', '1']:
            forever = bool(int(sys.argv[3]))
        else:
            print('run_forever argument if specified, should only be 0 or 1!')
            exit(2)

    try:
        with open(file, 'r') as f:
            pass
    except FileNotFoundError:
        print('Please provide a valid filename, the filename you gave does not exist!')
        exit(3)

    print('starting the script with arguments:')
    print('\trandom_order = ', rand)
    print('\trun_forever = ', forever)

    itr = iterate(file, random_order=rand, run_forever=forever)
    # the i counter is needed to limit the iteration to 32 * 4 images in case of run_forever = True.
    i = 0
    while i < 4:
        try:
            patches = next(itr)
            for patch in patches:
                # show image using matplotlib, before that we need to transpose the patch to be (height, weight, color channels)
                patch = np.transpose(patch, (1, 2, 0))
                plt.imshow(patch)
                plt.show()
            i += 1
        except StopIteration:
            break

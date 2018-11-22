# data-iterator

### Functional solution: functional_script.py

you can run it using this command: python3 functional_script.py filename random_order run_forever
arguments: 
- filename: string: path of the file that contains the list of images paths.
- random_order: whether or not the images should be ordered. possible values: 0 or 1, default = False
- run_forever: whether or not the script should loope forever on the images. possible values: 0 or 1, default = False

### Object-Oriented solution

2 classes in src folder:
- DataIterator: read the content of the file containing the images paths, iterate over the images paths, return a generator 
of numpy array
- DataProcessor: reads images from disc as a numpy array, return a numpy array of size **(*batch_size*, 3, *height*, *width*)**.

Variables:
- Random order (*random_order*), default = False
- Run forever (*run_forever*), default = False
- Batch size (*batch_size*), default = 32
- Patch height (*height*), default = 512
- Patch width (*width*), default = 512

### Visualizing the results

in main.py script, I iterated through the images in the folder: **dataset**, which their paths are stored in the file 
**images.txt** and using matplotlib I visualized the images patches.

### Memory Usage Profiling

I ran the **mem_usage_analysis.py** multiple times increasing the number of processed images each time from 40 images to 4096.

The result are saved in the **mem_usage.csv** file. and it can be summarized in the next plot.

![alt text](https://raw.githubusercontent.com/bothmena/data-iterator/master/mem_usage.png "Memory usage profiling")

### Functional testing

because I wanted to make sure the code is doing what it is intended to do, I had to create some functional tests to:
- make sure images are only used once in every epoch
- in the case where run_forever and random_order are both True, the order of images should be different each time.
- test output patches dimension to be (32, 3, 512, 512), of type numpy.ndarray
- test single output patch dimension to be (3, 512, 512), of type numpy.ndarray

Test suites:
- **data_iterator.test.py**: before you run this file, you need to uncomment the 15th line in *src/data_processor.py*
- **data_processor.test.py**



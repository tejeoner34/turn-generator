"""
We create the generator function to be used in main file
"""


def infinite_generator():
    x = 0
    while True:
        x += 1
        yield x
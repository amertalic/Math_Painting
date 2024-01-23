import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width

        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):

        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
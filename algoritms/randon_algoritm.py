from random import randint
import numpy as np


def randon_algoritm(width, height, dimensions, pixel_values,init,finish):
    img_process = np.zeros((height, width, dimensions), dtype=np.uint8)
    for h in range(height):
        for w in range(width):
            pixel = list(pixel_values[width*h + w])
            value = randint(init, finish)
            pixel[0] += value
            pixel[1] += value
            pixel[2] += value
            if (pixel[0] > 255):
                pixel[0] = 255
            if (pixel[1] > 255):
                pixel[1] = 255
            if (pixel[2] > 255):
                pixel[2] = 255
            if (pixel[0] < 0):
                pixel[0] = 0
            if (pixel[1] < 0):
                pixel[1] = 0
            if (pixel[2] < 0):
                pixel[2] = 0
            img_process[h, w] = tuple(pixel)
    return img_process

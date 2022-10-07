from PIL import Image
import numpy as np


def calc_pixel_values(img):
    image_array = np.array(img, dtype=np.uint8)
    img_base = Image.fromarray(image_array)

    pixel_values = list(img_base.getdata())

    if (type(pixel_values[0]) != tuple):
        list_pixels = list()
        for i in pixel_values:
            list_pixels.append(tuple([i]))
        pixel_values = list_pixels
    return pixel_values

import numpy as np


def calc_rgb(width, height, pixel_values):
    sum_pixel_r = 0
    sum_pixel_g = 0
    sum_pixel_b = 0

    for h in range(height):
        for w in range(width):
            pixel = list(pixel_values[width*h + w])
            sum_pixel_r += pixel[0]
            sum_pixel_g += pixel[1]
            sum_pixel_b += pixel[2]

    r = sum_pixel_r/(width*height)
    g = sum_pixel_g/(width*height)
    b = sum_pixel_b/(width*height)
    return r, g, b

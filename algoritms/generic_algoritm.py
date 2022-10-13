import numpy as np
from algoritms.blue.blue_decrease import blue_decrease
from algoritms.blue.blue_plus import blue_plus
from algoritms.green.green_decrease import green_decrease
from algoritms.green.green_plus import green_plus
from algoritms.red.red_decrease import red_decrease

from algoritms.red.red_plus import red_plus
from calc_pixel_values import calc_pixel_values
from rgb_to_img import calc_rgb


def algoritm(width, height, dimensions, pixel_values, img):
    r, g, b = calc_rgb(width, height, pixel_values)
    r = r/(width*height)
    g = g/(width*height)
    b = b/(width*height)
    if (r > g and r > b):
        print("Red")
        img_process = red_plus(width, height, dimensions, calc_pixel_values(img), 70)
        img_process = green_decrease(width, height, dimensions, calc_pixel_values(img), 20)
        img_process = blue_decrease(width, height, dimensions, calc_pixel_values(img), 20)
    elif (b > g and b > r):
        print("Blue")
        img_process = blue_plus(width, height, dimensions, calc_pixel_values(img), 70)
        img_process = green_decrease(width, height, dimensions, calc_pixel_values(img), 20)
        img_process = red_decrease(width, height, dimensions, calc_pixel_values(img), 20)
    elif (g > b and g > r):
        print("Green")
        img_process = green_plus(width, height, dimensions, calc_pixel_values(img), 70)
        img_process = red_decrease(width, height, dimensions, calc_pixel_values(img), 20)
        img_process = blue_decrease(width, height, dimensions, calc_pixel_values(img), 20)
    else:
        print("sem dominancia")
        img_process = img

    return img_process

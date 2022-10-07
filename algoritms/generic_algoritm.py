import numpy as np
from algoritms.blue.blue_decrease import blue_decrease
from algoritms.blue.blue_plus import blue_plus
from algoritms.green.green_decrease import green_decrease
from algoritms.green.green_plus import green_plus
from algoritms.red.red_decrease import red_decrease

from algoritms.red.red_plus import red_plus
from calc_pixel_values import calc_pixel_values


def algoritm(width, height, dimensions, pixel_values, img):
    img_process = np.zeros((height, width, dimensions), dtype=np.uint8)

    sum_pixel_r = 0
    sum_pixel_g = 0
    sum_pixel_b = 0

    for h in range(height):
        for w in range(width):
            pixel = list(pixel_values[width*h + w])
            sum_pixel_r += pixel[0]
            sum_pixel_g += pixel[1]
            sum_pixel_b += pixel[2]

    red_pixel = sum_pixel_r/(width*height)
    green_pixel = sum_pixel_g/(width*height)
    blue_pixel = sum_pixel_b/(width*height)

    if( red_pixel > green_pixel and red_pixel > blue_pixel):
        print("Red")
        img_process = red_plus(width, height, dimensions, calc_pixel_values(img), 70)
        img_process = green_decrease(width, height, dimensions, calc_pixel_values(img), 20)
        img_process = blue_decrease(width, height, dimensions, calc_pixel_values(img), 20)
    elif( blue_pixel > green_pixel and blue_pixel > red_pixel):
        print("Blue")
        img_process = blue_plus(width, height, dimensions, calc_pixel_values(img), 70)
        img_process = green_decrease(width, height, dimensions, calc_pixel_values(img), 20)
        img_process = red_decrease(width, height, dimensions, calc_pixel_values(img), 20)
    elif( green_pixel > blue_pixel and green_pixel > red_pixel):
        print("Green")
        img_process = green_plus(width, height, dimensions, calc_pixel_values(img), 70)
        img_process = red_decrease(width, height, dimensions, calc_pixel_values(img), 20)
        img_process = blue_decrease(width, height, dimensions, calc_pixel_values(img), 20)
    else:
        print("sem dominancia")
        img_process = img

    return img_process

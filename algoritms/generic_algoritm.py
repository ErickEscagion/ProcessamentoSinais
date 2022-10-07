import numpy as np


def algoritm(width, height, dimensions, pixel_values):
    img_process = np.zeros((height, width, dimensions), dtype=np.uint8)

    for h in range(height):
        for w in range(width):
            pixel = list(pixel_values[width*h + w])

            if ((pixel[0] >= 200 and pixel[0] <= 255) and (pixel[1] >= 0 and pixel[1] <= 50) and (pixel[2] >= 0 and pixel[2] <= 50)):
                pixel[0] = pixel[0] - 100

            if ((pixel[0] >= 0 and pixel[0] <= 50) and (pixel[1] >= 200 and pixel[1] <= 255) and (pixel[2] >= 0 and pixel[2] <= 50)):
                pixel[1] = pixel[1] - 100

            if ((pixel[0] >= 0 and pixel[0] <= 50) and (pixel[1] >= 0 and pixel[1] <= 50) and (pixel[2] >= 200 and pixel[2] <= 255)):
                pixel[2] = pixel[2] - 100

            if ((pixel[0] >= 0 and pixel[0] <= 50) and (pixel[1] >= 50 and pixel[1] <= 100) and (pixel[2] >= 100 and pixel[2] <= 200)):
                pixel[2] = pixel[2] + 50

            img_process[h, w] = tuple(pixel)
    return img_process

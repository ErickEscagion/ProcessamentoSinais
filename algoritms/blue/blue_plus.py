import numpy as np


def blue_plus(width, height, dimensions, pixel_values, intensity):
    img_process = np.zeros((height, width, dimensions), dtype=np.uint8)

    for h in range(height):
        for w in range(width):
            pixel = list(pixel_values[width*h + w])

            if ((pixel[0] >= 0 and pixel[0] <= 100) and (pixel[1] >= 0 and pixel[1] <= 100) and (pixel[2] >= 100 and pixel[2] <= 255)):
                pixel[2] = pixel[2] + intensity
                if(pixel[2] > 255):
                    pixel[2] = 255

            img_process[h, w] = tuple(pixel)
    return img_process

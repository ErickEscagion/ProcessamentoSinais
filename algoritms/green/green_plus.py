import numpy as np


def green_plus(width, height, dimensions, pixel_values, intensity):
    img_process = np.zeros((height, width, dimensions), dtype=np.uint8)

    for h in range(height):
        for w in range(width):
            pixel = list(pixel_values[width*h + w])

            if ((pixel[0] >= 0 and pixel[0] <= 100) and (pixel[1] >= 100 and pixel[1] <= 255) and (pixel[2] >= 0 and pixel[2] <= 100)):
                pixel[1] = pixel[1] + intensity
                if (pixel[1] > 255):
                    pixel[1] = 255

            img_process[h, w] = tuple(pixel)
    return img_process

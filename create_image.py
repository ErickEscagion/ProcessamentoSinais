from PIL import Image
import numpy as np


def create_image():
    img = [
        [
            [255, 255, 255], [255, 255, 255], [255, 255, 255]
        ],
        [
            [255, 0, 0], [255, 0, 0], [255, 0, 0]
        ],
        [
            [0, 255, 0], [0, 255, 0], [0, 255, 0]
        ],
        [
            [0, 0, 255], [0, 0, 255], [0, 0, 255]
        ],
        [
            [0, 0, 0], [0, 0, 0], [0, 0, 0]
        ]
    ]
    image_array = np.array(img, dtype=np.uint8)
    img_base = Image.fromarray(image_array)
    return img_base

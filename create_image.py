from PIL import Image
import numpy as np


def create_image():
    img = [
        # white
        [
            [255, 255, 255], [255, 255, 255], [255, 255, 255]
        ],
        # yellow
        [
            [255, 255, 0], [255, 255, 0], [255, 255, 0]
        ],
        # pink
        [
            [255, 0, 255], [255, 0, 255], [255, 0, 255]
        ],
        # cian
        [
            [0, 255, 255], [0, 255, 255], [0, 255, 255]
        ],
        # red
        [
            [255, 0, 0], [255, 0, 0], [255, 0, 0]
        ],
        # blue
        [
            [0, 0, 255], [0, 0, 255], [0, 0, 255]
        ],
        # green
        [
            [0, 255, 0], [0, 255, 0], [0, 255, 0]
        ],
        # black
        [
            [0, 0, 0], [0, 0, 0], [0, 0, 0]
        ]
    ]
    image_array = np.array(img, dtype=np.uint8)
    img_base = Image.fromarray(image_array)
    return img_base

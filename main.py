from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

img_base = Image.open("imgs/praia.jpg")
#img_base = Image.open("imgs/m.png")
#img_base = Image.open("imgs/perfil.jpg")
#img_base = Image.open("imgs/c.png")

#create image
"""
img = [
    [
        [255, 255, 255], [255, 255, 255],[255, 255, 255]
    ],
    [
        [255, 0, 0], [255, 0, 0],[255, 0, 0]
    ],
    [
        [0, 255, 0], [0, 255, 0],[0, 255, 0]
    ],
    [
        [0, 0, 255], [0, 0, 255],[0, 0, 255]
    ],
    [
        [0, 0, 0], [0, 0, 0],[0, 0, 0]
    ]
]
image_array = np.array(img, dtype=np.uint8)
img_base = Image.fromarray(image_array)
"""


width, height = img_base.size
pixel_values = list(img_base.getdata())
qtd_pixels = len(pixel_values)

if (type(pixel_values[0]) != tuple):
    list_pixels = list()
    for i in pixel_values:
        list_pixels.append(tuple([i]))
    pixel_values = list_pixels

dimensions = len(pixel_values[0])

print("----------------------------------------------------")
print("Width: ",  width, "\nHeigth: ", height)
print("Dimensoes: ", dimensions, "\nTotal Pixels: ", dimensions * qtd_pixels)
print("----------------------------------------------------")

img_process = np.zeros((height, width, dimensions), dtype=np.uint8)

## algoritimo para alterar a imagem
for h in range(height):
    for w in range(width):
        pixel = list(pixel_values[width*h + w])
        #print(pixel)
        if ((pixel[0] >= 200 and pixel[0] <= 255) and (pixel[1] >= 0 and pixel[1] <= 50) and (pixel[2] >= 0 and pixel[2] <= 50)):
            pixel[0] = pixel[0] - 100

        if ((pixel[0] >= 0 and pixel[0] <= 50) and (pixel[1] >= 200 and pixel[1] <= 255) and (pixel[2] >= 0 and pixel[2] <= 50)):
            pixel[1] = pixel[1] - 100

        if ((pixel[0] >= 0 and pixel[0] <= 50) and (pixel[1] >= 0 and pixel[1] <= 50) and (pixel[2] >= 200 and pixel[2] <= 255)):
            pixel[2] = pixel[2] - 100

        if ((pixel[0] >= 0 and pixel[0] <= 50) and (pixel[1] >= 50 and pixel[1] <= 100) and (pixel[2] >= 100 and pixel[2] <= 200)):
            pixel[2] = pixel[2] + 50

        img_process[h, w] = tuple(pixel)


f, axarr = plt.subplots(2)
axarr[0].imshow(img_base)
axarr[1].imshow(img_process)
plt.show()

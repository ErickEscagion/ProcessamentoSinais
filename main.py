from fileinput import hook_encoded
from venv import create
from matplotlib import pyplot as plt
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


def informations_to_image(img):
    width, height = img.size
    pixel_values = calc_pixel_values(img)
    qtd_pixels = len(pixel_values)
    dimensions = len(pixel_values[0])
    """
    print("----------------------------------------------------")
    print("Width: ",  width, "\nHeigth: ", height)
    print("Dimensoes: ", dimensions, "\nTotal Pixels: ", dimensions * qtd_pixels)
    print("----------------------------------------------------")
    """
    return width, height, dimensions, pixel_values


def algoritm(width, height, dimensions, pixel_values):
    img_process = np.zeros((height, width, dimensions), dtype=np.uint8)
    # algoritimo para alterar a imagem
    for h in range(height):
        for w in range(width):
            pixel = list(pixel_values[width*h + w])
            # print(pixel)
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


def algoritm2(width, height, dimensions, pixel_values):
    img_process = np.zeros((height, width, dimensions), dtype=np.uint8)
    # algoritimo para alterar a imagem
    for h in range(height):
        for w in range(width):
            pixel = list(pixel_values[width*h + w])
            # print(pixel)
            if ((pixel[0] >= 101 and pixel[0] <= 255)):
                pixel[0] = pixel[0] - 100

            img_process[h, w] = tuple(pixel)
    return img_process


def main():
    #img_base = Image.open("imgs/praia.jpg")
    #img_base = Image.open("imgs/m.png")
    #img_base = Image.open("imgs/perfil.jpg")
    #img_base = Image.open("imgs/c.png")
    img_base = create_image()
    img = img_base
    img_process = img_base
    width, height, dimensions, pixel_values = informations_to_image(img_base)
    x = 0
    while (x != 8):
        f, axarr = plt.subplots(2)
        img = img_process
        print("Menu:\n1)Azul +\n2)Azul -\n3)Amarelo +\n4)Amarelo -\n5)Vermelho +\n6)Vermelho -\n7)Generico \n8)Sair")
        x = int(input("Digite a função desejada: "))
        if (x == 1):
            print("Algoritmo Azul +")
            img_process = algoritm(width, height, dimensions, calc_pixel_values(img))
        elif (x == 2):
            print("Algoritmo Azul -")
            img_process = algoritm2(width, height, dimensions, calc_pixel_values(img))
        elif (x == 3):
            print("Algoritmo Amarelo +")
        elif (x == 4):
            print("Algoritmo Amarelo -")
        elif (x == 5):
            print("Algoritmo Vermelho +")
        elif (x == 6):
            print("Algoritmo Vermelho -")
        elif (x == 7):
            print("O Algoritmo!")
            
        if (x == 8):
            print("Obrigado por utilizar nosso algoritmo!")
            axarr[0].imshow(img_base)
            axarr[1].imshow(img_process)
            plt.show()
        elif (x > 0 and x < 9):
            axarr[0].imshow(img)
            axarr[1].imshow(img_process)
            plt.show()
        else:
            print("-------------------\nFunção invalida!")


if __name__ == "__main__":
    main()

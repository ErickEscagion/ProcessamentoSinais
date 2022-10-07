from matplotlib import pyplot as plt
from calc_pixel_values import calc_pixel_values
from create_image import create_image
from algoritms.generic_algoritm import algoritm
from informations_to_image import informations_to_image
from PIL import Image

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
        img = img_process
        print("Menu:\n1)Azul +\n2)Azul -\n3)Amarelo +\n4)Amarelo -\n5)Vermelho +\n6)Vermelho -\n7)Generico \n8)Sair")
        x = int(input("Digite a função desejada: "))
        if (x == 1):
            print("Algoritmo Azul +")
        elif (x == 2):
            print("Algoritmo Azul -")
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
            img_process = algoritm(width, height, dimensions, calc_pixel_values(img))
            
        if (x == 8):
            f, axarr = plt.subplots(2)
            print("Obrigado por utilizar nosso algoritmo!")
            axarr[0].imshow(img_base)
            axarr[1].imshow(img_process)
            plt.show()
        elif (x > 0 and x < 9):
            f, axarr = plt.subplots(3)
            axarr[0].imshow(img_base)
            axarr[1].imshow(img)
            axarr[2].imshow(img_process)
            plt.show()
        else:
            print("-------------------\nFunção invalida!")


if __name__ == "__main__":
    main()

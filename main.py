from PIL import Image
from matplotlib import pyplot as plt
from calc_pixel_values import calc_pixel_values
from create_image import create_image
from informations_to_image import informations_to_image
from algoritms.generic_algoritm import algoritm
from algoritms.blue.blue_decrease import blue_decrease
from algoritms.blue.blue_plus import blue_plus
from algoritms.red.red_decrease import red_decrease
from algoritms.red.red_plus import red_plus
from algoritms.green.green_decrease import green_decrease
from algoritms.green.green_plus import green_plus

def main():
    #img_base = Image.open("imgs/praia.jpg")
    #img_base = Image.open("imgs/perfil.jpg")
    #img_base = Image.open("imgs/campo.jpg")
    img_base = Image.open("imgs/campoAgua.jpg")
    #img_base = create_image()
    #img_base = Image.open("imgs/florestaVermelha.jpg")

    img = img_base
    img_process = img_base
    width, height, dimensions, pixel_values = informations_to_image(img_base)
    x = 100
    while (x != 0):
        img = img_process
        print("Menu:\n0)Sair\n1)Azul +\n2)Azul -\n3)Amarelo +\n4)Amarelo -\n5)Vermelho +\n6)Vermelho -\n7)Azul ++\n8)Azul --\n9)Amarelo ++\n10)Amarelo --\n11)Vermelho ++\n12)Vermelho --\n13)Generico")
        x = int(input("Digite a função desejada: "))
        if (x == 1):
            img_process = blue_plus(width, height, dimensions, calc_pixel_values(img), 20)
        elif (x == 2):
            img_process = blue_decrease(width, height, dimensions, calc_pixel_values(img), 20)
        elif (x == 3):
            img_process = green_plus(width, height, dimensions, calc_pixel_values(img), 20)
        elif (x == 4):
            img_process = green_decrease(width, height, dimensions, calc_pixel_values(img), 20)
        elif (x == 5):
            img_process = red_plus(width, height, dimensions, calc_pixel_values(img), 20)
        elif (x == 6):
            img_process = red_decrease(width, height, dimensions, calc_pixel_values(img), 20)
        elif (x == 7):
            img_process = blue_plus(width, height, dimensions, calc_pixel_values(img), 50)
        elif (x == 8):
            img_process = blue_decrease(width, height, dimensions, calc_pixel_values(img), 50)
        elif (x == 9):
            img_process = green_plus(width, height, dimensions, calc_pixel_values(img), 50)
        elif (x == 10):
            img_process = green_decrease(width, height, dimensions, calc_pixel_values(img), 50)
        elif (x == 11):
            img_process = red_plus(width, height, dimensions, calc_pixel_values(img), 50)
        elif (x == 12):
            img_process = red_decrease(width, height, dimensions, calc_pixel_values(img), 50)
        elif (x == 13):
            img_process = algoritm(width, height, dimensions, calc_pixel_values(img), img)

        if (x == 0):
            f, axarr = plt.subplots(2)
            print("Obrigado por utilizar nosso algoritmo!")
            axarr[0].imshow(img_base)
            axarr[0].title.set_text('Figura Inicial')
            axarr[0].axis('off')
            axarr[1].imshow(img_process)
            axarr[1].title.set_text('Figura Processada')
            axarr[1].axis('off')
            plt.show()
        elif (x >= 0 and x <= 13):
            f, axarr = plt.subplots(3)
            
            axarr[0].imshow(img_base)
            axarr[0].title.set_text('Figura Inicial')
            axarr[0].axis('off')
            axarr[1].imshow(img)
            axarr[1].title.set_text('Figura Em Processamento')
            axarr[1].axis('off')
            axarr[2].imshow(img_process)
            axarr[2].title.set_text('Figura Processada')
            axarr[2].axis('off')
            plt.show()
        else:
            print("-------------------\nFunção invalida!")


if __name__ == "__main__":
    main()

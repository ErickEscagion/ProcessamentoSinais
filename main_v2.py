from PIL import Image
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from algoritms.randon_algoritm import randon_algoritm
from calc_pixel_values import calc_pixel_values
from create_image import create_image
from informations_to_image import informations_to_image
from algoritms.blue.blue_plus import blue_plus
from algoritms.red.red_plus import red_plus
from algoritms.green.green_plus import green_plus
from results import generate_graph_results
from rgb_to_img import calc_rgb
from graph_to_img import generate_graph


def main():
    #img_base = Image.open("Imagens/1/base.jpg")
    #img_base = Image.open("Imagens/2/base.jpg")
    #img_base = Image.open("Imagens/3/base.jpg")
    img_base = Image.open("Imagens/4/base.jpg")
    #img_base = Image.open("Imagens/5/base.jpg")
    # img_base = Image.open("imgs/perfil.jpg")
    # img_base = Image.open("imgs/campo.jpg")
    # img_base = Image.open("imgs/campoAgua.jpg")
    # img_base = Image.open("imgs/florestaVermelha.jpg")
    # img_base = create_image()
    width, height, dimensions, pixel_values = informations_to_image(img_base)

    img_blue = blue_plus(width, height, dimensions, calc_pixel_values(randon_algoritm(
        width, height, dimensions, calc_pixel_values(blue_plus(
            width, height, dimensions, calc_pixel_values(randon_algoritm(
                width, height, dimensions, calc_pixel_values(img_base), 0, 20)), 70)), -2, 2)), 50)

    img_red = red_plus(
        width, height, dimensions, calc_pixel_values(randon_algoritm(
            width, height, dimensions, calc_pixel_values(red_plus(
                width, height, dimensions, calc_pixel_values(randon_algoritm(
                    width, height, dimensions, calc_pixel_values(img_base), 0, 20)), 70)), -2, 2)), 50)
    img_green = green_plus(
        width, height, dimensions, calc_pixel_values(randon_algoritm(
            width, height, dimensions, calc_pixel_values(green_plus(
                width, height, dimensions, calc_pixel_values(randon_algoritm(
                    width, height, dimensions, calc_pixel_values(img_base), 0, 20)), 70)), -2, 2)), 50)

    im = Image.fromarray(img_blue)
    im.save("img_blue.png")

    im = Image.fromarray(img_red)
    im.save("img_red.png")

    im = Image.fromarray(img_green)
    im.save("img_green.png")

    generate_graph(img_base, "graf_img_base")
    generate_graph(img_blue, "graf_img_blue")
    generate_graph(img_red, "graf_img_red")
    generate_graph(img_green, "graf_img_green")

    r, g, b = calc_rgb(width, height, pixel_values)
    generate_graph_results(abs(r - r), abs(g - g), abs(b - b), "results_base")

    r_blue, g_blue, b_blue = calc_rgb(width, height, calc_pixel_values(img_blue))
    generate_graph_results(abs(r - r_blue), abs(g - g_blue), abs(b - b_blue), "results_blue")

    r_green, g_green, b_green = calc_rgb(width, height, calc_pixel_values(img_green))
    generate_graph_results(abs(r - r_green), abs(g - g_green), abs(b - b_green), "results_green")

    r_red, g_red, b_red = calc_rgb(width, height, calc_pixel_values(img_red))
    generate_graph_results(abs(r - r_red), abs(g - g_red), abs(b - b_red), "results_red")

    f, axarr = plt.subplots(4, 3)

    print("Obrigado por utilizar nosso algoritmo!")
    axarr[0, 0].imshow(img_base)
    axarr[0, 0].title.set_text('Figura Inicial')
    axarr[0, 0].axis('off')

    axarr[0, 1].imshow(mpimg.imread("./graf_img_base.png"))
    axarr[0, 1].title.set_text('Pixels da Figura Inicial')
    axarr[0, 1].axis('off')

    axarr[0, 2].imshow(mpimg.imread("./results_base.png"))
    axarr[0, 2].title.set_text('Pixels da Figura Inicial - Pixels da Figura Inicial')
    axarr[0, 2].axis('off')

    axarr[1, 0].imshow(img_red)
    axarr[1, 0].title.set_text('Figura Vermelha')
    axarr[1, 0].axis('off')

    axarr[1, 1].imshow(mpimg.imread("./graf_img_red.png"))
    axarr[1, 1].title.set_text('Pixels da Figura Vermelha')
    axarr[1, 1].axis('off')

    axarr[1, 2].imshow(mpimg.imread("./results_red.png"))
    axarr[1, 2].title.set_text('Pixels da Figura Inicial - Pixels da Figura Vermelha')
    axarr[1, 2].axis('off')

    axarr[2, 0].imshow(img_blue)
    axarr[2, 0].title.set_text('Figura Azul')
    axarr[2, 0].axis('off')

    axarr[2, 1].imshow(mpimg.imread("./graf_img_blue.png"))
    axarr[2, 1].title.set_text('Pixels da Figura Azul')
    axarr[2, 1].axis('off')

    axarr[2, 2].imshow(mpimg.imread("./results_blue.png"))
    axarr[2, 2].title.set_text('Pixels da Figura Inicial - Pixels da Figura Azul')
    axarr[2, 2].axis('off')

    axarr[3, 0].imshow(img_green)
    axarr[3, 0].title.set_text('Figura Verde')
    axarr[3, 0].axis('off')

    axarr[3, 1].imshow(mpimg.imread("./graf_img_green.png"))
    axarr[3, 1].title.set_text('Pixels da Figura Verde')
    axarr[3, 1].axis('off')

    axarr[3, 2].imshow(mpimg.imread("./results_green.png"))
    axarr[3, 2].title.set_text('Pixels da Figura Inicial - Pixels da Figura Verde')
    axarr[3, 2].axis('off')
    plt.show()


if __name__ == "__main__":
    main()

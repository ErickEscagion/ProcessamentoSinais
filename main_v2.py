from PIL import Image
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from algoritms.randon_algoritm import randon_algoritm
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
from results import generate_graph_results
from rgb_to_img import calc_rgb
from graph_to_img import generate_graph


def main():
    # img_base = Image.open("imgs/praia.jpg")
    # img_base = Image.open("imgs/perfil.jpg")
    img_base = Image.open("imgs/campo.jpg")
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

    generate_graph(img_blue, "graf_img_base")
    generate_graph(img_blue, "graf_img_blue")
    generate_graph(img_red, "graf_img_red")
    generate_graph(img_green, "graf_img_green")

    r, g, b = calc_rgb(width, height, pixel_values)

    r_blue, g_blue, b_blue = calc_rgb(
        width, height, calc_pixel_values(img_blue))
    res_r_blue = r - r_blue
    res_g_blue = g - g_blue
    res_b_blue = b - b_blue
    generate_graph_results(abs(res_r_blue), abs(
        res_g_blue), abs(res_b_blue), "results_blue")

    r_green, g_green, b_green = calc_rgb(
        width, height, calc_pixel_values(img_green))
    res_r_green = r - r_green
    res_g_green = g - g_green
    res_b_green = b - b_green
    generate_graph_results(abs(res_r_green), abs(
        res_g_green), abs(res_b_green), "results_green")

    r_red, g_red, b_red = calc_rgb(width, height, calc_pixel_values(img_red))
    res_r_red = r - r_red
    res_g_red = g - g_red
    res_b_red = b - b_red
    generate_graph_results(abs(res_r_red), abs(
        res_g_red), abs(res_b_red), "results_red")

    f, axarr = plt.subplots(4, 2)

    print("Obrigado por utilizar nosso algoritmo!")
    axarr[0, 0].imshow(img_base)
    axarr[0, 0].title.set_text('Figura Inicial')
    axarr[0, 0].axis('off')

    axarr[0, 1].imshow(mpimg.imread("./graf_img_base.png"))
    axarr[0, 1].title.set_text('Grafico da Figura Inicial')
    axarr[0, 1].axis('off')

    axarr[1, 0].imshow(img_red)
    axarr[1, 0].title.set_text('Figura Vermelha')
    axarr[1, 0].axis('off')

    axarr[1, 1].imshow(mpimg.imread("./results_red.png"))
    axarr[1, 1].title.set_text('Grafico da Figura Vermelha')
    axarr[1, 1].axis('off')

    axarr[2, 0].imshow(img_blue)
    axarr[2, 0].title.set_text('Figura Azul')
    axarr[2, 0].axis('off')

    axarr[2, 1].imshow(mpimg.imread("./results_blue.png"))
    axarr[2, 1].title.set_text('Grafico da Figura Azul')
    axarr[2, 1].axis('off')

    axarr[3, 0].imshow(img_green)
    axarr[3, 0].title.set_text('Figura Verde')
    axarr[3, 0].axis('off')

    axarr[3, 1].imshow(mpimg.imread("./results_green.png"))
    axarr[3, 1].title.set_text('Grafico da Figura Verde')
    axarr[3, 1].axis('off')
    plt.show()


if __name__ == "__main__":
    main()

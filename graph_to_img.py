from PIL import Image
from matplotlib import pyplot as plt
import numpy
from informations_to_image import informations_to_image

from rgb_to_img import calc_rgb


def generate_graph(img, name):
    if(type(img) == numpy.ndarray):
        img = Image.fromarray(img)

    width, height, dimensions, pixel_values = informations_to_image(img)
    r, g, b = calc_rgb(width, height, pixel_values)

    x = ["Vermelho(R)", "Verde(G)", "Azul(B)"]
    y = [round(r, 3), round(g, 3), round(b, 3)]
    plt.bar(x, y, color=['red', 'green', 'blue'])
    addlabels(x, y)
    plt.ylabel("Quantidade de Cor")
    plt.title("Dominancia de Cor")
    plt.savefig(name + '.png', format='png')
    plt.close()


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])

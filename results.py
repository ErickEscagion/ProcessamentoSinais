from PIL import Image
from matplotlib import pyplot as plt
import numpy


def generate_graph_results(r,g,b, name):
    x = ["Vermelho(R)", "Verde(G)", "Azul(B)"]
    y = [round(r, 3), round(g, 3), round(b, 3)]
    plt.bar(x, y, color=['red', 'green', 'blue'])
    addlabels(x, y)
    plt.ylabel("Quantidade de Cor")
    plt.title("Cores Alteradas")
    plt.savefig(name + '.png', format='png')
    plt.close()


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])

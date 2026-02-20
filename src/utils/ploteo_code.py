import matplotlib.pyplot as plt
import numpy as np

def plot(x_size, y_size, x_data, y_data, text_label, title, x_label, y_label):
    plt.figure(figsize = (x_size, y_size))
    plt.plot(x_data, y_data, label = text_label)
    plt.title(title)
    plt.xlabel = x_label
    plt.ylabel = y_label
    plt.legend()
    plt.show()

x = np.linspace(0, 100, 5)
y = x**2

plot(5, 5, x, y, "prueba", "titulo", "xlabel", "ylabel")
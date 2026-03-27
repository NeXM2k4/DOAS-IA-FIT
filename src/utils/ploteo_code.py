import matplotlib.pyplot as plt
import numpy as np

def simple_plot(x_size, y_size, x_data, y_data, text_label, title, x_label, y_label):
    plt.figure(figsize = (x_size, y_size))
    plt.plot(x_data, y_data, label = text_label)
    plt.title(title)
    plt.xlabel = x_label
    plt.ylabel = y_label
    plt.legend()
    plt.show()


def model_plot(history, longitudes, optical_density):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (15, 6))
    ax1.plot(history.history['loss'], label = 'Error de entrenamiento', color = 'blue')
    ax1.plot(history.history['val_loss'], label = 'Error validacion', color = 'orange')
    ax1.set_title('Error de entrenamiento')
    ax1.set_xlabel('Epoca')
    ax1.set_ylabel('MSE')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(optical_density, longitudes, label = 'Opticas Density', color = 'green')
    ax2.set_title('Optical Density')
    ax2.set_xlabel('Longitud de onda')
    ax2.set_ylabel('UA')
    .

'''
x = np.linspace(0, 100, 5)
y = x**2

simple_plot(5, 5, x, y, "prueba", "titulo", "xlabel", "ylabel")
'''
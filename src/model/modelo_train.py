import module as mdl
mdl.module(__file__)

import src.physics.generacion_datos as gen_data
import tensorflow as tf
from tensorflow.keras import layers, models


def construir_modelo(__n_gases):

    #Nombre
    __modelo = models.Sequential(name = "Gaussiano")

    #Dimensiones
    __modelo.add(layers.Input(shape = (n_pixeles, 1)))

    #Capas convolucionales
    __modelo.add(layers.Conv1D(filters = 16, kernel_size = 5, activation = 'relu'))
    __modelo.add(layers.MaxPooling1D(pool_size = 2))

    __modelo.add(layers.Conv1D(filters = 32, kernel_size = 3, activation = 'relu'))
    __modelo.add(layers.MaxPooling1D(pool_size = 2))

    __modelo.add(layers.Flatten())

    #Capas densas
    __modelo.add(layers.Dense(32, activation = 'relu'))
    #__modelo.add(layers.Dropout(0.085))
    __modelo.add(layers.Dense(__n_gases, activation = 'linear'))

    #Compilación
    __modelo.compile(optimizer = 'adam', loss = 'mse', metrics = ['accuracy'])

    return __modelo

n_gases = 2
n_muestras = 2000
n_pixeles = 200
Datos_train, Real_Slant_Colum_Densities, __ = gen_data.generar_datos(n_gases, n_muestras, n_pixeles)


modelo = construir_modelo(n_gases)
modelo.summary()
Real_Slant_Colum_Densities_Trans = Real_Slant_Colum_Densities.T
#ENTRENAMIENTO

historial = modelo.fit(
    Datos_train,
    Real_Slant_Colum_Densities_Trans,
    epochs           = 50,
    batch_size       = 32,
    validation_split = 0.2,
    verbose          = 1
)
import numpy as np
#import matplotlib.pyplot as plt

#GENERAR LOS DATOS SINTÉTICOS

def seccion_eficaz_simulada(__n_gases, __longitudes_de_onda, __n_pixeles):

    secciones_eficaces_simuladas = np.zeros((__n_gases,__n_pixeles))

    #Parámetos de las gaussianas
    for i in range(__n_gases):
        amplitud_1 = np.random.uniform(0.7, 1)
        amplitud_2 = np.random.uniform(0.7, 1)
        amplitud_3 = np.random.uniform(0.7, 1)

        lambda_pico_1 = np.random.randint(400, 420)
        lambda_pico_2 = np.random.randint(420, 440)
        lambda_pico_3 = np.random.randint(440, 460)

        desviacion_estandar_1 = np.random.uniform(1.5, 3.1)
        desviacion_estandar_2 = np.random.uniform(1.5, 3.1)
        desviacion_estandar_3 = np.random.uniform(1.5, 3.1)

        #Definiendo las gaussianas
        gaussiana_1 = amplitud_1 * np.exp(-0.5 * ((__longitudes_de_onda - lambda_pico_1)/desviacion_estandar_1)**2)
        gaussiana_2 = amplitud_2 * np.exp(-0.5 * ((__longitudes_de_onda - lambda_pico_2)/desviacion_estandar_2)**2)
        gaussiana_3 = amplitud_3 * np.exp(-0.5 * ((__longitudes_de_onda - lambda_pico_3)/desviacion_estandar_3)**2)
        gaussiana_def = gaussiana_1 + gaussiana_2 + gaussiana_3

        secciones_eficaces_simuladas[i,:] = gaussiana_def

    return secciones_eficaces_simuladas

def generar_datos(__n_gases, __n_muestras, __n_pixeles):

    #Definiendo variables
    longitudes_de_onda    = np.linspace(400, 460, __n_pixeles)
    seccion_eficaz        = seccion_eficaz_simulada(__n_gases, longitudes_de_onda, __n_pixeles)
    Datos                 = np.zeros((__n_muestras, __n_pixeles))
    Slant_Colum_Densities = np.zeros((__n_gases, __n_muestras))

    #Generando los datos
    for i in range(__n_muestras):
        densidad_optica = np.zeros((__n_muestras, __n_pixeles))
        for j in range(__n_gases):
            slant_colum_density = np.random.uniform(0, 1000)
            Slant_Colum_Densities[j, i] = slant_colum_density
            densidad_optica[i,:] += seccion_eficaz[j, :] * slant_colum_density

        ruido = np.random.normal(0, 35, __n_pixeles)
        Datos[i, :] = densidad_optica[i] + ruido

    return Datos, Slant_Colum_Densities, longitudes_de_onda
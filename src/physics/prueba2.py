import Filtros
import DOAS_Processing_IPM as imp
import pandas as pd
import matplotlib.pyplot as plt

#Agarrar la medida y el offset
df_referencia = pd.read_csv("referencia.txt", sep = "\t", skiprows = [1])
df_medida     = pd.read_csv("medida.txt", sep = "\t", skiprows = [1])
df_offset     = pd.read_csv("offset.txt", sep = "\t", skiprows = [1])

df_referencia = df_referencia.iloc[:, :2]
df_medida     = df_medida.iloc[:, :2]
df_offset     = df_offset.iloc[:, :2]

#Restarle el offset a la medida
df_medida["Intensities"]     = df_medida["Intensities"] - df_offset["Intensities"]
df_referencia["Intensities"] = df_referencia["Intensities"] - df_offset["Intensities"]

print(df_referencia)
print(df_medida)

#Aplicarle los filtros
filtro = Filtros.FiltroDOASIA()
datos_procesados = filtro.procesar_espectro_ia(df_medida["Wavelength"].values, 
                                               df_referencia["Intensities"].values, 
                                               df_medida["Intensities"].values,
                                               df_offset["Intensities"].values)

df_output = pd.DataFrame({
    "Wavelength(nm)": df_medida["Wavelength"],
    "OD(a.u.)": datos_procesados
})

#Mostrar la gráfica
plt.figure()

plt.subplot(2, 1, 1)
plt.plot(df_medida["Wavelength"], df_medida["Intensities"], label='Intensidad Medida (Cruda)', color='blue', alpha=0.7)
plt.title("Intensidad Cruda")
plt.ylabel("Intensidad (a.u.)")
plt.grid(alpha=0.3)
plt.legend()

# Subplot 2: El resultado para la IA
plt.subplot(2, 1, 2)
plt.plot(df_medida["Wavelength"], datos_procesados, label='Densidad Óptica Diferencial (Filtrada)', color='red')
plt.title("Señal Limpia")
plt.xlabel("Longitud de Onda (nm)")
plt.ylabel("OD Diferencial")
plt.grid(alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()
'''
import Filtros
import DOAS_Processing_IPM as imp
import pandas as pd
import matplotlib.pyplot as plt

#Agarrar la medida y el offset
df_referencia = pd.read_csv("referencia.txt", sep = "\t", skiprows = [1])
df_medida     = pd.read_csv("medida.txt", sep = "\t", skiprows = [1])
df_offset     = pd.read_csv("offset.txt", sep = "\t", skiprows = [1])

df_referencia = df_referencia.iloc[:, :2]
df_medida     = df_medida.iloc[:, :2]
df_offset     = df_offset.iloc[:, :2]

#Restarle el offset a la medida
df_medida["Intensities"]     = df_medida["Intensities"] - df_offset["Intensities"]
df_referencia["Intensities"] = df_referencia["Intensities"] - df_offset["Intensities"]

print(df_referencia)
print(df_medida)

#Aplicarle los filtros
filtro = Filtros.FiltroDOASIA()
datos_procesados = filtro.procesar_espectro_ia(df_medida["Wavelength"].values, 
                                               df_referencia["Intensities"].values, 
                                               df_medida["Intensities"].values)

df_output = pd.DataFrame({
    "Wavelength(nm)": df_medida["Wavelength"],
    "OD(a.u.)": datos_procesados
})

#Mostrar la gráfica
plt.figure()

plt.subplot(2, 1, 1)
plt.plot(df_medida["Wavelength"], df_medida["Intensities"], label='Intensidad Medida (Cruda)', color='blue', alpha=0.7)
plt.title("Intensidad Cruda")
plt.ylabel("Intensidad (a.u.)")
plt.grid(alpha=0.3)
plt.legend()

# Subplot 2: El resultado para la IA
plt.subplot(2, 1, 2)
plt.plot(df_medida["Wavelength"], datos_procesados, label='Densidad Óptica Diferencial (Filtrada)', color='red')
plt.title("Señal Limpia")
plt.xlabel("Longitud de Onda (nm)")
plt.ylabel("OD Diferencial")
plt.grid(alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()
'''
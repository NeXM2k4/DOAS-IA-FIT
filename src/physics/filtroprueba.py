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

wavelengths = df_medida["Wavelength"].values
I_ref       = df_referencia["Intensities"].values
I_meas      = df_medida["Intensities"].values
I_dark      = df_offset["Intensities"].values

print(df_referencia)
print(df_medida)

#Ventana
fit_wav_sta = 370
fit_wav_end = 410

#Mask
mask = (wavelengths >= fit_wav_sta) & (wavelengths <= fit_wav_end)

fit_wv   = wavelengths[mask]
fit_ref  = I_ref[mask]
fit_meas = I_meas[mask]
fit_dark = I_dark[mask]

#Aplicarle los filtros
filtro = Filtros.FiltroDOASIA()
datos_procesados = filtro.procesar_espectro_ia(fit_wv, fit_ref, fit_meas, fit_dark)

df_output = pd.DataFrame({
    "Wavelength(nm)": fit_wv,
    "OD(a.u.)": datos_procesados
})

# Plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))

ax1.plot(wavelengths, I_meas, label="Intensidad Medida (Cruda)", color="blue", alpha=0.7)
ax1.set_title("Intensidad Cruda")
ax1.set_ylabel("Intensidad (a.u.)")
ax1.legend()
ax1.grid(alpha=0.3)

ax2.plot(fit_wv, datos_procesados, label="Densidad Óptica Diferencial (Filtrada)", color="red")
ax2.set_title("Señal Limpia — Ventana de Fit (370–410 nm)")
ax2.set_xlabel("Longitud de Onda (nm)")
ax2.set_ylabel("OD Diferencial")
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
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

wavelengths = df_medida["Wavelength"].values
I_ref       = df_referencia["Intensities"].values
I_meas      = df_medida["Intensities"].values
I_dark      = df_offset["Intensities"].values

print(df_referencia)
print(df_medida)

#Ventana
fit_wav_sta = 370
fit_wav_end = 410

#Mask
mask = (wavelengths >= fit_wav_sta) & (wavelengths <= fit_wav_end)

fit_wv   = wavelengths[mask]
fit_ref  = I_ref[mask]
fit_meas = I_meas[mask]
fit_dark = I_dark[mask]

#Aplicarle los filtros
filtro = Filtros.FiltroDOASIA()
datos_procesados = filtro.procesar_espectro_ia(fit_wv, fit_ref, fit_meas, fit_dark)

df_output = pd.DataFrame({
    "Wavelength(nm)": fit_wv,
    "OD(a.u.)": datos_procesados
})

# Plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))

ax1.plot(wavelengths, I_meas, label="Intensidad Medida (Cruda)", color="blue", alpha=0.7)
ax1.set_title("Intensidad Cruda")
ax1.set_ylabel("Intensidad (a.u.)")
ax1.legend()
ax1.grid(alpha=0.3)

ax2.plot(fit_wv, datos_procesados, label="Densidad Óptica Diferencial (Filtrada)", color="red")
ax2.set_title("Señal Limpia — Ventana de Fit (370–410 nm)")
ax2.set_xlabel("Longitud de Onda (nm)")
ax2.set_ylabel("OD Diferencial")
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()
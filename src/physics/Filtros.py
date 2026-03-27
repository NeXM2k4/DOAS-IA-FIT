import numpy as np
import DOAS_Processing_IPM as ipm
from scipy.integrate import trapezoid
from scipy.interpolate import Akima1DInterpolator
from scipy import signal

class FiltroDOASIA:
    def __init__(self):
        """
        Inicializa el filtro utilizando las variables de configuración de ipm.
        """
        print("🔧 Inicializando Preprocesador DOAS para IA...")
        print(f"  - Filtro tipo: {ipm.od_typ}")
        print(f"  - Frecuencia de corte baja: {ipm.od_lowcut} Hz")
        print(f"  - Frecuencia de corte alta: {ipm.od_highcut} Hz")

    def od_cleaning(self, wavelengths, I_ref, I_meas, I_dark):
        """
        Calcula la Densidad Óptica (OD) y la limpia interpolando valores inválidos.
        Recrea la lógica de OD_Cleaning pero sin modificar arreglos externos.
        """
        # Restamos el Dark Offset si es necesario (asumimos 0 si ya viene limpio)
        ref_clean = np.abs(I_ref - I_dark)
        meas_clean = np.abs(I_meas - I_dark)
        
        oddrty = np.zeros_like(wavelengths, dtype=float)
        odmask = np.zeros_like(wavelengths, dtype=bool)
        
        # Simulación de la lógica de integración de tu código original
        # En tu código original, se compara la integral de la medida vs referencia
        # Aquí simplificamos la condición para el cálculo directo de DOAS
        for i in range(len(wavelengths)):
            if ref_clean[i] > 1e-6 and meas_clean[i] > 1e-6:
                oddrty[i] = np.log(np.abs(ref_clean[i] / meas_clean[i]))
                if np.isfinite(oddrty[i]):
                    odmask[i] = True
                else:
                    oddrty[i] = np.nan
                    odmask[i] = False
            else:
                oddrty[i] = np.nan
                odmask[i] = False
                
        # Interpolación de Akima para limpiar NaNs
        if np.any(odmask) and not np.all(odmask):
             oddrty = Akima1DInterpolator(wavelengths[odmask], oddrty[odmask], method="makima")(wavelengths)
        elif not np.any(odmask):
             oddrty = np.zeros_like(wavelengths) # Failsafe si todo es ruido
             
        return oddrty

    def od_wght(self, data_x, data_y):
        """
        Calcula los pesos (Kernel Gaussiano) idéntico a tu función OD_Wght
        """
        wghts_w = 120
        wghts_nrm = data_y.max()
        if wghts_nrm == 0: wghts_nrm = 1e-6 # Failsafe

        px_ampltd = np.abs(data_y / wghts_nrm)
        diff = data_x[:, np.newaxis] - data_x[np.newaxis, :]
        kernel_matrix = np.exp(-(diff / wghts_w)**2)
        kernel_sum = kernel_matrix.sum(axis=1)
        wghts = px_ampltd * kernel_sum
        return wghts

    def od_filtering(self, odwv, oddrty):
        """
        Aplica el filtro Butterworth usando las constantes de ipm.
        """
        # Calcular frecuencias de corte usando variables de ipm
        fil_low = ipm.od_lowcut / (ipm.od_fctr_lwc * ipm.od_frq_sr)
        fil_high = ipm.od_highcut / (ipm.od_fctr_hgc * ipm.od_frq_sr)
        
        # Limitar frecuencias para evitar errores de SciPy (0 < Wn < 1)
        fil_low = np.clip(fil_low, 1e-5, 0.99)
        fil_high = np.clip(fil_high, fil_low + 1e-5, 0.999)
        
        # Calcular pesos y offset DC
        ofs_wghts = self.od_wght(odwv, oddrty)
        if np.sum(ofs_wghts) == 0:
            ofs_dc = np.mean(oddrty)
        else:
            ofs_dc = np.average(oddrty, weights=ofs_wghts)
        
        # Crear y aplicar filtro
        sos = signal.butter(2, [fil_low, fil_high], btype=ipm.od_typ, output='sos', fs=ipm.od_frq_sr)
        od_filtered = signal.sosfiltfilt(sos, oddrty - ofs_dc)
        
        # Re-añadir offset
        od_final = od_filtered + ofs_dc
        return od_final

    def procesar_espectro_ia(self, wavelengths, I_ref, I_meas, I_dark):
        """
        FUNCIÓN MAESTRA para llamar desde el entrenamiento de la IA.
        """
        # 1. Limpieza y OD
        od_clean = self.od_cleaning(wavelengths, I_ref, I_meas, I_dark)
        
        # 2. Filtrado
        od_final = self.od_filtering(wavelengths, od_clean)
        
import numpy as np
import DOAS_Processing_IPM as ipm
from scipy.integrate import trapezoid
from scipy.interpolate import Akima1DInterpolator
from scipy import signal

class FiltroDOASIA:
    def __init__(self):
        """
        Inicializa el filtro utilizando las variables de configuración de ipm.
        """
        print("🔧 Inicializando Preprocesador DOAS para IA...")
        print(f"  - Filtro tipo: {ipm.od_typ}")
        print(f"  - Frecuencia de corte baja: {ipm.od_lowcut} Hz")
        print(f"  - Frecuencia de corte alta: {ipm.od_highcut} Hz")

    def od_cleaning(self, wavelengths, I_ref, I_meas, I_dark):
        """
        Calcula la Densidad Óptica (OD) y la limpia interpolando valores inválidos.
        Recrea la lógica de OD_Cleaning pero sin modificar arreglos externos.
        """
        # Restamos el Dark Offset si es necesario (asumimos 0 si ya viene limpio)
        ref_clean = np.abs(I_ref - I_dark)
        meas_clean = np.abs(I_meas - I_dark)
        
        oddrty = np.zeros_like(wavelengths, dtype=float)
        odmask = np.zeros_like(wavelengths, dtype=bool)
        
        # Simulación de la lógica de integración de tu código original
        # En tu código original, se compara la integral de la medida vs referencia
        # Aquí simplificamos la condición para el cálculo directo de DOAS
        for i in range(len(wavelengths)):
            if ref_clean[i] > 1e-6 and meas_clean[i] > 1e-6:
                oddrty[i] = np.log(np.abs(ref_clean[i] / meas_clean[i]))
                if np.isfinite(oddrty[i]):
                    odmask[i] = True
                else:
                    oddrty[i] = np.nan
                    odmask[i] = False
            else:
                oddrty[i] = np.nan
                odmask[i] = False
                
        # Interpolación de Akima para limpiar NaNs
        if np.any(odmask) and not np.all(odmask):
             oddrty = Akima1DInterpolator(wavelengths[odmask], oddrty[odmask], method="makima")(wavelengths)
        elif not np.any(odmask):
             oddrty = np.zeros_like(wavelengths) # Failsafe si todo es ruido
             
        return oddrty

    def od_wght(self, data_x, data_y):
        """
        Calcula los pesos (Kernel Gaussiano) idéntico a tu función OD_Wght
        """
        wghts_w = 120
        wghts_nrm = data_y.max()
        if wghts_nrm == 0: wghts_nrm = 1e-6 # Failsafe

        px_ampltd = np.abs(data_y / wghts_nrm)
        diff = data_x[:, np.newaxis] - data_x[np.newaxis, :]
        kernel_matrix = np.exp(-(diff / wghts_w)**2)
        kernel_sum = kernel_matrix.sum(axis=1)
        wghts = px_ampltd * kernel_sum
        return wghts

    def od_filtering(self, odwv, oddrty):
        """
        Aplica el filtro Butterworth usando las constantes de ipm.
        """
        # Calcular frecuencias de corte usando variables de ipm
        fil_low = ipm.od_lowcut / (ipm.od_fctr_lwc * ipm.od_frq_sr)
        fil_high = ipm.od_highcut / (ipm.od_fctr_hgc * ipm.od_frq_sr)
        
        # Limitar frecuencias para evitar errores de SciPy (0 < Wn < 1)
        fil_low = np.clip(fil_low, 1e-5, 0.99)
        fil_high = np.clip(fil_high, fil_low + 1e-5, 0.999)
        
        # Calcular pesos y offset DC
        ofs_wghts = self.od_wght(odwv, oddrty)
        if np.sum(ofs_wghts) == 0:
            ofs_dc = np.mean(oddrty)
        else:
            ofs_dc = np.average(oddrty, weights=ofs_wghts)
        
        # Crear y aplicar filtro
        sos = signal.butter(2, [fil_low, fil_high], btype=ipm.od_typ, output='sos', fs=ipm.od_frq_sr)
        od_filtered = signal.sosfiltfilt(sos, oddrty - ofs_dc)
        
        # Re-añadir offset
        od_final = od_filtered + ofs_dc
        return od_final

    def procesar_espectro_ia(self, wavelengths, I_ref, I_meas, I_dark):
        """
        FUNCIÓN MAESTRA para llamar desde el entrenamiento de la IA.
        """
        # 1. Limpieza y OD
        od_clean = self.od_cleaning(wavelengths, I_ref, I_meas, I_dark)
        
        # 2. Filtrado
        od_final = self.od_filtering(wavelengths, od_clean)
        
        return od_final
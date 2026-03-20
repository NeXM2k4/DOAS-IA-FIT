import pandas as pd
from datetime import date
from pathlib import Path

class DOAS_results_parser:
    """
    Parses DOAS result files (e.g. Results_RTFit_CHOCHO.txt) into a
    structured pandas DataFrame in LONG format.
    """
    SEPARATOR = ","

    def __init__(self, filepath: str | Path) -> None:
        self.filepath = Path(filepath)
        self._df: pd.DataFrame | None = None
        self.base_units: dict[str, str] = {}

    def parse(self, capture_date: date | None = None) -> pd.DataFrame:
        with open(self.filepath, "r") as f:
            lines = f.readlines()

        # Extraer nombres de columnas y unidades (líneas 0 y 1)
        headers_raw = [col.strip() for col in lines[0].split(self.SEPARATOR) if col.strip()]
        units_raw = [u.strip() for u in lines[1].split(self.SEPARATOR)]

        # 1. Limpiar los encabezados y Mapear las unidades a las variables base
        unique_headers = []
        prev_field = ""
        
        for h, u in zip(headers_raw, units_raw):
            if h.startswith("Error["):
                bracket = h[len("Error"):]
                col_name = f"Error_{prev_field}{bracket}"
                base_name = f"Error_{prev_field}"
            else:
                prev_field = h.split("[")[0]
                col_name = h
                base_name = prev_field

            unique_headers.append(col_name)

            # Ajustar nombres en el diccionario de unidades para que coincidan con la tabla final
            if base_name == "Con":
                base_name = "Concentration"
            elif base_name == "Error_Con":
                base_name = "Error_Concentration"

            # Guardar la unidad de la variable base (solo la primera vez que aparece)
            if base_name not in self.base_units:
                self.base_units[base_name] = u

        # 2. Leer los datos numéricos
        data_lines = lines[2:]
        rows = []
        for line in data_lines:
            line = line.strip()
            if not line:
                continue
            values = [v.strip() for v in line.split(self.SEPARATOR) if v.strip()]
            rows.append(values)

        df = pd.DataFrame(rows, columns=unique_headers)
        df["Set"] = pd.to_numeric(df["Set"], errors="coerce").astype("Int64")

        # 3. Dar formato a los tiempos y números ANTES de transformar la tabla
        for col in df.columns:
            if col == "Set":
                continue
            if col.startswith("Error_Time["):
                df[col] = pd.to_timedelta(df[col], errors="coerce")
            elif col.startswith("Time["):
                if capture_date is not None:
                    date_str = f"{capture_date.isoformat()} "
                    df[col] = pd.to_datetime(date_str + df[col].astype(str), errors="coerce")
                else:
                    df[col] = pd.to_timedelta(df[col], errors="coerce")
            else:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        # 4. Transformar a FORMATO LARGO (Melt -> Extract -> Pivot)
        df_melted = df.melt(id_vars=["Set"], var_name="Raw_Column", value_name="Value")
        
        extracted = df_melted["Raw_Column"].str.extract(r'([A-Za-z_]+)\[azi_(\d+)_ele_(\d+)\]')
        df_melted[["Base_Var", "Azimutal", "Elevation"]] = extracted
        
        df_melted["Azimutal"] = pd.to_numeric(df_melted["Azimutal"])
        df_melted["Elevation"] = pd.to_numeric(df_melted["Elevation"])
        
        df_final = df_melted.pivot(
            index=["Set", "Azimutal", "Elevation"], 
            columns="Base_Var", 
            values="Value"
        ).reset_index()
        
        # 5. Renombrar las columnas de Concentración
        df_final.rename(columns={
            "Con": "Concentration", 
            "Error_Con": "Error_Concentration"
        }, inplace=True)
        
        # 6. Ordenar columnas según tu requerimiento
        column_order = [
            "Set", "Azimutal", "Elevation", "Time", "Error_Time", 
            "Concentration", "Error_Concentration", "SCD", "Error_SCD", 
            "Shift", "Error_Shift", "Squeeze", "Error_Squeeze"
        ]
        final_cols = [c for c in column_order if c in df_final.columns]
        
        self._df = df_final[final_cols]
        return self._df

    def get_units(self) -> dict[str, str]:
        """
        Retorna un diccionario limpio con las variables y sus unidades.
        """
        if not self.base_units:
            raise RuntimeError("Call parse() before get_units().")
        return self.base_units


# ==========================================
# CÓMO USARLO Y NAVEGAR POR LAS CARPETAS
# ==========================================
if __name__ == "__main__":
    # 1. Obtenemos la ruta donde está ESTE script (formateo_resultados.py)
    # Ruta actual: Root/src/model/data_processing/formateo_resultados.py
    current_dir = Path(__file__).resolve().parent 
    
    # 2. Subimos 3 niveles hasta la carpeta raíz (Root)
    # parent 1: model | parent 2: src | parent 3: Root
    root_dir = current_dir.parent.parent.parent 
    
    # 3. Bajamos a la carpeta de resultados
    results_dir = root_dir / "data" / "results"
    
    print(f"Buscando archivos en: {results_dir}\n")

    # 4. Buscamos todos los archivos txt que empiecen con 'Results_RTFit_'
    archivos_resultados = list(results_dir.glob("Results_RTFit_*.txt"))

    if not archivos_resultados:
        print("No se encontraron archivos en la carpeta especificada.")
    else:
        # Creamos un diccionario o lista para guardar todos los DataFrames si lo deseas
        tablas_procesadas = {}

        for archivo_txt in archivos_resultados:
            print(f"--- Procesando: {archivo_txt.name} ---")
            
            # Instanciamos la clase pasándole la ruta del archivo
            parser = DOAS_results_parser(archivo_txt)
            
            # Formateamos la tabla (puedes pasarle un capture_date=date(2026,3,19) si quieres)
            df_limpio = parser.parse() 
            
            # Obtenemos las unidades
            unidades = parser.get_units()
            
            print(f"Unidades encontradas: {unidades}")
            print(f"Filas y Columnas de la tabla: {df_limpio.shape}")
            print(df_limpio.head(3)) # Mostrar las primeras 3 filas
            print("\n")

            # Guardamos el DataFrame en el diccionario usando el nombre del archivo como clave
            # Ejemplo: tablas_procesadas['Results_RTFit_CHOCHO.txt'] = df_limpio
            tablas_procesadas[archivo_txt.name] = df_limpio

            df_limpio.to_csv(f'{archivo_txt.name}.csv', sep = '\t', index = False)
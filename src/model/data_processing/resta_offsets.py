import pandas as pd
import re
from pathlib import Path

BASE_DIR        = Path(__file__).resolve().parents[3]
INTENSITIES_DIR = BASE_DIR / "data" / "data_intensities"
OFFSET_DIR      = BASE_DIR / "data" / "offsets"


def load_txt(filepath):
    return pd.read_csv(filepath, sep = "\t", header = None,
                       names = ["Wavelength", "Intensities"],
                       skiprows = [0, 1],
                       usecols=[0, 1],
                       index_col=False,
                       dtype = float)


def get_offset_for(set_number):
    offset_file = OFFSET_DIR / f"Set_{set_number}_Offset.txt"
    return load_txt(offset_file)


def subtract_offsets():
    pattern = re.compile(r"Set_(\w+)_Azi_([\d.]+)_Ele_([\d.]+)\.txt")
    results = []

    for result_file in sorted(INTENSITIES_DIR.glob("*.txt")):
        match = pattern.match(result_file.name)
        if not match:
            continue

        set_num, azi, ele = match.group(1), match.group(2), match.group(3)

        df     = load_txt(result_file)
        offset = get_offset_for(set_num)

        # .values evita el problema de alineación de índices
        df["Intensities_corrected"] = df["Intensities"].values - offset["Intensities"].values

        # Una fila por medición, con listas
        results.append({
            "set"                   : set_num,
            "azi"                   : float(azi),
            "ele"                   : float(ele),
            "wavelengths"           : df["Wavelength"].tolist(),
            "intensities_corrected" : df["Intensities_corrected"].tolist(),
        })

    final_df = pd.DataFrame(results)
    return final_df


if __name__ == "__main__":
    df = subtract_offsets()
    print(df.head())
    print(df.shape)
    df.to_csv('archivo.csv', sep = '\t', index = False)
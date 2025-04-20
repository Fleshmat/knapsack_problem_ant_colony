import pandas as pd
import numpy as np
from config import EXCEL_INPUT_PATH, EXCEL_SHEET_NAME

def cargar_items():
    datos = pd.read_excel(EXCEL_INPUT_PATH, sheet_name=EXCEL_SHEET_NAME)
    items_tup = [(int(datos.iloc[i, 0]), int(1000 * datos.iloc[i, 1]), int(datos.iloc[i, 2]), int(datos.iloc[i, 3]))
                 for i in range(len(datos))]
    return np.array(items_tup)

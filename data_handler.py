
import os
import pandas as pd
from datetime import datetime

# Diretório onde os arquivos CSV serão salvos
DATA_DIR = "logs"
os.makedirs(DATA_DIR, exist_ok=True)

def save_data(data: dict, table_name: str):
    """
    Salva os dados em um arquivo CSV nomeado com base na tabela.
    Cada chamada adiciona uma linha.
    """
    df_new = pd.DataFrame([data])
    file_path = os.path.join(DATA_DIR, f"{table_name}.csv")
    if os.path.exists(file_path):
        df_existing = pd.read_csv(file_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.to_csv(file_path, index=False)
    else:
        df_new.to_csv(file_path, index=False)

def load_data(table_name: str) -> pd.DataFrame:
    """
    Carrega os dados de uma tabela (arquivo CSV).
    """
    file_path = os.path.join(DATA_DIR, f"{table_name}.csv")
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame()

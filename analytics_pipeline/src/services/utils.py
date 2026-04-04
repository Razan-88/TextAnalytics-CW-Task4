import pandas as pd
import numpy as np
import os



baseDIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def load_data(file_name):
    try:
        file_path = os.path.join(baseDIR, 'data', file_name)
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    

def save_data(data, file_name):
    try:
        file_path = os.path.join(baseDIR, 'data', file_name)
        data.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Error saving data: {e}")
        return None
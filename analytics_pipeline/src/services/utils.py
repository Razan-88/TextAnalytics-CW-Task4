import joblib
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

def save_model(model, subdirectory, file_name):
    try:
        dir_path = os.path.join(baseDIR, 'models', subdirectory)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, file_name)
        joblib.dump(model, file_path)
    except Exception as e:
        print(f"Error saving model: {e}")


def load_model(subdirectory, file_name):
    try:
        file_path = os.path.join(baseDIR, 'models', subdirectory, file_name)
        model = joblib.load(file_path)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None
    
def saveplot(plot, subdirectory, file_name):
    try:
        clean_name = file_name
        if ':' in clean_name:
            clean_name = clean_name.replace(':', '')
        if ' ' in clean_name:
            clean_name = "_".join(clean_name.split())
        dir_path = os.path.join(baseDIR, 'models', 'artifacts', subdirectory)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, f"{clean_name}.png")
        plot.savefig(file_path)
    except Exception as e:
        print(f"Error saving plot: {e}")
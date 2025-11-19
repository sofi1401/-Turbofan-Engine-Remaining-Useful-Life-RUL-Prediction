import pandas as pd
import os

# Folder path
data_dir = r"C:\Users\LENOVO\Downloads\turbofan project\Datas"

def read_rul(filename):
    # Correct way to join path
    path = os.path.join(data_dir, filename)
    df = pd.read_csv(path, sep='\s+', header=None, names=['RUL'])
    print(df.head())
    print("Total engines:", len(df))
    return df

rul_df = read_rul("RUL_FD001.txt")

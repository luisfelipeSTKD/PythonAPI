import sys 
sys.path.append('../') # para relative imports

import os
import json
import openpyxl
import requests

import pandas as pd

from IPython.core.interactiveshell import InteractiveShell


######## LOAD DATASET ########

def downloader(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    filename = url.split('/')[-1].replace(" ", "_")
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:
        print(f"Download failed: status code {r.status_code}\n{r.text}")

###### URL #####

url_to_titanic_data = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
downloader(url_to_titanic_data, './data')

###### TRANSFORM DATA ######

df = pd.read_csv('./data/titanic.csv')
df.to_json(r'./data/titanic.json')
df.to_excel(r'./data/titanic.xlsx')

with open('./data/titanic.json') as json_file:
    data = json.load(json_file)

df = pd.read_json('./data/titanic.json')
df.to_hdf(
    './titanic_data.h5',
    'titanic_data',
    mode='w'
)

# pd.read_hdf('./titanic_data.h5')

df.to_feather('./titanic_data.feather')

df.to_parquet('./titanic_data.parquet')

df.to_pickle('./titanic_data.pkl')
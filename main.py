import requests
import pandas as pd
from datetime import datetime

timestamp = datetime.now()
base_url = 'https://portaldata.kemenhub.go.id/api/siasati'
base_filename = 'laporan_pusintrans_0'
formatted_timestamp = timestamp.strftime("%Y-%m-%d_%H-%M-%S")
for id in range(1,7):
    filename = f'{base_filename}{id}'
    url = f'{base_url}/{filename}?&format=json'
    response = requests.get(url).json()
    pd.DataFrame(response).to_parquet(f'output/{formatted_timestamp}_{filename}.parquet', engine='pyarrow')
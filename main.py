import requests
import pandas as pd
from datetime import datetime
import pytz

timestamp = datetime.now(pytz.utc)

# Define WIB timezone (UTC +7)
wib_timezone = pytz.timezone('Asia/Jakarta')

# Convert the UTC time to WIB
formatted_timestamp = timestamp.astimezone(wib_timezone).strftime("%Y-%m-%d_%H-%M-%S")

base_url = 'https://portaldata.kemenhub.go.id/api/siasati'
base_filename = 'laporan_pusintrans_0'

for id in range(1,7):
    filename = f'{base_filename}{id}'
    url = f'{base_url}/{filename}?&format=json'
    response = requests.get(url).json()
    pd.DataFrame(response).to_csv(f'{formatted_timestamp}_{filename}.csv', index=False)

import os
from ucimlrepo import fetch_ucirepo
import pandas as pd

DATA_DIR = 'data'
PICKLE_PATH = os.path.join(DATA_DIR, 'rt_iot2022.csv')

os.makedirs(DATA_DIR, exist_ok=True)

try:
    if os.path.exists(PICKLE_PATH):
        print("data file already exists")
    else:
        print("creating data file...")
        # fetch dataset
        rt_iot2022 = fetch_ucirepo(id=942)

        # data (as pandas dataframes)
        X = rt_iot2022.data.features
        y = rt_iot2022.data.targets

        # combine features and targets into a single DataFrame
        df = pd.concat([X, y], axis=1)
        df.to_csv(PICKLE_PATH, index=False)
        print("data file created")

except Exception as e:
    print(f'Erreur: {e}')
import os
from pathlib import Path
import json
import pandas as pd
data = {}
for file in os.listdir('raw_data'):
    fp = Path(f"raw_data/{file}")
    df = pd.read_excel(fp) 
    indicator = fp.stem 
    first_col_name = df[df.columns[0]].name
    try:
        int(first_col_name)
        if df.index.name == None:
            df.index.name = 'Country'
    except:
        df.set_index(df.columns[0], inplace=True)
        df.index.name = 'Country'
    print('===' * 20)
    print(indicator)
    print('===' * 20)
    print(df.head().to_dict(orient='index'))
    data[indicator] = df.to_dict(orient='index')
    
with open(f'json/master_data.json', 'w') as outfile:
        json.dump(data, outfile)
        
    
    


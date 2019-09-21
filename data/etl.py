import os
from pathlib import Path
import json
import pandas as pd

data = {}
for file in os.listdir('raw_data'):
    fp = Path(f"raw_data/{file}")
    dfs = pd.read_excel(fp) 
    print(fp.stem)
    if isinstance(dfs, pd.DataFrame):
        df = dfs.fillna(0)
        df.index = df.iloc[:, 0]
        dict_ = df.to_json(orient='records')
        with open(f'json/{fp.stem}.json', 'w') as outfile:
            json.dump(dict_, outfile)
    else:
        for name, sheet in dfs.items():
            print(name)
            try:
                print(sheet.info())
                print('====' * 20)
                print(sheet.head(10))
            except:
                print(sheet)

            cont = input('save? y/n >>>>')
            if cont == 'n':
                pass
            else:
                name = input('Name for json file >>>> ')
                index_col = input('Index column >>> ')
                dict_ = sheet.set_index(index_col).to_json(orient='records')
                with open(f'json/{name}.json', 'w') as outfile:
                    json.dump(dict_, outfile)


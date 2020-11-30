#
# read-json.py
#
import pandas as pd

jsondata = pd.read_json('data.json')

print(jsondata)
print()

print(jsondata.iloc[1:3,1:3])
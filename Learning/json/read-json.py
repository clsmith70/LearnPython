#
# read-json.py
#
import json

_file = open('data.json',)
jsondata = json.load(_file)
for i in jsondata['glossary']:
    print(i)

_file.close()
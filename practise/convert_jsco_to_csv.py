import json
import csv
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

with open('article.json') as json_file:
    jsondata = json.load(json_file)

# data_file = open('article.csv', 'w', newline='')
# csv_writer = csv.writer(data_file)

df = pd.json_normalize(jsondata)
# print(df)
df.to_csv('article.csv',index = False)

# count = 0
# for data in jsondata:
#     print(data)
#     if count == 0:
#         header = data.keys()
#         csv_writer.writerow(header)
#         count += 1
#     csv_writer.writerow(data.values())
#
# data_file.close()
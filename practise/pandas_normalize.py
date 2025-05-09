import pandas as pd
json_data = [
    {"id": 1, "name": "Alice", "address": {"city": "Wonderland", "zip": "12345"}},
    {"id": 2, "name": "Bob", "address": {"city": "Builderland", "zip": "67890"}}
]
df = pd.json_normalize(json_data)
print(df)
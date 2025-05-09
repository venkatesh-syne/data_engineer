import requests

try:
    x = requests.get("https://www.amazon.in/")
except Exception as e:
    print("Error: ", e)

print(x.text)
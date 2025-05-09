import requests

try:
    url = "https://itunes.apple.com/gb/rss/customerreviews/id=1500780518/sortBy=mostRecent/json"
    r = requests.get(url)
    data = r.json()
    entries = data["feed"]["entry"][1]
    print(entries)
except Exception as e:
    print("error: ",e)

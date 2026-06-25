import json
import sys
import requests

if len(sys.argv) < 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term="+sys.argv[1])
# print(response.json()) print the result in json format
# print(json.dumps(response.json(), indent=2)) for more concise format
# but we need only songs name, so
o = response.json()
for t in o["results"]: #result is the dictionary in the json file, where we have to look for the song
    print(t["trackName"]) # trackName is the key in the results
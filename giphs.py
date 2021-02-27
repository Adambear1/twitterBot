# python
import urllib
import json
import random
import os


def get_gif():
    values = ["ken griffey jr", "Edgar Martinez", "Seattle Mariners", "Jarrod Kelenic", "Kyle Lewis",
              "Jerry Dipoto", "Evan White Mariners", "Scott Servais", "Kyle Seager", "Mariners Baseball"]
    url = "http://api.giphy.com/v1/gifs/search"
    params = urllib.parse.urlencode({
        "q": random.choice(values),
        "api_key": os.environ.get('GIPHY_API_KEY'),
        "limit": "1"
    })
    with urllib.request.urlopen("".join(url, params)) as response:
        data = json.loads(response.read())
    return json.dumps(data, sort_keys=True, indent=4)

import sys

sys.path.append("..")

import requests

r = requests.get("https://api.github.com/events")
print(r)

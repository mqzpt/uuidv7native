# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests<3",
#     "rich",
# ]
#
# [[tool.uv.index]]
# url = "https://example.com/simple"
# ///


import requests
from rich.pretty import pprint

resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])

type Point = tuple[float, float]
print(Point)

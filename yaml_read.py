import yaml
from pprint import pprint

with open("sample.yaml", "r") as f:
    data = yaml.safe_load(f)

for item in data["download"]:
    print(item["link"])

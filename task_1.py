import yaml
from pprint import pprint

with open('config.yaml') as f:
    config = yaml.safe_load(f)
    

if not isinstance(config["maxDepth"], int):
    print("ERROR: maxDepth needs to be integer")
elif config["maxDepth"] < 1:
    print("ERROR: maxDepth needs to be positive")
for x in config:
    if config[x] is None:
        print("ERROR:", x, "is empty")
print("параметры:")
for x in config:
    print(x, "=", config[x])

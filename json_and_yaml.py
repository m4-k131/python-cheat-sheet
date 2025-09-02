import os
import json
import yaml


with open("path/to/my_json.json", encoding="utf-8") as f:
    loaded_json = json.load(f)

with open(os.path.join("path/to/my_json.json"), "w", encoding="utf-8") as f:
    json.dump(loaded_json, f, indent=4)

with open("path/to/my_yaml.yml", "r", encoding="utf-8") as f:
    loaded_yaml = yaml.safe_load(f)

with open("path/to/my_yaml.yml", "w", encoding="utf-8") as f:
    yaml.dump(loaded_yaml, f, default_flow_style=False, indent=4)

import json
import yaml
from pathlib import Path


with open("path/to/my_json.json", encoding="utf-8") as f:
    loaded_json = json.load(f)

with open("path/to/my_json.json", "w", encoding="utf-8") as f:
    json.dump(loaded_json, f, indent=4, allow_nan=True)


output_path = Path("path/to/my_json.json")
# 1. Get the JSON string
json_string = json.dumps(loaded_json, indent=4)

# 2. Write the string to a file
output_path.write_text(json_string, encoding="utf-8")

# --- Serialize to a string ---
# For compact output (e.g., network transfer), use no indent and compact separators.
compact_json_string = json.dumps(data, separators=(',', ':'))
pretty_json_string = json.dumps(data, indent=4)

# --- Deserialize from a string ---
json_string = '{"user": "Alex", "id": 12345}'


import datetime
import json

class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder to handle datetime objects."""
    def default(self, obj):
        if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
            # Convert datetime objects to ISO 8601 string format
            return obj.isoformat()
        return super().default(obj)

my_complex_data = {
    "event": "Project Deadline",
    "timestamp": datetime.datetime.now(datetime.timezone.utc)
}

# Use the custom encoder class with `cls`
json_string = json.dumps(my_complex_data, cls=CustomJSONEncoder, indent=4)
print(json_string)

try:
    data_from_string = json.loads(json_string)
    print("Data from string:", data_from_string)
except json.JSONDecodeError:
    print("Invalid JSON string.")

with open("path/to/my_yaml.yml", "r", encoding="utf-8") as f:
    loaded_yaml = yaml.safe_load(f)

with open("path/to/my_yaml.yml", "w", encoding="utf-8") as f:
    yaml.dump(loaded_yaml, f, default_flow_style=False, indent=4)


# --- Setup ---
# YAML supports more complex structures like anchors and aliases
data = {
    "defaults": {
        "adapter": "postgres",
        "host": "localhost",
    },
    "development": {
        "database": "dev_db",
        "adapter": "postgres", # This could be an alias in pure YAML
        "host": "localhost",
    },
    "production": {
        "database": "prod_db",
        "adapter": "postgres",
        "host": "db.prod.server.com",
    }
}
file_path = Path("config.yml")

# --- Write to YAML file ---
# default_flow_style=False prevents inline formatting {key: value}
# sort_keys=False preserves the original insertion order (in Python 3.7+)
try:
    with file_path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, indent=4)
except IOError as e:
    print(f"Error writing to file {file_path}: {e}")

# --- Read from YAML file ---
try:
    with file_path.open("r", encoding="utf-8") as f:
        # ALWAYS use safe_load to prevent arbitrary code execution
        loaded_data = yaml.safe_load(f)
    print("Successfully loaded YAML:", loaded_data)
except FileNotFoundError:
    print(f"Error: {file_path} not found.")
except yaml.YAMLError as e:
    print(f"Error parsing YAML from {file_path}: {e}")


multi_doc_yaml_string = """
---
user:
  name: alice
  role: admin
---
user:
  name: bob
  role: editor
"""

try:
    # Use safe_load_all for multi-document streams
    documents = list(yaml.safe_load_all(multi_doc_yaml_string))
    for doc in documents:
        print(f"Loaded document for user: {doc['user']['name']}")
except yaml.YAMLError as e:
    print(f"Error parsing YAML: {e}")

from ruamel.yaml import YAML
from pathlib import Path

# ruamel.yaml preserves comments and formatting
yaml_content = """
# User configuration
user:
  name: charlie  # The user's login name
  roles:
    - developer
    - tester
"""
file_path = Path("config_ruamel.yml")
file_path.write_text(yaml_content)

yaml = YAML() # Defaults to a safe loader
with file_path.open('r') as f:
    data = yaml.load(f)

# Modify the data
data['user']['roles'].append('deployer')

# Write it back - comments and structure will be preserved
with file_path.open('w') as f:
    yaml.dump(data, f)
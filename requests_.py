import requests
import json 
import shutil 

headers = {}
data = {}
out_path = ""

with requests.get("", headers=headers, data=json.dumps(data), verify=False, stream=True, timeout=600) as response:
    with open(out_path, "wb") as f:
        shutil.copyfileobj(response.raw, f)
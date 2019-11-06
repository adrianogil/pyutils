import sys
import json


target_json_file = sys.argv[1]

with open(target_json_file, 'r') as f:
    data = json.load(f)

print("Load JSON into dictionary 'data'")

#!/usr/bin env python3
import json
import sys

files = sys.argv[1].split()

result = {}

for f in files:
    result[f] = {"status": "PASS"}

print(json.dumps(result, indent=2))

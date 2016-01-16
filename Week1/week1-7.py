#!/usr/bin/env python
import yaml
import json

from pprint import pprint as pp

with open("yaml_test.yml") as f:
	yaml_file = yaml.load(f)

with open("json_test.json") as f:
	json_file = json.load(f)

print(pp(yaml_file))
print(pp(json_file))
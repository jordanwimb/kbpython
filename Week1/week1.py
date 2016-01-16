#!/usr/bin/env python
import yaml
import json

test_dict = {'router':'ASR9K', 'model':'9010', 'software':'XR 4.3.4'}

test_list = ['jordan', 'wimberley', test_dict, 'switchz']

with open("yaml_test.yml", "w") as f:
	f.write(yaml.dump(test_list, default_flow_style = False))

with open("json_test.json", "w") as f:
	json.dump(test_list, f)

print("Done!")
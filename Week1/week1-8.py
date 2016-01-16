#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse

config = CiscoConfParse("cisco_ipsec.txt")
maps = config.find_objects(r"^crypto map")

def printMaps(maps):
	for line in maps:
		print(line.text)
		for child in line.children:
			print(child.text)

printMaps(maps)
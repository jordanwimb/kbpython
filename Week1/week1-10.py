#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse

config = CiscoConfParse("cisco_ipsec.txt")
group3 = config.find_objects_wo_child(parentspec=r"^crypto map", childspec=r"transform-set AES-")

def findNonAES(groups):
	print("Maps not using AES set:")
	for line in group3:
		print(line.text)
		for child in line.children:
			if "transform-set" in child.text:
				print(child.text)

findNonAES(group3)
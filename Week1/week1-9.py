#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse

config = CiscoConfParse("cisco_ipsec.txt")
group2 = config.find_objects_w_child(parentspec=r"^crypto map", childspec=r"pfs group2")

def findGroup2(groups):
	print("Maps using pfs group 2:")
	for line in group2:
		print(line.text)

findGroup2(group2)
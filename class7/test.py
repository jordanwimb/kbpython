import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", type=str, default="")
parser.add_argument("vlan", type=str)
parser.add_argument("--remove", action="store_true", default=False)
args = parser.parse_args()

print args
print args.name
print args.vlan
print args.remove

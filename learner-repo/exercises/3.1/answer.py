import argparse

parser = argparse.ArgumentParser(description="Double a whole number")
parser.add_argument("number", type=int)
args = parser.parse_args()
print(args.number)

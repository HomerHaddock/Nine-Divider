import argparse
import logic

parser = argparse.ArgumentParser(
    prog="9 Divider",
    description="Divides an integer by nine without using x / 9",
)
parser.add_argument("number", type=int, help="The number to divide by nine")
parser.add_argument('-v', '--verbose', action='store_true')
args = parser.parse_args()
print(args)
print(logic.nearestValidNumber(args.number, args.verbose))
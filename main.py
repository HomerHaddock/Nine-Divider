import argparse
import logic
import inputapi as inp

parser = argparse.ArgumentParser(
    prog="9 Divider",
    description="Divides an integer by nine without using x / 9",
)
parser.add_argument(
    "number",
    type=int,
    nargs="?",
    default="0",
    help="The number to divide by nine, enter nothing to use CLI",
)
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()

if args.number == 0:
    args.number = inp.numerical.integer.newLineInt("Number to divide:", allowNeg=False)
elif args.number < 0:
    raise ValueError("Number must be positive")

print(args)
print(logic.divideWholeByNine(args.number, args.verbose))

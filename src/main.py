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
    default="-1",
    help="The number to divide by nine, enter nothing to use CLI",
)
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-s", "--skip-cache", action="store_true", help="Skips both loading and saving to cache")
args = parser.parse_args()

if args.number == -1:
    args.number = inp.numerical.integer.newLineInt("Number to divide:", allowNeg=False)
elif args.number < 0:
    raise ValueError("Number must be positive")

print(logic.formatResults(logic.divideNumberByNine(args.number, args.verbose, args.skip_cache)))

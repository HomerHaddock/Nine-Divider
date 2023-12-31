from typing import List, Tuple
from cache import loadCache


def splitDigits(number: int) -> List[int]:
    """Splits an integers digits into a list

    Args:
        number (int): The number to split the digits

    Returns:
        List[int]: The numbers digits in a list
    """
    string = str(number)
    digits = list(string)
    return [int(i) for i in digits]


def nearestValidNumber(number: int, verbose: bool = False) -> Tuple[int, int]:
    """
    nearestValidNumber finds the nearest integer that is divisible by nine

    Args:
        number (int): The number to be searched
        verbose (bool): Wether or not to give a verbose output

    Returns:
        Tuple[int, int]: The nearest number that is divisible by nine,
        and the number subtracted from the original number
    """
    if verbose:
        print("Finding nearest valid number.")
    digitList = splitDigits(number)
    total = sum(digitList)
    while total >= 10:
        total = sum(splitDigits(total))

    if total == 9:
        return number, 0

    return number - total, total


def numberToSubtractFrom(number: int, verbose: bool = False) -> int:
    """
    numberToSubtractFrom finds the number to subtract from

    When dividing by nine if the integer's digits adds to nine or a multiple of nine
    you can subtract the first digit of the number to be divided from a multiple of ten
    based on how many times the number passes multiples of 99.
    (e.g. 19 is 10, 99 is 20, 144 is 20)

    Args:
        number (int): The number to search
        verbose (bool, optional): Wether or not the output should be verbose. Defaults to False.

    Returns:
        int: The number to subtract from
    """
    if verbose:
        print("Finding the number to subtract the number from")
    digits = splitDigits(number)
    if len(digits) < 3:
        return 10 if number < 99 else 20

    subtraction = 20
    subtractionCheck = 199
    while subtractionCheck < number:
        subtractionCheck += 99
        subtraction += 10

    return subtraction


def divideWholeByNine(number: int, verbose: bool = False) -> int:
    """
    divideWholeByNine divides the whole number by nine

    Args:
        number (int): Number to be divided (must be divisible by nine)
        verbose (bool, optional): Wether or not the output should be verbose. Defaults to False.

    Returns:
        int: The divided number
    """
    if number == 0:
        return 0
    subtraction = numberToSubtractFrom(number, verbose)
    if verbose:
        print("Dividing valid number")
    digits = splitDigits(number)
    return subtraction - digits[-1]


def divideNumberByNine(
    number: int, verbose: bool = False, skipCache: bool = False
) -> Tuple[int, int]:
    """
    divideNumberByNine divides any whole integer by nine and gives a decimal

    Args:
        number (int): The number to divide by nine (Can be any whole number)
        verbose (bool, optional): Wether or not the output should be verbose. Defaults to False.
        skipCache (bool, optional): Skips both loading and saving to cache. Defaults to False.

    Returns:
        Tuple[int, int]: The number divided by nine (Whole number, Decimal (repeating))
    """
    if not skipCache:
        if verbose:
            print("Checking cache")
        # Return result if in cache
        value = cache.loadValue(str(number))
        if value:
            if verbose:
                print("Answer found in cache")
            return tuple(value)

    if verbose:
        print("Dividing by nine")
        print("Found decimal")

    # Divide number by nine
    valid, decimal = nearestValidNumber(number, verbose)
    dividedWhole = divideWholeByNine(valid, verbose)
    result = (dividedWhole, decimal)

    if not skipCache:
        # Save result to cache
        cache.saveValue(str(number), result)
        cache.saveCache()

    return result


def formatResults(result: Tuple[int, int], verbose: bool = False) -> str:
    """
    formatResults formats the divideNumberByNine into a readable string

    Args:
        result (Tuple[int, int]): The result to format
        verbose (bool, optional): Wether or not the output should be verbose. Defaults to False.

    Returns:
        str: The result formatted to "$WHOLE.($DECIMAL)" or just "$WHOLE" if decimal is 0
    """
    if verbose:
        print("Formatting result")
    if result[1] == 0:
        return str(result[0])
    return "%s.(%s)" % result


cache = loadCache()

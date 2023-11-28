from typing import List, Tuple


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

def joinDigits(digits: List[int]) -> int:
    string = [str(i) for i in digits]
    return int(''.join(string))


def nearestValidNumber(number: int, verbose: bool) -> Tuple[int, int]:
    """
    nearestValidNumber finds the nearest integer that is divisable by nine

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


def numberToSubtractFrom(number: int, verbose: bool) -> int:

    if verbose:
        print("Finding the number to subtract the number from")
    digits = splitDigits(number)
    if len(digits) < 3:
        return 10 if number < 99 else 20

    subtraction = 20
    subtractionCheck = 199
    while subtractionCheck < joinDigits(digits):
        subtractionCheck += 99
        print(subtractionCheck)
        subtraction += 10

    return subtraction

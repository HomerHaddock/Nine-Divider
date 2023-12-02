import sys

sys.path.insert(0, "../src/")
from logic import divideNumberByNine  # noqa: E402


def testDivideZero():
    assert divideNumberByNine(0, skipCache=True) == (0, 0)


def testDivideTwentySix():
    assert divideNumberByNine(26, skipCache=True) == (2, 8)


def testDivideHundredFortyEight():
    assert divideNumberByNine(148, skipCache=True) == (16, 4)


def testDivideTwoHundredFiftySix():
    assert divideNumberByNine(256, skipCache=True) == (28, 4)

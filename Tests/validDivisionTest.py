from logic import divideWholeByNine


def testDivideNine():
    assert divideWholeByNine(9) == 1


def testDivideEighteen():
    assert divideWholeByNine(18) == 2


def testDivideNinetyNine():
    assert divideWholeByNine(99) == 11


def testDivideHundredFortyFour():
    assert divideWholeByNine(144) == 16

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def getMessage(row):
    """
        Return a message tuple representing the text message.
        Assuming that row is an array having 3 elements
    """
    return (row[0], row[1], row[2])


def getCall(row):
    """
        Return a call dictionary representing the call.
        Assuming that row is an array having 4 elements
    """
    return (row[0], row[1], row[2], row[3])


def getUniqueMessageNumbersCount(data, uniqueNumbers):
    """
        This function prints the unique numbers found in textData (array of call records).
        Assumptions:
        1. assumes that the inputs textData contains valid data that can be printed    
    """
    for row in data:
        incoming, answering, _ = getMessage(row)
        uniqueNumbers.add(incoming)
        uniqueNumbers.add(answering)
    return uniqueNumbers


def getUniqueCallNumbersCount(data, uniqueNumbers):
    """
        This function prints the unique numbers found in callData (array of call records).
        Assumptions:
        1. assumes that the inputs callData contains valid data that can be printed    
    """
    for row in data:
        incoming, answering, _, _ = getCall(row)
        uniqueNumbers.add(incoming)
        uniqueNumbers.add(answering)
    return uniqueNumbers


def printUniqueNumber(textData, callData):
    """
        This function prints the unique numbers found in textData (array of text message records)
        and from callData (array of call records).
        Assumptions:
        1. assumes that the inputs textData and callData contains valid data that can be printed
    """
    uniqueNumbers = set()
    getUniqueMessageNumbersCount(textData, uniqueNumbers)
    getUniqueCallNumbersCount(callData, uniqueNumbers)
    print(
        "There are {} different telephone numbers in the records.".format(
            len(uniqueNumbers)
        )
    )


def testGetUniqueMessageNumbers():
    raw = [["97424 22395", "90365 06212", "01-09-2016 06:03:22"]]
    uniqueNumbers = set()
    getUniqueMessageNumbersCount(raw, uniqueNumbers)
    assert len(uniqueNumbers) == 2

    raw = [
        ["97424 22395", "90365 06212", "01-09-2016 06:03:22"],
        ["97424 22395", "90365 06111", "01-09-2016 06:03:22"],
    ]
    uniqueNumbers = set()
    getUniqueMessageNumbersCount(raw, uniqueNumbers)
    assert len(uniqueNumbers) == 3

    print("getUniqueMessageNumbersCount testing completed.")


def testGetUniqueCallNumbersCount():
    raw = [["98447 62998", "(080)46304537", "30-09-2016 23:57:15", "2151"]]
    uniqueNumbers = set()
    getUniqueCallNumbersCount(raw, uniqueNumbers)
    assert len(uniqueNumbers) == 2

    raw = [
        ["98447 62998", "(080)46304537", "30-09-2016 23:57:15", "2151"],
        ["98447 62111", "(080)46304537", "30-09-2016 23:57:15", "2151"],
    ]
    uniqueNumbers = set()
    getUniqueCallNumbersCount(raw, uniqueNumbers)
    assert len(uniqueNumbers) == 3

    print("getUniqueCallNumbersCount testing completed.")


def testAll():
    testGetUniqueMessageNumbers()
    testGetUniqueCallNumbersCount()


printUniqueNumber(texts, calls)

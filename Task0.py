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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def getRow(data, rowIndex):
    """
        Returns the row indicated by rowIndex from data which is assumed to be an array.
        Assuming that rowIndex will be a value from 0 to length of data - 1
    """
    return data[rowIndex]


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


def printFirstTextAndLastCall(textData, callData):
    """
        This function prints the first record from textData (array of text message records)
        and last record from callData (array of call records).
        Assumptions:
        1. assumes that no formatting of phone numbers, dates or duration is required and outputs 
        the values as obtained from the raw file in the print statements.
        2. assumes that the inputs textData and callData contains valid data that can be printed
    """
    firstMessage = getRow(textData, 0)
    incoming, answering, time = getMessage(firstMessage)
    print(
        "First record of texts, {} texts {} at time {}".format(
            incoming, answering, time
        )
    )
    lastCall = getRow(callData, len(callData) - 1)
    incoming, answering, time, duration = getCall(lastCall)
    print(
        "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
            incoming, answering, time, duration
        )
    )


def testGetRow():
    testData = ["First", "Second", "Last"]

    assert getRow(testData, 0) == "First"
    assert getRow(testData, 1) == "Second"
    assert getRow(testData, -1) == "Last"
    print("getRow testing completed.")


def testGetMessage():
    raw = ["97424 22395", "90365 06212", "01-09-2016 06:03:22"]
    incoming, answering, time = getMessage(raw)
    assert incoming == "97424 22395"
    assert answering == "90365 06212"
    assert time == "01-09-2016 06:03:22"
    print("getText testing completed.")


def testGetCall():
    raw = ["98447 62998", "(080)46304537", "30-09-2016 23:57:15", "2151"]
    incoming, answering, time, duration = getCall(raw)
    assert incoming == "98447 62998"
    assert answering == "(080)46304537"
    assert time == "30-09-2016 23:57:15"
    assert duration == "2151"
    print("getCall testing completed.")


def testAll():
    testGetRow()
    testGetMessage()
    testGetCall()


printFirstTextAndLastCall(texts, calls)

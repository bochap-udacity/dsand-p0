"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def getNumberWithHighestDuration(data):
    """
        Return a tuple indicating the telephone number, total time of the number with the most call usage.
        total time includes the calling out and receiving of a call
        Assuming that data is a valid array that contains an array having 4 elements 
        that has data only in Sept 2016
        Assuming that if multiple numbers have the highest duration the first one process will be returned
    """
    numberDuration = {}
    highestNumber = None

    for row in data:
        duration = int(row[3])
        incoming = row[0]
        answering = row[1]
        if incoming not in numberDuration:
            numberDuration[incoming] = 0
        numberDuration[incoming] += duration
        if (
            highestNumber == None
            or numberDuration[highestNumber] < numberDuration[incoming]
        ):
            highestNumber = incoming

        if answering not in numberDuration:
            numberDuration[answering] = 0
        numberDuration[answering] += duration
        if (
            highestNumber == None
            or numberDuration[highestNumber] < numberDuration[answering]
        ):
            highestNumber = answering

    return (highestNumber, numberDuration[highestNumber])


def testGetNumberWithHighestDuration():
    data = [["78130 00821", "98453 94494", "01-09-2016 06:01:12", "186"]]
    number, duration = getNumberWithHighestDuration(data)
    assert number == "78130 00821"
    assert duration == 186

    data = [
        ["78130 00821", "98453 94494", "01-09-2016 06:01:12", "186"],
        ["98453 46196", "78130 00821", "01-09-2016 06:40:20", "2457"],
    ]
    number, duration = getNumberWithHighestDuration(data)
    assert number == "78130 00821"
    assert duration == 2643

    data = [
        ["78130 00821", "98453 94494", "01-09-2016 06:01:12", "186"],
        ["98453 46196", "94005 06213", "01-09-2016 06:40:20", "2457"],
        ["94005 06213", "78130 00821", "01-09-2016 06:46:56", "9"],
    ]
    number, duration = getNumberWithHighestDuration(data)
    assert number == "94005 06213"
    assert duration == 2466

    print("getNumberWithHighestDuration testing completed.")


def testAll():
    testGetNumberWithHighestDuration()


def printLongestCall():
    """
        This function prints the number from callData (array of call records) that contains the highest duration for total calls in September 2016
        Assumptions:
        1. assumes that no formatting of phone numbers is required and outputs 
        those values as obtained from the raw file in the print statements.
        2. assumes that the input callData contains valid data that can be printed
    """
    number, duration = getNumberWithHighestDuration(calls)
    print(
        "{} spent the longest time, {} seconds, on the phone during September 2016".format(
            number, duration
        )
    )


printLongestCall()

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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def getTelemarketerCallNumber(callData):
    """
        Returns a set containing numbers that are telemarketer numbers that make outgoing calls but receive incoming calls.
    """
    numbers = set()
    nonTelemarketerNumbers = set()
    for index in range(len(callData)):
        row = callData[index]
        if row[0] not in nonTelemarketerNumbers:
            numbers.add(row[0])

        if row[1] in numbers:
            nonTelemarketerNumbers.add(row[1])
            numbers.remove(row[1])

    return numbers


def removeMessageNumberForTelemarketerNumbers(textData, numbers):
    for index in range(len(textData)):
        row = textData[index]
        if row[0] in numbers:
            numbers.remove(row[0])
        if row[1] in numbers:
            numbers.remove(row[1])

    return numbers


def testGetTelemarketerCallNumber():
    data = [["78130 00821", "98453 94494", "01-09-2016 06:01:12", "186"]]
    numbers = getTelemarketerCallNumber(data)
    assert len(numbers) == 1
    assert "78130 00821" in numbers

    data = [
        ["78130 00821", "98453 94494", "01-09-2016 06:01:12", "186"],
        ["(0821)6141380", "90366 69257", "01-09-2016 06:54:44", "2147"],
    ]
    numbers = getTelemarketerCallNumber(data)
    assert len(numbers) == 2
    assert "78130 00821" in numbers
    assert "(0821)6141380" in numbers

    data = [
        ["78130 00821", "98453 94494", "01-09-2016 06:01:12", "186"],
        ["(0821)6141380", "78130 00821", "01-09-2016 06:54:44", "2147"],
    ]
    numbers = getTelemarketerCallNumber(data)
    assert len(numbers) == 1
    assert "78130 00821" not in numbers
    assert "(0821)6141380" in numbers

    data = [
        ["78130 00821", "98453 94494", "01-09-2016 06:01:12", "186"],
        ["(0821)6141380", "78130 00821", "01-09-2016 06:54:44", "2147"],
        ["78130 00821", "98453 94494", "04-09-2016 16:11:43", "2672"],
    ]
    numbers = getTelemarketerCallNumber(data)
    assert len(numbers) == 1
    assert "78130 00821" not in numbers
    assert "(0821)6141380" in numbers

    print("getTelemarketerCallNumber testing completed.")


def testRemoveMessageNumberForTelemarketerNumbers():
    numbers = set()
    data = [["97424 22395", "90365 06212", "01-09-2016 06:03:22"]]
    numbers = removeMessageNumberForTelemarketerNumbers(data, numbers)
    assert len(numbers) == 0
    numbers = set({"97424 22395"})
    data = [["97424 22395", "90365 06212", "01-09-2016 06:03:22"]]
    numbers = removeMessageNumberForTelemarketerNumbers(data, numbers)
    assert len(numbers) == 0
    numbers = set({"90365 06212"})
    data = [["97424 22395", "90365 06212", "01-09-2016 06:03:22"]]
    numbers = removeMessageNumberForTelemarketerNumbers(data, numbers)
    assert len(numbers) == 0
    numbers = set({"97424 22395", "90365 06212", "81513 30231", "84313 45689"})
    data = [
        ["97424 22395", "90365 06212", "01-09-2016 06:03:22"],
        ["81513 30231", "90365 06212", "01-09-2016 18:09:40"],
    ]
    numbers = removeMessageNumberForTelemarketerNumbers(data, numbers)
    assert len(numbers) == 1
    assert "84313 45689" in numbers

    print("removeMessageNumberForTelemarketerNumbers testing completed.")


def testAll():
    testGetTelemarketerCallNumber()
    testRemoveMessageNumberForTelemarketerNumbers()


def printTelemarketerNumbers():
    numbers = getTelemarketerCallNumber(calls)
    numbers = removeMessageNumberForTelemarketerNumbers(texts, numbers)
    print("These numbers could be telemarketers: ")
    for number in sorted(numbers):
        print(number)


printTelemarketerNumbers()

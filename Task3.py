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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def getCall(row):
    """
        Return a call dictionary representing the call.
        Assuming that row is an array having 4 elements
    """
    return (row[0], row[1], row[2], row[3])


def getCallingCodes(phoneNumber):
    """
        Returns the calling code for a phone number. () will be removed from calling codes for fixed lines
        Assuming that fixed lines do not have a calling code that is (140)
    """
    if phoneNumber.startswith("140"):
        return "140"
    if (
        phoneNumber.startswith("7")
        or phoneNumber.startswith("8")
        or phoneNumber.startswith("9")
    ):
        return phoneNumber[0:4]

    return phoneNumber[0 : phoneNumber.index(")") + 1]


def testGetCallingCodes():
    assert getCallingCodes("(080)62164823") == "(080)"
    assert getCallingCodes("(0821)3602212") == "(0821)"
    assert getCallingCodes("(04344)322628") == "(04344)"
    assert getCallingCodes("1408371942") == "140"
    assert getCallingCodes("78130 00821") == "7813"
    assert getCallingCodes("89071 31755") == "8907"
    assert getCallingCodes("98446 66723") == "9844"

    print("getCallingCodes testing completed.")


def isBangaloreCallingCode(callingCode):
    """
        Helper function that checks if the callingCode is a Bangalore number (080)
    """
    return callingCode == "(080)"


def getBangaloreCallDetails(data):
    """
        Returns a tuple that contains the total calls made from a Bangalore number,
        the total calls made from a Bangalore number to another Bangalore number and
        the list of unique calling codes called by Bangalore number
    """
    callingCodes = set()
    totalCount = 0
    localCallCount = 0
    for index in range(len(data)):
        incoming, answering, _, _ = getCall(data[index])
        if isBangaloreCallingCode(getCallingCodes(incoming)):
            totalCount += 1
            answeringCallingCode = getCallingCodes(answering)
            callingCodes.add(answeringCallingCode)
            if isBangaloreCallingCode(answeringCallingCode):
                localCallCount += 1

    return totalCount, localCallCount, callingCodes


def testIsBangaloreCallingCode():
    assert isBangaloreCallingCode("(080)") == True
    assert isBangaloreCallingCode("7406") == False
    print("getBangaloreCallDetails testing completed.")


def testGetBangaloreCallDetails():
    data = [["(080)46566171", "(080)40395498", "01-09-2016 21:13:18", "938"]]
    totalCount, localCallCount, callingCodes = getBangaloreCallDetails(data)
    assert totalCount == 1
    assert localCallCount == 1
    assert callingCodes == set({"(080)"})

    data = [["(080)62164823", "74066 93594", "01-09-2016 06:52:07", "300"]]
    totalCount, localCallCount, callingCodes = getBangaloreCallDetails(data)
    assert totalCount == 1
    assert localCallCount == 0
    assert callingCodes == set({"7406"})

    data = [
        ["(080)62164823", "74066 93594", "01-09-2016 06:52:07", "300"],
        ["(080)34121098", "81513 36123", "01-09-2016 10:35:25", "763"],
    ]
    totalCount, localCallCount, callingCodes = getBangaloreCallDetails(data)
    assert totalCount == 2
    assert localCallCount == 0
    assert callingCodes == set({"7406", "8151"})

    data = [
        ["(080)62164823", "74066 93594", "01-09-2016 06:52:07", "300"],
        ["(080)34121098", "81513 36123", "01-09-2016 10:35:25", "763"],
        ["(080)23802940", "98445 71741", "01-09-2016 18:27:19", "2554"],
    ]
    totalCount, localCallCount, callingCodes = getBangaloreCallDetails(data)
    assert totalCount == 3
    assert localCallCount == 0
    assert callingCodes == set({"7406", "8151", "9844"})

    data = [
        ["(080)62164823", "74066 93594", "01-09-2016 06:52:07", "300"],
        ["(080)34121098", "81513 36123", "01-09-2016 10:35:25", "763"],
        ["(080)23802940", "98445 71741", "01-09-2016 18:27:19", "2554"],
        ["90192 87313", "(080)33251027", "01-09-2016 18:18:39", "9"],
    ]
    totalCount, localCallCount, callingCodes = getBangaloreCallDetails(data)
    assert totalCount == 3
    assert localCallCount == 0
    assert callingCodes == set({"7406", "8151", "9844"})

    print("getBangaloreCallDetails testing completed.")


def testAll():
    testGetCallingCodes()
    testIsBangaloreCallingCode()
    testGetBangaloreCallDetails()


def printBangaloreCallDetails():
    totalCount, localCallCount, callingCodes = getBangaloreCallDetails(calls)

    print("The numbers called by people in Bangalore have codes:")
    for callingCode in sorted(callingCodes):
        print(callingCode)

    print(
        "{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
            (localCallCount / totalCount) * 100
        )
    )


printBangaloreCallDetails()

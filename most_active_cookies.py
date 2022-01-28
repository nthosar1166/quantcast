from util import *


def testValidDate():
    print("Testing checkValidDate():")

    test_list = ["2018-12-09",
                 "2018-9-9",
                 "20-12-09",
                 "2021-11-25",
                 "2018/12/09",
                 "a-b-c"]

    for date in test_list:
        if checkCorrectDate(date):
            print("\t{} is valid".format(date))
        else:
            print("\t{} is invalid".format(date))

    print()


def testAppendDict():
    print('Testing appendDict():')

    list_data = [["AtY0laUfhglK3lC7", "2018-12-09"],
                 ["SAZuXPGUrfbcn5UA", "2018-12-09"],
                 ["5UAVanZf6UtGyKVS", "2018-12-09"],
                 ["AtY0laUfhglK3lC7", "2018-12-09"],
                 ["SAZuXPGUrfbcn5UA", "2018-12-08"],
                 ["4sMM2LxV07bPJzwf", "2018-12-08"],
                 ["fbcn5UAVanZf6UtG", "2018-12-08"],
                 ["4sMM2LxV07bPJzwf", "2018-12-07"]]

    dic = {}

    for cookie, data in list_data:
        appendDict(cookie, data, dic)

    printDict(dic)

    print()


def testParseCSV(filename):
    print("Testing parseCSV() on {}:".format(filename))

    dic = parseCSV(filename)

    printDict(dic)

    print()


def testMostActiveCookie(filename):
    print("Testing mostActiveCookie():")

    dic = parseCSV(filename)

    print("\n------dic-------")
    printDict(dic)
    print("----------------\n")

    print("---{}---".format("2018-12-09"))
    mostActiveCookie(dic, "2018-12-09")
    print()

    print("---{}---".format("2018-12-08"))
    mostActiveCookie(dic, "2018-12-08")
    print()

    print("---{}---".format("2018-12-07"))
    mostActiveCookie(dic, "2018-12-07")
    print()

    print("---{}---".format("2018-12-06"))
    mostActiveCookie(dic, "2018-12-06")
    print()


def main():
    testMostActiveCookie("cookies.csv")


if __name__ == "__main__":
    main()

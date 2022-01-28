import csv, sys


def parseCommand(argv):
    if len(argv) < 4 or argv[2] != '-d':
        print("ERROR:  Please put in the correct filepath arguments, as shown below.")
        print("\t./most_active_cookie [csv file] -d [date]")
        sys.exit()

    filename = argv[1]

    date = argv[3]


    if not checkCorrectDate(date):
        print("ERROR: time date doesn't match format yyyy-mm-dd")
        sys.exit()

    return filename, date


def checkCorrectDate(date):
    try:
        year, month, day = date.split("-")
        if not year.isnumeric() or not month.isnumeric() or not day.isnumeric():
            return 0
        if len(year) != 4 or len(month) != 2 or len(day) != 2:
            return 0
        return 1
    except ValueError:
        return 0



def parseCSV(filename):
    dictCookieByDate = dict()

    try:
        fileopen = open(filename, 'r')
        reader = csv.reader(fileopen)

        linecounter = 0

        for line in reader:
            if linecounter == 0 or len(line) == 0:
                linecounter += 1
                continue
            linecounter += 1

            try:
                cookie = line[0]
                timestamp = line[1]
                date, time = timestamp.split("T")

                if not checkCorrectDate(date):
                    raise IndexError

                dictCookieByDate = appendDict(cookie, date, dictCookieByDate)
            except IndexError:
                print("Skipping line {}: in wrong format.".format(linecounter))


    except FileNotFoundError:
        print("ERROR: File not found.")
        sys.exit()

    return dictCookieByDate


def appendDict(cookie, date, dic):
    if date in dic:
        if cookie in dic[date]:
            dic[date][cookie] += 1
        else:
            dic[date][cookie] = 1

    else:
        dic[date] = {cookie: 1}
    return dic


def printDict(dic):
    for date in dic:
        print("date: " + date)
        for cookie in dic[date]:
            print("\t{} : {}".format(cookie, dic[date][cookie]))
    return





def mostActiveCookie(dic, date):
    if date in dic:
        max_cnt = max(dic[date].values())
        for cookie, cnt in dic[date].items():
            if cnt == max_cnt:
                print(cookie)
    else:
        print("No cookies active on {}".format(date))

    return

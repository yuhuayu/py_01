import datetime as dt

def end_of_month(regDate, months):

    addYear = months // 12
    addMonth = months - addYear * 12

    newMonth = regDate.month + addMonth
    if newMonth == 12:
        res = dt.datetime(regDate.year + addYear, newMonth, 31)
    else:
        res = dt.datetime(regDate.year + addYear, newMonth + 1, 1) - dt.timedelta(1)

    return res
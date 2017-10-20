import datetime as dt

def end_of_month(regDate, months):

    newMonth = regDate.month + months
    addYear = newMonth // 12
    newMonth = newMonth % 12

    if newMonth == 12:
        res = dt.datetime(regDate.year + addYear, newMonth, 31)
    else:
        res = dt.datetime(regDate.year + addYear, newMonth + 1, 1) - dt.timedelta(1)
    
    return res


if __name__ == '__main__':

    A = dt.datetime(2011,12,31)
    B = dt.datetime(2008,1,3)
    C = dt.datetime(2007,2,28)
    D = dt.datetime(2008,2,1)

    print (end_of_month(A, 1))
    print (end_of_month(B, 1))
    print (end_of_month(C, 12))
    print (end_of_month(D, 0))
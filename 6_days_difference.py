"""
6. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
def get_year_days(year):#function to get no of days in year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 366
    else:
        return 365


def get_monthdays(month,year):#function to get no of days in month
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        #print("leap year")
    else:
        list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        #print("not a leap year")
    #print(list)
    for i in range(0,12):
        if month == i+1:
            return list[i]


def calculate_diff(day1,month1,year1,day2,month2,year2):
    if year1 == year2:
        if month1 == month2:
            days = day2 - day1
            return days
        else:
            days = 0
            for i in range(month1,month2+1):
                #print("i : ",i)
                #print(get_monthdays(i,year2))
                days += get_monthdays(i,year2)
        #print("months ;",days)
        days -= day1
        #print("after 1 month :",days)
        remaining_days2 = get_monthdays(month2,year2)-day2 + 1
        #print(remaining_days2)
        days -= remaining_days2
        return days
    else:
        days = 0

        for i in range(year1+1,year2):
            #print(i,get_year_days(i))
            days += get_year_days(i)
        for i in range(month1,13):
            #print("i : ",i)
            #print(get_monthdays(i,year1))
            days += get_monthdays(i, year1)
        for i in range(1,month2+1):
            print("i : ", i)
            print(get_monthdays(i, year2))
            days += get_monthdays(i, year2)
        # print("months ;",days)
        days -= day1
        # print("after 1 month :",days)
        remaining_days2 = get_monthdays(month2, year2) - day2 + 1
        # print(remaining_days2)
        days -= remaining_days2
        return days


print(calculate_diff(10,1,2020,10,5,2021))


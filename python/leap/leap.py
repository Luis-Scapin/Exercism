def leap_year(year):
    return year % 4 == 0 and True if year % 100 != 0 else year % 400 == 0

import datetime 
#left off 2:45
#print(dir(datetime))
#or 
#dir(datetime)
#always a good a idea to look at the help() with a new module
#help(datetime)
    #fromt top of help text
#class date(builtins.object)
    #date(year, month, day) -->
gvr = datetime.datee(1956, 1, 31)
#can access year, month, and day separately
print(gvr.year)
print(gvr.month)
print(gvr.day)
#dir(datetime)
#timedelta class, lets you add or subtract a number of days from a date
mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
sum_of_vars = mill + dt
print(sum_of_vars)
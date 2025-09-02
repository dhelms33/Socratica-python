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
gvr = datetime.date(1956, 1, 31)
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
#positive num increase the date, neg number to decrease the date
# day0name, month-name Day-#, Year -> format
#old way to format this
print(gvr.strftime("%A, %B %d, %Y"))

#more modern
message = "GVR was born on {:%A, %B %d, %Y}"
print(message.format(gvr))

#return to dateimte using datetime to know spacex launch date
launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0) #hours, min, sec
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launch_date)
print(launch_time)
print(launch_datetime)

#can get access to individual components 
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)


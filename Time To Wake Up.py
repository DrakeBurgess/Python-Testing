"""
Time To Wake Up
https://github.com/pbeens/ICS-Computer-Studies/blob/master/Challenges/Time%20to%20Wake%20Up.pdf
"""

# imports

# Global Vars
goodData = []
months = []
hours = []

# Read in data file
def readData():
    f = open('Time To Wake Up.txt', 'r')
    lines = f.readlines()
    for line in lines:
        hour = line.strip().split()[4].split(':')[0]
        if hour in ['05', '06', '07']:
            goodData.append(line.strip())

# get months
def getMonths():
    for line in goodData:
        month = line.split()[0]
        if month not in months:
            months.append(month)

# gets hours
def getHour():
    for line in goodData:
        hour = line.split()[4]
        if hour not in hours:
            hours.append(hour)


readData()
getMonths()
getHour()


for elem in hours:
        print (elem)
print(months)
"""
Test Area

s = 'June 11, 2016 at 06:05AM'
items = s.split()

hour = items[4].split(':')[0]
print(hour)
"""
#centimeter to meter and kilometer

num = int(input("Enter number in centimeter : "))

meter = num / 100
kilometer = meter / 1000

print("Number in meter is ", meter)
print("Number in kilometer is ", kilometer)


# Celcius to Farenhide

celcius = int(input("enter temperature in celcius : "))

farenhide = celcius*1.8 + 32

print("Temperature in Farenhude : ", farenhide)


# Farenhide to celcius

farenhide = int(input("enter temperature in Farenhide : "))

celcius = (farenhide - 32) * (5/9)

print("Temperature in Celcius : ", celcius)

#Days conversion

days = (int(input("Enter number of days : ")))

years = days / 365
weeks = (days - (years * 365)) / 7
remaining_days = days - ((years*365) + (weeks*7))

print("years are ",years, "weeks are ",weeks, "Remaining days are ", remaining_days)

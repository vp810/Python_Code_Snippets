import pyodbc
import csv
from datetime import datetime


now = datetime.now()
month = now.month
day = now.day
year = now.year
minute = now.minute
hour = now.hour
second = now.second
file_extension = ".csv"
strMonth = ""
strDay = ""
strMinute = ""
strSecond =""


#if month or minute or seconds is single digit add a zero
def addZeroToSingleNumber(num1):
      if num1 < 10:
        x = "0" + str(num1)
      else:
          x = str(num1)
      return x


strMonth = addZeroToSingleNumber(month)
strDay = addZeroToSingleNumber(day)
strMinute =addZeroToSingleNumber(minute)
strSecond = addZeroToSingleNumber(second)

folder  = r'C:\XXX\YYY\New'


filename = r"\XXX_" + str(year) + "-" + strMonth + "-" + strDay + "-" + strMinute + "-" + strSecond + file_extension

#filename = r"\BHA_FOR_IMPORT" + file_extension
filepath =folder + filename

print("now: ", now)
print("Filename: ", filename)
print("filepath: ", filepath)


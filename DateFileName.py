# import module
from datetime import datetime
import os


path ="C:\\Users\\Public\\Documents\\"



#filepath = 'C:\\Users\\vinhx\\OneDrive\\NOV\SQL\\DPForImport\'
# get current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
print("Current date & time : ", current_datetime)

# convert datetime obj to string
str_current_datetime = str(current_datetime)

# create a file object along with extension
file_name = path + str_current_datetime + ".txt"

print(os.path.join(path, file_name))
file = open(file_name, 'w')

print("File created : ", file.name)
file.close()

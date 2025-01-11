import datetime
import os.path



current_time = datetime.datetime.now()

print("Year:", current_time.year)

print("Month:", current_time.month)
print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)
print("Microsecond:", current_time.microsecond)



current_datetime = datetime.datetime.now().date()

print(current_datetime)

print("Year",current_datetime.year)
print("Month",current_datetime.month)
print("Day",current_datetime.day)


settime = datetime.datetime.now().time()

specifictime = datetime.date(2024, 1, 1)

print(specifictime.year)
print(specifictime.month)
print(specifictime.day)

futuretime = current_time + datetime.timedelta(days=100)

print(futuretime)


teksti = "Hello this is the text i\n wanted to write"
with open("example.txt","w") as file:
    file.write(teksti)

file.path = "example.txt"
file_open()

content = file.read()
print(content)
file.close

with open("example.txt","w") as file:
    lines = file.readLines()
    print(lines)

with open("example.txt", "w") as file:
    line = file.readLine()
    print(line)



if os.path.exists("example.txt"):
    print("files exists!")

















































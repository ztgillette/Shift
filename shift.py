#Zach Gillette
#1/20/22

from datetime import datetime
import time
import os 

os.system("clear") 

#user input
print("Welcome to Sh%" + "ft. \nDeveloped by Zach Gillette\n1/20/22\n\nThis application will tell you how far\nyou are through a shift by showing an\nupdating percentage.\nEnjoy!\n")
start = input("Shift start: ")
end = input("Shift end: ")
advanced = input("Turn on advanced data? (y/n): ")

#fix inputs for manipulation
start_num = 1
end_num = 1
#error checking
if len(start) > 5 or len(end) > 5 or len(start) < 4 or len(end) < 4:
    print("Error: time formatting.")
#short-form
if(len(start) == 4):
    start_num = int(start[0:1]) * 3600 + int(start[2:]) * 60
#shorter_form
if(len(start) == 1):
    start_num = int(start[0:1]) * 3600
#military-form
else:
    start_num = int(start[0:2]) * 3600 + int(start[3:]) * 60

#short-form
if(len(end) == 4):
    end_num = int(end[0:1]) * 3600 + int(end[2:]) * 60
#shorter_form
if(len(start) == 1):
    end_num = int(end[0:1]) * 3600
#military-form
else:
    end_num = int(end[0:2]) * 3600 + int(end[3:]) * 60

current_time = str(datetime.now().time())
current_time_num = (int(current_time[0:2]) * 3600) + (int(current_time[3:5])) * 60 + int(current_time[6:8])

#calculations
diff = end_num - start_num

#loop
run = True
while(run):
    os.system("clear") 

    current_time = str(datetime.now().time())
    current_time_num = (int(current_time[0:2]) * 3600) + (int(current_time[3:5])) * 60 + int(current_time[6:8])
    percent = (current_time_num - start_num) / diff

    if current_time_num > end_num:
        run = False

    #formatting for printing
    percent = percent * 100
    percent_string = str(percent)[0:5] + '%'

    if(advanced == 'y' and run):
        print("Current time:", current_time[0:8])

        hours = int((end_num-current_time_num) / 3600)
        minutes = int((end_num-current_time_num - (hours * 3600)) / 60)
        seconds = int((end_num-current_time_num - ((hours * 3600) + (minutes * 60))))
        
        hours_string = str(hours)
        if(len(hours_string) == 1):
            hours_string = '0' + hours_string

        minutes_string = str(minutes)
        if(len(minutes_string) == 1):
            minutes_string = '0' + minutes_string

        seconds_string = str(seconds)
        if(len(seconds_string) == 1):
            seconds_string = '0' + seconds_string

        time_remaining = hours_string + ':' + minutes_string + ':' + seconds_string

        print("Time remaining:", time_remaining)
        print("Percent of shift remaining:", percent_string)
    elif(run):
        print(percent_string)
    else:
        print("Shift is over.")

    time.sleep(0.25)
    


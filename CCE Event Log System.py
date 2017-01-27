from datetime import *
import csv

# Time and Date Stamps Functions
def file_date_stamp():
    """Returns the current date"""
    now = date.today()
    full_date = "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.year)
    return full_date


def time_stamp():
    """Stamps the time that the guest enters"""
    time_record = datetime.now().strftime("%H:%M:%S")
    return time_record

#Inialize the System
greeting = print("Event Log System")
filename = input("Enter Hostname: ")
welcome_message = print("Welcome to the "+ filename.title() +" event.\n")

# Create File and Label Columns
with open(filename + file_date_stamp() + ".csv", 'a') as file_object:
            file_object.write("Student Name"+","+"ID Number"+","+"Time Entered\n")

# Start Student Input Process
guest_active = True
while guest_active:
    name = input("Enter Fullname: ")
    if name == "End":   # How would you like to end the program?
        guest_active = False
    else:
        id_num = input("Enter Student ID: ")
        print("Welcome to the event, " + name.title() + "!\n")
        with open(filename.title() + file_date_stamp() + ".csv", 'a') as file_object:
            file_object.write(name.title() + "," + id_num + "," + time_stamp() + "\n")
        guest_active = True

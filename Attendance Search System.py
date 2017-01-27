#Import os module
import os
print("Event Attendance Search System")
search = True
while search:
        # Ask the user to enter string to search
        search_path = os.getcwd()
        file_type = ".csv"
        search_str = input("Enter Fullname to search attendance: ")
        print("\nYou have attended the following events:")

        # Append a directory separator if not already present
        if not (search_path.endswith("/") or search_path.endswith("\\") ): 
                search_path = search_path + "/"
                                                                  
        # If path does not exist, set search path to current directory
        if not os.path.exists(search_path):
                search_path ="."

        # Repeat for each file in the directory  
        for fname in os.listdir(path=search_path):

           # Apply file type filter   
           if fname.endswith(file_type):

                # Open file for reading
                fo = open(search_path + fname)

                # Read the first line from the file
                line = fo.readline()

                # Initialize counter for line number
                line_no = 1

                # Loop until EOF
                while line != '' :
                        # Search for string in line
                        index = line.find(search_str.title())
                        if ( index != -1) :
                            print(fname)

                        # Read next line
                        line = fo.readline()  

                        # Increment line counter
                        line_no += 1
        repeat = input("\nNew Search? (y/n): ")
        print("\n")
        if repeat == 'y':
                search=True
        else:
                search=False
                       
                       


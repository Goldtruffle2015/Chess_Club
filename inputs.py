def get_studentID():
    studentID = input("Input the Student ID: ")
    ### --- Check if the StudentID is 8 characters long --- ###
    if len(studentID) == 8:
        ### --- Checks if the ID is a valid integer --- ###
        try:
            ### --- Student ID is valid --- ###
            studentID = int(studentID)
            return str(studentID)
        except:
            ### --- Student ID cannot be turned into an integer --- ###
            print("That is not a valid student ID. Please try again.")
            return get_studentID()
    else:
        ### --- Student ID is not 8 characters long --- ###
        print("That is not a valid student ID. Please try again.")
        return get_studentID()

def get_name():
    first_name = input("Input the first name: ")
    last_name = input("Input the last name: ")
    return first_name, last_name

def input_time():
    try:
        timevar = input("Insert the time (24 hr clock): ")
        ### --- Split the time into hours and minutes --- ###
        timevar = timevar.split(":")
        ### --- Convert each index into an integer to be processed --- ###
        try:
            for i in range(len(timevar)):
                timevar[i] = int(timevar[i])
        except:
            print("Your input is not valid. Please try again.")
            return input_time()
        ### --- Calculate minutes after midnight --- ###
            ### --- Convert the hour variable into minutes --- ###
        timevar[0] = timevar[0]*60
            ### --- Add up all the minutes --- ###
        time_in_minutes = timevar[0] + timevar[1]

        return int(time_in_minutes)
    except:
        print('Please enter a valid time.')
        return input_time()
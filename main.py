'''
Title: Chess Club Tournament Organizer
Author: John Yu
Date: 2018-12-03
'''
# *****************************ADD DRAW#####
queue = []  # This is a list of all the players that are waiting to be matched
volunteer_attendance_li = []  # This is a list of all the volunteers currently present at the tournament
matches = []  # This is a list that keeps track of all the matches happening
leaderboard = []  # This is a list that contains the current standings of all the participants

### --- Code Starts Here --- ###
while True:
    from inputs import *
    from processing import *
    from output import *
    from tkinter import *
    from functools import *
    import csv
    import statistics
    import math


    class main_gui:
        def __init__(self):
            ### --- Get Screen Dimensions --- ###
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            ### --- Get GUI Dimensions --- ###
            width = screen_width
            height = screen_height / 2
            ### --- Center the GUI --- ###
            posx = (screen_width / 2) - (width / 2)
            posy = 0
            ### --- Place the GUI --- ###
            root.geometry('%dx%d+%d+%d' % (width, height, posx, posy))
            root.resizable(False, False)

            container = Frame(root)  # The main frame that holds all of the class objects
            main_gui.configure_dimensions(0, 0, container)
            container.rowconfigure(0, minsize=height)
            container.columnconfigure(0, minsize=width)
            container.grid(row=0, column=0, sticky=N + E + S + W)

            self.frames = {}  # This dictionary stores all of the frame objects we need #
            ### --- Create all the frame objects --- ###

            for i in (player_gui, volunteer_gui, blacklist_gui, menu_gui, insert_matches_gui):
                frame = i(container, self)

                self.frames[i] = frame

                frame.grid(row=0, column=0, sticky=N + E + S + W)

            self.show_frame(menu_gui)

        def configure_dimensions(rownumber, columnnumber, parent):
            ### --- Configure the rows and columns --- ###
            ### --- Rows --- ###
            for y in range(rownumber):
                parent.rowconfigure(y, weight=1)
                ### --- Columns --- ###
            for x in range(columnnumber):
                parent.columnconfigure(x, weight=1)

        def show_frame(self, controller):  # This is used to put the frame we want on top #
            frame = self.frames[controller]
            frame.tkraise()

        @staticmethod
        def menu_choice(var):
            global choice
            choice = var
            root.destroy()


    class menu_gui(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)  # This sets up the class to have all the attributes of a frame #
            main_gui.configure_dimensions(1, 4, self)
            ### --- Create all the buttons --- ###
            ### --- Player Button --- ###
            Button(self, text='Participant Options', bg='red', fg='white',
                   command=lambda: controller.show_frame(player_gui)).grid(row=0, column=0, sticky=N + E + S + W)
            ### --- Volunteer Button --- ###
            Button(self, text='Volunteer Options', bg='yellow', fg='white',
                   command=lambda: controller.show_frame(volunteer_gui)).grid(row=0, column=1, sticky=N + E + S + W)
            ### --- Blacklist Button --- ###
            Button(self, text='Blacklist Options', bg='green', fg='white',
                   command=lambda: controller.show_frame(blacklist_gui)).grid(row=0, column=2, sticky=N + E + S + W)
            ### --- End Button --- ###
            Button(self, text='Exit', bg='red', fg='white', command=lambda: controller.menu_choice(16)).grid(row=0,
                                                                                                             column=3,
                                                                                                             sticky=N + E + S + W)


    class player_gui(Frame):
        def __init__(self, parent, controller):
            self.rownumber = 3
            self.columnnumber = 3
            self.button_names = ['Insert Player into Queue', 'Remove Player from Queue',
                                 'Remove All Players from Queue', 'View Queue', 'View All Participants',
                                 'Create a Match', 'View All Matches', 'Insert Match Results', 'View Leaderboard']
            self.color_pattern = ['peru', 'sandybrown']
            self.starting_index = 1
            Frame.__init__(self, parent)
            main_gui.configure_dimensions(self.rownumber, self.columnnumber, self)
            ### --- Create all the buttons for player's gui --- ###
            for j in range(self.columnnumber):
                for i in range(self.rownumber):
                    ### --- Create the button --- ###
                    index = (j * self.rownumber) + i
                    if index == 7:  # Option 8 opens its own window asking if the game was drawn or won
                        Button(self, text=self.button_names[index], bg=self.color_pattern[(i + j) % 2], fg='white',
                               command=lambda: controller.show_frame(insert_matches_gui)).grid(row=i, column=j,
                                                                                               sticky=N + E + S + W)
                    else:
                        Button(self, text=self.button_names[index], bg=self.color_pattern[(i + j) % 2], fg='white',
                               command=partial(controller.menu_choice,
                                               j * self.rownumber + i + self.starting_index)).grid(row=i, column=j,
                                                                                                   sticky=N + E + S + W)


    class volunteer_gui(Frame):
        def __init__(self, parent, controller):
            self.rownumber = 2
            self.columnnumber = 2
            self.button_names = ['Volunteer Login', 'Volunteer Logout', 'Logout All Volunteers', 'View All Volunteers']
            self.color_pattern = ['sandybrown', 'peru']
            self.starting_index = 10
            Frame.__init__(self, parent)
            main_gui.configure_dimensions(self.rownumber, self.columnnumber, self)
            ### --- Create all the buttons for volunteer's gui --- ###
            for j in range(self.columnnumber):
                for i in range(self.rownumber):
                    ### --- Create the button --- ###
                    index = (j * self.rownumber) + i
                    Button(self, text=self.button_names[index],
                           bg=self.color_pattern[((j * self.rownumber) + i + j) % self.rownumber], fg='white',
                           command=partial(controller.menu_choice, j * self.rownumber + i + self.starting_index)).grid(
                        row=i, column=j, sticky=N + E + S + W)


    class blacklist_gui(Frame):
        def __init__(self, parent, controller):
            self.rownumber = 1
            self.columnnumber = 3
            self.button_names = ['Blacklist Person', 'View Blacklist']
            self.color_pattern = ['peru', 'sandybrown']
            self.starting_index = 14
            Frame.__init__(self, parent)
            main_gui.configure_dimensions(self.rownumber, self.columnnumber, self)
            ### --- Create all the buttons for player's gui --- ###
            for j in range(self.columnnumber - 1):
                for i in range(self.rownumber):
                    ### --- Create the button --- ###
                    index = (j * self.rownumber) + i
                    Button(self, text=self.button_names[index], bg=self.color_pattern[(i + j) % 2], fg='white',
                           command=partial(controller.menu_choice, j * self.rownumber + i + self.starting_index)).grid(
                        row=i, column=j, sticky=N + E + S + W)
            Button(self, text='Back', bg='red', fg='white', command=lambda: controller.show_frame(menu_gui)).grid(row=0,
                                                                                                                  column=2,
                                                                                                                  sticky=N + E + S + W)


    class insert_matches_gui(Frame):
        def __init__(self, parent, controller):
            self.rownumber = 1
            self.columnnumber = 2
            Frame.__init__(self, parent)
            main_gui.configure_dimensions(self.rownumber, self.columnnumber, self)
            ### --- Create all the buttons for insert matches gui --- ###
            Button(self, text='Game Won', bg='peru', fg='white',
                   command=partial(insert_matches_gui.option_func, 1)).grid(row=0, column=0, sticky=N + E + S + W)
            Button(self, text='Game Drawn', bg='sandybrown', fg='white',
                   command=partial(insert_matches_gui.option_func, 2)).grid(row=0, column=1, sticky=N + E + S + W)

        @staticmethod
        def option_func(var):
            global option_8_choice
            global choice  # The function must also set the option to Insert Match Results
            choice = 8
            option_8_choice = var
            root.destroy()


    participants_file_name = "participants.csv"
    volunteers_file_name = "volunteers.csv"
    blacklist_file_name = "blacklist.csv"
    ### --- Menu --- ###
    root = Tk()
    main_gui_obj = main_gui()
    mainloop()
    ### --- Inputs --- ###
    if choice == 1:  # Insert player into queue
        li_of_participants = get_list_from_file(participants_file_name)
        master_volunteer_li = get_list_from_file(volunteers_file_name)
        blacklist_li = get_list_from_file(blacklist_file_name)
        studentID = get_studentID()
        ### --- Check if the student ID is in either the volunteers list or black list --- ###
        if check_if_in_list(studentID, master_volunteer_li) == True:
            i = find_index_from_list(studentID, master_volunteer_li)
            print('%s %s is a already volunteering for the chess tournament.' % (
            master_volunteer_li[i][1], master_volunteer_li[i][2]))
        elif check_if_in_list(studentID, blacklist_li) == True:
            i = find_index_from_list(studentID, blacklist_li)
            print('%s %s is banned from the chess tournament.' % (blacklist_li[i][1], blacklist_li[i][2]))
        else:
            ### --- Check if the player is already in the current list of participants --- ###
            if check_if_in_list(studentID,
                                li_of_participants) == False:  # Player is not in the current list of participants --- ###
                first_name, last_name = get_name()
                add_to_file(li_of_participants, [str(studentID), first_name, last_name, 0, 0, 0, ' '],
                            participants_file_name)
            ### --- Find student ID in queue to prevent duplication --- ###
            if check_if_in_list(studentID, queue) == True:
                print('Player is already in the queue.')
            elif check_if_in_list(studentID, queue) == False:  # Player is not in the queue
                ### --- Get the index of StudentID in list of participants --- ###
                i = find_index_from_list(str(studentID), li_of_participants)
                queue.append(li_of_participants[i])  # Insert player into the queue
    elif choice == 2:  # Remove player from queue
        studentID = get_studentID()
        queue = remove_player_from_queue(queue, studentID)
    elif choice == 3:  # Remove all players from queue
        queue = remove_all_players_from_queue(queue)
    elif choice == 4:  # View Queue
        display_queue(queue)
    elif choice == 5:  # View all participants
        li_of_participants = get_list_from_file(participants_file_name)
        display_all_participants(li_of_participants)
    elif choice == 6:  # Create a match
        li_of_participants = get_list_from_file(participants_file_name)
        if len(queue) > 1:
            ### --- Find a unique match --- ###
            player1, player2 = find_a_unique_match(queue)
            if player2 == None:  # The first person in line has played with everyone in the queue
                queue = turn_index_6_in_li_to_list_mode(queue)
                player2 = find_least_played_match(queue)  # Find the match that was played the least
                queue = turn_index_6_in_li_to_string_mode(queue)
            else:
                pass
            ### --- Determine who plays as black and white --- ###
            white, black = determine_who_plays_as_black_and_white(player1, player2)
            ### --- Output the matchup --- ###
            output_matchup(white, black)
            ### --- Update match history --- ###
            # Player 1 #
            i = find_index_from_list(player1[0],
                                     li_of_participants)  # Used to find player 1 in the list of participants
            li_of_participants = turn_index_6_in_li_to_list_mode(
                li_of_participants)  # Convert the match history from a string to a list
            j = find_index_from_list(player2[0],
                                     li_of_participants[i][6])  # Used to find player 2 in player 1's match history
            if j == None:  # Player 2 is not in player 1's match history
                li_of_participants[i][6].append([player2[0], 1])
            else:
                li_of_participants[i][6][j][1] += 1
            li_of_participants = turn_index_6_in_li_to_string_mode(li_of_participants)

            # Player 2 #
            i = find_index_from_list(player2[0],
                                     li_of_participants)  # Used to find player 2 in the list of participants
            li_of_participants = turn_index_6_in_li_to_list_mode(
                li_of_participants)  # Convert the match history from a string to a list
            j = find_index_from_list(player1[0],
                                     li_of_participants[i][6])  # Used to find player 1 in player 2's match history
            if j == None:  # Player 1 is not in player 2's match history
                li_of_participants[i][6].append([player1[0], 1])
            else:
                li_of_participants[i][6][j][1] += 1
            li_of_participants = turn_index_6_in_li_to_string_mode(li_of_participants)
            ### --- Update games played --- ###
            # White #
            i = find_index_from_list(white[0], li_of_participants)
            # Turn any number in the list into an integer #
            li_of_participants = turn_each_index_into_integers(li_of_participants)
            li_of_participants[i][3] += 1  # Games as white increases by 1
            li_of_participants[i][4] += 1  # Total games played increases by 1
            # Turn all the numbers back into strings #
            li_of_participants = turn_each_index_into_strings(li_of_participants)
            # Black #
            i = find_index_from_list(black[0], li_of_participants)
            # Turn any number in the list into an integer #
            li_of_participants = turn_each_index_into_integers(li_of_participants)
            li_of_participants[i][4] += 1  # Total games played increases by 1
            # Turn all numbers back into strings #
            li_of_participants = turn_each_index_into_strings(li_of_participants)
            ### --- Write changes to file --- ###
            write_to_file(li_of_participants, participants_file_name)
            ### --- Add player 1 and player 2 to the matches list --- ###
            matches.append([white, black])
            ### --- Remove player 1 and player 2 from queue --- ###
            # Find their indexes #
            i = find_index_from_list(player1[0], queue)
            queue.pop(i)
            j = find_index_from_list(player2[0], queue)
            queue.pop(j)
        else:
            print("There are not enough people to start a match.")
    elif choice == 7:  # View all matches
        display_all_matches(matches)
    elif choice == 8:  # Insert match results
        # Get list of participants #
        li_of_participants = get_list_from_file(participants_file_name)
        if len(matches) > 0:
            # Get the student ID of the winner #
            studentID = get_studentID()
            # Look for the student ID among all the matches #
            gohere = True  # Used to determine if the code will output the statement after the for loop
            for each_match in matches:  # For each match that is happening #
                if check_if_in_list(studentID, each_match) == True:
                    # Update Total Points #
                    if option_8_choice == 1:  # Game Won
                        # Winner #
                        i = find_index_from_list(studentID, li_of_participants)
                        winner_index = find_index_from_list(studentID,
                                                            each_match)  # Note: This is used to find the studentID of the loser
                        stdev, z_point = statistics_func(studentID, li_of_participants)
                        points_to_add = 0
                        ### --- Calculate points to be added --- ###
                        if z_point < 0:  # The person who won has a below average score
                            points_to_add = math.floor((stdev / 3) * math.fabs(z_point))
                            '''
                                The added points are to accomodate for people
                                who may not have participated as often in the
                                tournament. This is to give those people more
                                equal opportunity to succeed in the
                                tournament. 
                            '''
                        else:
                            pass
                        li_of_participants[i][5] = int(li_of_participants[i][5])
                        li_of_participants[i][5] += (3 + points_to_add)
                        li_of_participants[i][5] = str(li_of_participants[i][5])
                        # Loser #
                        loser_id = each_match[abs(winner_index - 1)][0]
                        j = find_index_from_list(loser_id, li_of_participants)
                        li_of_participants[j][5] = int(li_of_participants[j][5])
                        li_of_participants[j][5] += 1
                        li_of_participants[j][5] = str(li_of_participants[j][5])
                    elif option_8_choice == 2:  # Game Drawn
                        # Player 1 #
                        player_1 = find_index_from_list(each_match[0][0], li_of_participants)
                        li_of_participants[player_1][5] = int(li_of_participants[player_1][5])
                        li_of_participants[player_1][5] += 2
                        li_of_participants[player_1][5] = str(li_of_participants[player_1][5])
                        # Player 2 #
                        player_2 = find_index_from_list(each_match[1][0], li_of_participants)
                        li_of_participants[player_2][5] = int(li_of_participants[player_2][5])
                        li_of_participants[player_2][5] += 2
                        li_of_participants[player_2][5] = str(li_of_participants[player_2][5])

                    # Add players to the queue #
                    queue.append(li_of_participants[j])  # Insert the loser into the queue
                    queue.append(li_of_participants[i])  # Insert the winner into the queue
                    # Remove players from matches #
                    matches.remove(each_match)
                    # Write changes to file #
                    write_to_file(li_of_participants, participants_file_name)
                    gohere = False
                    break
                else:
                    pass
            if gohere == True:
                i = find_index_from_list(studentID, li_of_participants)
                print('%s %s is not playing any games.' % (li_of_participants[i][1], li_of_participants[i][2]))
            else:
                pass
        else:
            print('There are currently no matches happening.')
    elif choice == 9:  # View leaderboard
        # This is a list that contains the current standings of all the participants
        leaderboard = get_list_from_file(participants_file_name)
        leaderboard.pop(0)  # Remove the prompts #
        # Sort the leaderboard by total points #
        try:
            leaderboard.sort(reverse=True, key=sort_by_score)
            # Display leaderboard #
            display_leaderboard(leaderboard)
        except:
            print('There is currently no one participating in the chess tournament.')
    elif choice == 10:  # Volunteer Login
        master_volunteer_li = get_list_from_file(
            volunteers_file_name)  # This list contains every volunteer registered to help out at the event.
        li_of_participants = get_list_from_file(participants_file_name)
        blacklist_li = get_list_from_file(blacklist_file_name)
        ### --- Inputs --- ###
        time_of_arrival = input_time()
        studentID = get_studentID()
        ### --- Check if the volunteer is already a participant --- ###
        if check_if_in_list(studentID, li_of_participants) == True:
            i = find_index_from_list(studentID, li_of_participants)
            print('%s %s is already participating in the tournament.' % (
            li_of_participants[i][1], li_of_participants[i][2]))
        ### --- Check if the volunteer is black listed --- ###
        elif check_if_in_list(studentID, blacklist_li) == True:
            i = find_index_from_list(studentID, blacklist_li)
            print('%s %s is banned from the chess tournament.' % (blacklist_li[i][1], blacklist_li[i][2]))
        else:
            ### --- If the volunteer was found update the time of arrival in the master volunteer file --- ###
            if check_if_in_list(studentID, master_volunteer_li) == True:
                i = find_index_from_list(str(studentID), master_volunteer_li)
                master_volunteer_li = update_list(master_volunteer_li, i, 3, time_of_arrival)
                write_to_file(master_volunteer_li, volunteers_file_name)
            else:
                ### --- If the volunteer was not found in master put the volunteer into the master list --- ###
                first_name, last_name = get_name()
                add_to_file(master_volunteer_li, [studentID, first_name, last_name, time_of_arrival, 0, 0],
                            volunteers_file_name)
                master_volunteer_li = get_list_from_file(volunteers_file_name)
            ### --- Get the index of studentID in master volunteer list --- ###
            i = find_index_from_list(str(studentID), master_volunteer_li)
            ### --- Put volunteer into volunteer attendance list --- ###
            ### --- Insert the volunteer into volunteer attendance list if not already in it --- ###
            if check_if_in_list(studentID, volunteer_attendance_li) == False:
                volunteer_attendance_li.append(
                    master_volunteer_li[i])  # Insert volunteer into volunteers attendance list
    elif choice == 11:  # Volunteer Logout
        ### --- Get Master Volunteer List --- ###
        master_volunteer_li = get_list_from_file(
            volunteers_file_name)  # This list contains every volunteer registered to help out at the event.
        ### --- Inputs --- ###
        time_finished = input_time()
        studentID = get_studentID()
        ### --- Find the index of the volunteer in the master volunteer list --- ###
        '''
            The function below performs two main tasks:
                1. It finds the index so I can find the time this volunteered started at.
                2. It checks if the volunteer is even logged in. 
        '''
        index = find_index_from_list(str(studentID), volunteer_attendance_li)
        try:
            ### --- Calculate time volunteered --- ###
            time_volunteered = calculate_time_volunteered(int(volunteer_attendance_li[index][3]), time_finished)
            ### --- Calculate total time volunteered --- ###
            ### --- Find the student in the master volunteer list --- ###
            i = find_index_from_list(str(studentID, ), master_volunteer_li)
            total_time_volunteered = int(master_volunteer_li[i][5]) + time_volunteered
            ### --- Remove volunteer from attendance list --- ###
            volunteer_attendance_li = remove_from_list(volunteer_attendance_li, studentID)
            ### --- Update master volunteer list --- ###
            ### --- Update the time finished --- ###
            master_volunteer_li = update_list(master_volunteer_li, i, 4, time_finished)
            ### --- Update the total time volunteered --- ###
            master_volunteer_li = update_list(master_volunteer_li, i, 5, total_time_volunteered)
            ### --- Save changes to volunteers.csv --- ###
            write_to_file(master_volunteer_li, volunteers_file_name)
        except:
            print("The Student ID was not recognized in the volunteer attendance list.")
    elif choice == 12:  # Logout all volunteers
        master_volunteer_li = get_list_from_file(volunteers_file_name)
        if len(volunteer_attendance_li) > 0:
            time_finished = input_time()
            ### --- For each person in the volunteers attendance list --- ###
            for each_volunteer in volunteer_attendance_li:
                ### --- Calculate the time volunteeered --- ###
                time_volunteered = calculate_time_volunteered(int(each_volunteer[3]), time_finished)
                ### --- Calculate the total time volunteered --- ###
                total_time_volunteered = int(each_volunteer[5]) + time_volunteered
                ### --- Add updated information to the master volunteer list --- ###
                # Find the index of the volunteer in the list #
                j = find_index_from_list(each_volunteer[0], master_volunteer_li)
                # Update the time finished #
                update_list(master_volunteer_li, j, 4, time_finished)
                # Update the total time volunteered #
                update_list(master_volunteer_li, j, 5, total_time_volunteered)

            ### --- Remove everyone in the volunteers attendance list --- ###
            volunteer_attendance_li.clear()

            ### --- Update the master volunteer file --- ###
            write_to_file(master_volunteer_li, volunteers_file_name)
        else:
            print("There are no volunteers to remove.")

    elif choice == 13:  # View all volunteers
        master_volunteer_li = get_list_from_file(volunteers_file_name)
        if len(master_volunteer_li) > 1:
            print("STUDENT ID;First Name;Last Name")
            for i in range(1, len(master_volunteer_li)):
                print(master_volunteer_li[i][0] + ";" + master_volunteer_li[i][1] + ";" + master_volunteer_li[i][2])
        else:
            print("There are no volunteers to display.")
    elif choice == 14:  # Blacklist Person
        ### --- Get the necessary files --- ###
        li_of_participants = get_list_from_file(participants_file_name)  # Used to blacklist a player
        master_volunteer_li = get_list_from_file(volunteers_file_name)  # Used to blacklist a volunteer
        blacklist_li = get_list_from_file(blacklist_file_name)
        ### --- Inputs --- ###
        studentID = get_studentID()
        i = find_index_from_list(studentID, li_of_participants)  # Find the person in the list of participants
        ### --- Processing --- ###
        if i == None:  # Person is not in the list of participants
            i = find_index_from_list(studentID, master_volunteer_li)
            if i == None:  # Person is not in the master volunteers list nor the list of participants
                print('The student ID was not recognized.')
            else:  # Person is in the master volunteers list but not in the list of participants
                ### --- Put the player into the blacklist --- ###
                blacklist_li.append(master_volunteer_li.pop(i))
                write_to_file(master_volunteer_li, volunteers_file_name)
                write_to_file(blacklist_li, blacklist_file_name)
        else:  # Person is in the list of participants
            ### --- Put the player into the blacklist --- ###
            blacklist_li.append(li_of_participants.pop(i))
            write_to_file(li_of_participants, participants_file_name)
            write_to_file(blacklist_li, blacklist_file_name)
    elif choice == 15:  # View Blacklist
        blacklist_li = get_list_from_file(blacklist_file_name)
        display_blacklist(blacklist_li)
    elif choice == 16:  # End program
        if len(volunteer_attendance_li) > 0 and len(matches) > 0:
            print('You must insert all match results and logout all volunteers before you can end the program.')
        elif len(matches) > 0:
            print('You must insert all match results before you can end the program.')
        elif len(volunteer_attendance_li) > 0:
            print('You must logout all volunteers before you can end the program.')
        else:
            print('Have a wonderful day.')
            break
    else:  # Theoretically it should never get to this point.
        pass
import csv
import statistics

def get_list_from_file(filename):
    # Format: studentID, first name, last name, games as white, total games played, total points
    ### --- Open CSV File --- ###
    fil = open(filename, newline='')
    fil_reader = csv.reader(fil)

    li = []

    ### --- Put all values into list --- ###
    for line in fil_reader:
        li.append(line)

    return li

def turn_index_6_in_li_to_string_mode(li): # You can only use this with the queue and the list of participants
    '''
    Pro: Finding the student ID in the match history will be easier
    Con: Cannot change the frequency of games played with certain player
    '''
    ### --- Turn li[i][6] into a string --- ###
    for i in range(1, len(li)):
        for j in range(len(li[i][6])):
            try:
                '''
                The list may contain a placeholder 
                written in that I didn't bother 
                trying to remove. I tried removing 
                the placeholder but it was making 
                my code more confusing and making 
                more errors appear out of nowhere 
                so I decided that the placeholder 
                wasn't worth removing. The try is 
                to check if the index is the 
                placeholder.
                '''
                li[i][6][j][1] = str(li[i][6][j][1])
            except:
                pass
            li[i][6][j] = ';'.join(li[i][6][j])
        li[i][6] = ':'.join(li[i][6])
    return li

def turn_index_6_in_li_to_list_mode(li): # You can only use this with the queue and the list of participants
    '''
    Pro: Can change the frequency of games played with certain player
    Con: Very difficult to find student ID in match history. Will require more code than conventional.
    '''
    for i in range(1, len(li)):
        li[i][6] = li[i][6].split(':')
        for j in range(len(li[i][6])):
            li[i][6][j] = li[i][6][j].split(';')
            # Turn li[i][6][j][1] into an integer #
            try:
                li[i][6][j][1] = int(li[i][6][j][1])
            except:
                pass
    return li

def turn_each_index_into_integers(li): # Only works on two dimensional arrays
    for i in range(len(li)):
        for j in range(len(li[i])):
            try:
                li[i][j] = int(li[i][j])
            except:
                pass
    return li

def turn_each_index_into_strings(li): # Only works on two dimensional arrays
    for i in range(len(li)):
        for j in range(len(li[i])):
            li[i][j] = str(li[i][j])
    return li

def add_to_file(li, to_add, filename):
    ### --- Add the new information to the list --- ###
    li.append(to_add)

    ### --- Write the updated list to the CSV file --- ###
    fil = open(filename, "w", newline='')
    fil_writer = csv.writer(fil)

    for i in range(len(li)):
        fil_writer.writerow(li[i])

def write_to_file(li, filename):
    ### --- Write the list fo the CSV file --- ###
    fil = open(filename, 'w', newline='')
    fil_writer = csv.writer(fil)

    for i in range(len(li)):
        fil_writer.writerow(li[i])

def remove_player_from_queue(queue, studentID):
    ### --- Find the player in the queue --- ###
    for i in range(len(queue)):
        if str(studentID) in queue[i]: # Player is found
            student = queue.pop(i) # Remove the player
            print("%s %s has been removed from the queue." % (student[1], student[2]))
            return queue
        else:
            pass
    print("Student ID was not recognized.")
    return queue

def remove_all_players_from_queue(queue):
    if len(queue) > 0:
        queue.clear()
        print('All players have been removed from the queue.')
    else:
        print('There is no one in the queue to remove.')
    return queue

def update_list(li, student_index, var_index, new_info):
    '''
    li: The list you want to update
    Student_index: The student you want to update.
    var_index: The variable you want to update.
    new_var: What you want to replace the old value with
    '''
    li[student_index][var_index] = new_info
    return li


def remove_from_list(li, studentID):
    for i in range(len(li)):
        if studentID in li[i]:
            li[i].pop(i)
            break
        else:
            pass
    return li

def calculate_time_volunteered(time_start, time_end):
    ### --- Make sure that the end time is greater than the start time --- ###
    if time_end < time_start: # This only happens around midnight. I want to do this just in case.
        time_end += 1440 # Add 24 hours to the clock
    net_time = time_end - time_start # These are all measured in minutes
    return net_time

def find_index_from_list(reference, li): # The reference is what the function will be searching for within the list
    # Note: This function only handles two dimensional lists
    for i in range(len(li)):
        if reference in li[i]:
            return i
        else:
            pass
    return

def check_if_in_list(reference, li):
    # Note: This function only handles two dimensional lists
    for i in range(len(li)):
        if reference in li[i]:
            return True
        else:
            pass
    return False

def find_a_unique_match(queue):
    player1 = queue[0] # The first person in line. Represented by Student ID.
    ### --- Find a player the first person in line has not played with yet --- ###
    if queue[0][6] == ' ':
        player2 = queue[1] # Player 2 is just the next person in line.
    else:
        for i in range(1, len(queue)):
            if queue[i][0] in queue[0][6]: # The index 6 for each player is still in string mode
                player2 = None # First in line has played this person before
            else:
                # The first in line has not played this person before #
                player2 = queue[i]
                break

    return player1, player2

def find_least_played_match(queue): # The first person in the queue should have played with everyone behind him in line to get to this point #
    lowest_played_games = 0 # This is to store the lowest number of games played among all players
    ### --- Find the least played game --- ###
    for i in range(1, len(queue)): # For each player other than the first in the queue
        # Find how many games player i has played with the first person in line #
            # Find the first in queue in player i match history #
        for j in range(len(queue[i][6])):
            if queue[0][0] in queue[i][6][j]: # Checks if list contains first person in queue Student ID
                if i == 1:
                    lowest_played_games = queue[i][6][j][1] # If this is the 2nd player in line automatically make lowest played games the 2nd player in line
                else:
                    if queue[i][6][j][1] < lowest_played_games: # Change the value if this player played less games with first person in line
                        lowest_played_games = queue[i][6][j][1]
                    else:
                        pass
    ### --- Find the first person with the lowest played games value --- ###
    for i in range(1, len(queue)):
        ### --- Find first player in line in each persons match history --- ###
        for j in range(len(queue[i][6])):
            try:
                if lowest_played_games == queue[i][6][j][1]:
                    return queue[i] # queue[0] has played queue[i] the least
                else:
                    pass
            except:
                pass

def determine_who_plays_as_black_and_white(player1, player2):
    if int(player1[4]) == 0 or int(player2[4]) == 0: # Checks if either of them has played 0 games.
        if int(player1[4]) == 0 and int(player2[4]) == 0: # Both player 1 and player 2 have never played a game
            white = player1
            black = player2
        else: # At least one of the players has not played a game
            if int(player1[4]) == 0: # If player 1 has not played a game
                white = player1
                black = player2
            elif int(player2[4]) == 0: # If player 2 has not played a game
                white = player2
                black = player1
    else: # Each player should have at least played 1 game. However it does not mean that each have played at least one game as white.
        if int(player1[3])/int(player1[4]) < int(player2[3])/int(player2[4]): # The ratio of player1 white games to total games is less than player2
            white = player1
            black = player2
        elif int(player2[3])/int(player2[4]) < int(player1[3])/int(player1[4]): # The ratio of player2 white games to total games is less than player 1
            white = player2
            black = player1
        else: # It only gets to this point if both ratios are the same in terms of value
            if int(player1[3]) == 0 and int(player2[3]) == 0: # If neither of the players have played a game as white.
                if int(player1[4]) > int(player2[4]): # Player 1 played more total games
                    white = player1
                    black = player2
                elif int(player2[4]) > int(player1[4]): # Player 2 played more total games
                    white = player2
                    black = player1
                else: # Both players played the exact amount of total games and none have ever played as white.
                    white = player1
                    black = player2
            elif int(player1[3]) == 0 or int(player2[3]) == 0: # If one of the players has not played a game as white
                if int(player1[3]) == 0: # Player 1 has not played a game as white
                    white = player1
                    black = player2
                elif int(player2[3]) == 0: # Player 2 has not played a game as white
                    white = player2
                    black = player1
            else: # Both players have the exact same ratio of white games to total games
                white = player1
                black = player2
    return white, black

def sort_by_score(e):
    return int(e[5])

def statistics_func(studentID, li_of_participants):
    list_of_scores = []
    ### --- Create a list of all the different scores --- ###
    for each_person in li_of_participants:
        try:
            list_of_scores.append(int(each_person[4])) # Put their total score into the list
        except:
            pass

    ### --- Calculate necessary Info --- ###
        # Calculate mean #
    mean = float(statistics.mean(list_of_scores))
        # Calculate Standard Deviation #
    stdev = float(statistics.pstdev(list_of_scores, mean))

    ### --- Calculate Z-Point --- ###
        # Find the Player Score #
            # Find the index of the studentID #
    for i in range(len(li_of_participants)):
        if studentID in li_of_participants[i]:
            break
        else:
            pass
    player_score = float(li_of_participants[i][4])
    z_point = float((player_score - mean) / stdev)

    return stdev, z_point
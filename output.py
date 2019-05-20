def display_queue(queue):
    if len(queue) > 0: # Checks if there are any people in the queue
        print("Student ID; First Name; Last Name")
        for i in range(len(queue)):
            print(str(i + 1) + ". " + str(queue[i][0]) + "; " + str(queue[i][1]) + "; " + str(queue[i][2]))
    else:
        print("There is nobody in the queue.")

def display_all_participants(li_participants):
    try:
        # Format: Student ID, First Name, Last Name
        for i in range(len(li_participants)):
            if i == 0:
                print("StudentID; First Name; Last Name")
            if not i == 0:
                print(str(i) + ". " + str(li_participants[i][0]) + "; " + str(li_participants[i][1]) + "; " + str(li_participants[i][2]))
    except:
        print('There is currently no one participating in the chess tournament.')

def output_matchup(white, black):
    print(white[1] + ' ' + white[2] + ' as white will be playing against ' + black[1] + ' ' + black[2] + ' as black.')

def display_all_matches(match_li):
    if len(match_li) > 0: # Checks if there are any matches happening.
        for i in range(len(match_li)):
            print(match_li[i][0][1] + ' ' + match_li[i][0][2] + ' vs ' + match_li[i][1][1] + ' ' + match_li[i][1][2])
    else:
        print("There are currently no matches happening.")

def display_leaderboard(li):
    if len(li) > 0: # Checks if there are any people in the leaderboard
        for i in range(len(li)):
            print('In position %s is %s %s with %s points' % (i + 1, li[i][1], li[i][2], li[i][5]))
    else:
        print('There are currently no players.')

def display_blacklist(li):
    try: # Checks if there are any people in the blacklist
        for i in range(len(li)):
            print('Student ID: %s; First Name; %s; Last Name; %s' % (li[i][0], li[i][1], li[i][2]))
    except:
        print('There is currently no one blacklisted.')
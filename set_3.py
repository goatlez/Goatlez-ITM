'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    Followed = from_member in social_graph[to_member]["following"]
    Follower = to_member in social_graph[from_member]["following"]
    
    if (Followed == False) and (Follower == True):
    
        relationship = "follower"
    
    elif (Followed == True) and (Follower == False):
    
        relationship = "followed by"
    
    elif (Follower == True) and (Followed == True):
    
        relationship = "friends"
    
    elif (Follower == False) and (Followed == False):
    
        relationship = "no relationship"

    else:

        relationship = "error"

    return relationship

def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    #ROW CHECK
    
    for row in board:
    
        row = list(dict.fromkeys(row))
        #REDUCES THE ROW / REMOVES DUPLICATES
    
        if len(row) == 1 and row[0] != '':
    
            return row[0]
    
    #COLUMN CHECK
    
    column = []
    column_index = 0
    
    for all in range(len(board)):
    
        for row in board: 
            column.append(row[column_index])
        
        column_index = column_index + 1
    
        column = list(dict.fromkeys(column))
    
        if len(column) == 1 and column[0] != '':
    
            return column[0]
    
        column = []
    
    #DIAGONAL CHECK
    
    diagonal = []
    diagonal_index = 0
    
    for row in board:
    
        diagonal.append(row[diagonal_index])
        diagonal_index = diagonal_index + 1
    
    diagonal = list(dict.fromkeys(diagonal))
    
    if len(diagonal) == 1 and diagonal[0] != '':
    
        return diagonal[0]
    
    #ANTI-DIAGONAL CHECK
    
    antidiagonal = []
    antidiagonal_index = len(board) - 1
    
    for row in board: 
    
        antidiagonal.append(row[antidiagonal_index])
        antidiagonal_index = antidiagonal_index - 1
    
    antidiagonal = list(dict.fromkeys(antidiagonal))
    
    if len(antidiagonal) == 1 and antidiagonal[0] != '':
    
        return antidiagonal[0]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    #Need to cycle through the values of the dictionary - use the .items function to cycle through and access the values

    current_stop = first_stop
    time = 0

    while current_stop != second_stop:
        
        for (start, end), info in route_map.items():

            if current_stop == start:
                time = time + info["travel_time_mins"]
                current_stop = end
                #assigns the current stop to the end stop in the touple pair, allowing the for loop to cycle
                break
                #exits the for loop once the value is found

    return time


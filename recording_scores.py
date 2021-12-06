from scores import team


# creating team instances

team1 = team('Get a grip')
team2 = team('Chalking rubbish')
team3 = team('Taking the lift')

# recording scores for the teams

    #team 1

team1.add_points('event 1',10)
team1.add_points('event 2', 8)
team1.add_points('event 3', 5)

    #team 2

team2.add_points('event 1', 2)
team2.add_points('event 2', 13)
team2.add_points('event 3', 8)

    #team 3

team3.add_points('event 1', 5)
team3.add_points('event 2', 11)
team3.add_points('event 3', 2)

# Creating a database of all the scored to be converted to a DataFrame

scores_database = []

for i in team.instances:
    scores_database.append(i.scores_database)


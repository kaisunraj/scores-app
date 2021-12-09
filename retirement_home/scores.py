class team:
    instances = []

    def __init__(self, team_name):
        self.__class__.instances.append(self)
        self.team_name = team_name 
        self.points = 0
        self.scores_database = {'Team':self.team_name}
        

    def add_points(self, event, points):
        self.points += points
        self.scores_database[event] = points


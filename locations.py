class Locations:
    def __init__(self):
        self.gameMaps = {'wild': {'town': (10,10), 'cave': (3,3)}, 'town': {'wild': (10, 0)}, 'cave': {'wild': (0, 0)}}
        self.mapETC = {'wild': [ ((10,5), 'rock'), ((11, 5), 'rock'), ((12, 5), 'rock'), ((13, 5), 'rock') ]}
        return

class Locations:
    def __init__(self):
        self.gameMaps = {'wild': {'town': (10,10), 'cave': (3,3)}, 'town': {'wild': (10, 0)}, 'cave': {'wild': (0, 0)}}
        self.mapETC = {'wild': [ ((10,5), 'rock'), ((11, 5), 'rock'), ((12, 5), 'rock'), ((13, 5), 'rock'), ((15, 5), 'rock'), ((16, 5), 'rock'), ((17, 5), 'rock') ]}
        self.mapETC['town'] = [((3,3), 'block'), ((0,3), 'block'),((1,3), 'block'),((2,3), 'block'),((4,3), 'block'),((5,3), 'block'),((6,3), 'block'),((7,3), 'block'),((7,4), 'block'),((7,7), 'block'),((7,8), 'block'),((6,8), 'block'),((5,8), 'block'),((4,8), 'block'),((3,8), 'block'),((2,8), 'block'),((1,8), 'block'),((0,8), 'block')]
        return

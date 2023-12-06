from pprint import pprint
from os import sep

day = "02"
puzzle = "02a"
test = False
inputFile = outputFile =  day + sep + puzzle

if test:
    inputFile += "_test"
    outputFile += "_test"
inputFile += "_input.txt"
outputFile += "_output.txt"

with open(inputFile, 'r') as f:
    data = f.read()
    inputData = data.splitlines()
pprint("Input Data")
pprint(inputData)

if test:
    with open(outputFile, 'r') as f:
        data = f.read()
        outputData = data.splitlines()
    pprint("Expected Output Data")
    pprint(outputData)

################ CODE HERE ######################
class PulledSet:

    validation =  {"red": 12, "blue": 14, "green": 13}

    def __init__(self, inputStr: str) -> None:
        # Parse input
        self.id = int(inputStr.split("Game ")[1].split(":")[0])
        gamesStr = inputStr.split(":")[1].split(';')
        self.games = []
        for game in gamesStr:
            self.games.append(self.parseGame(game))
        
    def parseGame(self, game: str):
        res = {"red": 0,
        "green" : 0,
        "blue" : 0}
        entries = game.split(',')
        for entry in entries:
            values = entry.split(' ')
            tag = values[2]
            res[tag] = max(res[tag], int(values[1]))    
        return res

    def valid(self) -> bool:
        for game in self.games:
            res = True
            if game["red"] > PulledSet.validation["red"]:
                pprint(f"Game {self.id} is invalid as red cubes {game['red']} is more than validation limit {PulledSet.validation['red']}")
                res &= False
            if game["blue"] > PulledSet.validation["blue"]:
                pprint(f"Game {self.id} is invalid as blue cubes {game['blue']} is more than validation limit {PulledSet.validation['blue']}")
                res &= False
            if game["green"] > PulledSet.validation["green"]:
                pprint(f"Game {self.id} is invalid as red cubes {game['green']} is more than validation limit {PulledSet.validation['green']}")
                res &= False
            if res is False:
                return False
        pprint(f"Game {self.id} is valid")
        return True
    
    def power(self) -> int:
        



inputs = []
for line in inputData:
    inputs.append(PulledSet(line))

res = 0
for attempt in inputs:
    if attempt.valid():
        res += attempt.id
        


################ CODE HERE ######################

if test:
    assert(res == int(outputData[0]))
else:
    with open(outputFile, 'w') as f:
        f.write(str(res))
    

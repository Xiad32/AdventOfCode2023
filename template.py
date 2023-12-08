from pprint import pprint
from os import path

day = path.basename(__file__)
day = day[:-2]

test = False
inputFile = day
outputFile = day
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



################ CODE HERE ######################

if test:
    assert(res == int(outputData[0]))
else:
    with open(outputFile, 'w') as f:
        f.write(str(res))
    

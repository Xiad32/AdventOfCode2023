from pprint import pprint

day = "01a"
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

lines = []
for line in inputData:
    first = ""
    last = ""
    for char in line:
        if char.isnumeric():
            last = char
            if first == "":
                first = char
    lines.append(first+last)

res = 0
for line in lines:
    lineValue = int(line)
    res += lineValue

if test:
    assert(res == int(outputData[0]))
else:
    with open(outputFile, 'w') as f:
        f.write(str(res))
    

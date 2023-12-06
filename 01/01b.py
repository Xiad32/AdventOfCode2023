from pprint import pprint

day = "01b"
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
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in inputData:
    first = 0
    last = 0
    for idx in range(len(line)):
        if line[idx].isnumeric():
            last = int(line[idx])
            if first == 0:
                first = int(line[idx])
            continue
        for value, num in enumerate(nums):
            if line[idx:].startswith(num):
                last = value + 1
                if first == 0:
                    first = value + 1
                continue

    lines.append(first*10+last)

res = sum(lines)

if test:
    assert(res == int(outputData[0]))
else:
    with open(outputFile, 'w') as f:
        f.write(str(res))
    

from pprint import pprint
from os import path
from typing import List

day = path.basename(__file__)
day = day[:-3]
test = False
inputFile = day
outputFile = day
if test:
    inputFile += "_test"
    outputFile += "_test"
inputFile += "_input.txt"
outputFile += "_output.txt"

with open("03\\" + inputFile, "r") as f:
    data = f.read()
    inputData = data.splitlines()
pprint("Input Data")
pprint(inputData)

if test:
    with open("03\\" + outputFile, "r") as f:
        data = f.read()
        outputData = data.splitlines()
    pprint("Expected Output Data")
    pprint(outputData)

################ CODE HERE ######################


class NumberEntry:
    value: int
    valueStr: str = ""
    isPartNumber: bool = False

    def __repr__(self) -> str:
        return f"value: {self.value} isPartNumber {self.isPartNumber}"


def extractNumbers(line: str, y: int, board: List[str]) -> List[NumberEntry]:
    res = []
    isInNumber = False
    for x, char in enumerate(line):
        if char.isdigit():
            if isInNumber:
                thisNumberEntry.valueStr += char
                thisNumberEntry.isPartNumber = (
                    thisNumberEntry.isPartNumber or checkSurroundingSymbols(x, y, board)
                )
            else:  #!isInNumber
                thisNumberEntry = NumberEntry()
                thisNumberEntry.valueStr += char
                thisNumberEntry.isPartNumber = (
                    thisNumberEntry.isPartNumber or checkSurroundingSymbols(x, y, board)
                )
                isInNumber = True

        else:  #!isDigit
            if not isInNumber:
                continue
            isInNumber = False
            thisNumberEntry.value = int(thisNumberEntry.valueStr)
            res.append(thisNumberEntry)

    if isInNumber:
        thisNumberEntry.value = int(thisNumberEntry.valueStr)
        res.append(thisNumberEntry)

    return res


def isValidIndex(index, rangeValue):
    return index >= 0 and index < rangeValue


def isSymbol(char: str) -> bool:
    return not (char >= "0" and char <= "9") and char != "."


def checkSurroundingSymbols(x, y, board) -> bool:
    directions = [(-1, 0), (1,   0), #L #R
                  (0, -1), (0,  1),  #U #D
                  (-1, -1), (-1,  1), #LU #LD  
                  (1, 1), (1, -1)]   #RD #RU
    for direction in directions:
        if (
            isValidIndex(x + direction[1], len(board[0]))
            and isValidIndex(y + direction[0], len(board))
            and isSymbol(board[y + direction[0]][x + direction[1]])
        ):
            return True

    return False


res = 0
for y, line in enumerate(inputData):
    numbers = extractNumbers(line, y, inputData)
    pprint(numbers)
    for number in numbers:
        if number.isPartNumber:
            res += number.value


################ CODE HERE ######################

if test:
    assert res == int(outputData[0])
else:
    with open(outputFile, "w") as f:
        f.write(str(res))

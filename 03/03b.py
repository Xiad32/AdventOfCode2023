from pprint import pprint
from os import path, sep
from typing import List

day = path.basename(__file__)
puzzle = day[:-3]
day = day[:-4]

test = False
inputFile = outputFile = day + sep + puzzle

if test:
    inputFile += "_test"
    outputFile += "_test"
inputFile += "_input.txt"
outputFile += "_output.txt"

with open(inputFile, "r") as f:
    data = f.read()
    inputData = data.splitlines()
pprint("Input Data")
pprint(inputData)

if test:
    with open(outputFile, "r") as f:
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


class Coordinates:
    x: int
    y: int


class ProcessedBoard:
    partNumbers: List[List[NumberEntry]] = []
    gears: List[Coordinates] = []
    boardIndexed: List[str] = []
    partNumberIdx: int = '0'
    keys = {'0'}


def extractNumbers(line: str, y: int, board: List[str]) -> List[NumberEntry]:
    isInNumber = False
    ProcessedBoard.partNumberIdx = '0'
    ProcessedBoard.boardIndexed.append(line)
    ProcessedBoard.partNumbers.append([])

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
            if char == "*":
                coord = Coordinates()
                coord.x = x
                coord.y = y
                ProcessedBoard.gears.append(coord)

            if not isInNumber:
                continue
            isInNumber = False
            thisNumberEntry.value = int(thisNumberEntry.valueStr)
            ProcessedBoard.partNumbers[len(ProcessedBoard.partNumbers)-1].append(thisNumberEntry)

            # normalize Index
            idx = x - 1
            charNormalizing = line[idx]
            while idx >= 0 and charNormalizing.isdigit():
                data = list(ProcessedBoard.boardIndexed[y])
                data[idx] = ProcessedBoard.partNumberIdx
                ProcessedBoard.boardIndexed[y] = "".join(data)
                idx -= 1
                charNormalizing = line[idx]
            ProcessedBoard.partNumberIdx = chr(ord(ProcessedBoard.partNumberIdx) + 1)
            ProcessedBoard.keys.add(ProcessedBoard.partNumberIdx)
            pprint(f"Part number Code: {ProcessedBoard.partNumberIdx}" )

    if isInNumber:
        thisNumberEntry.value = int(thisNumberEntry.valueStr)
        ProcessedBoard.partNumbers[len(ProcessedBoard.partNumbers)-1].append(thisNumberEntry)

    return


def isValidIndex(index, rangeValue):
    return index >= 0 and index < rangeValue


def isSymbol(char: str) -> bool:
    return not (char >= "0" and char <= "9") and char != "."


def checkSurroundingSymbols(x, y, board) -> bool:
    directions = [
        (-1, 0),
        (1, 0),  # L #R
        (0, -1),
        (0, 1),  # U #D
        (-1, -1),
        (-1, 1),  # LU #LD
        (1, 1),
        (1, -1),
    ]  # RD #RU
    for direction in directions:
        if (
            isValidIndex(x + direction[1], len(board[0]))
            and isValidIndex(y + direction[0], len(board))
            and isSymbol(board[y + direction[0]][x + direction[1]])
        ):
            return True

    return False


def computeRatio(gear: Coordinates):
    directions = [
        (-1, 0), #L
        (1, 0),  #R
        (0, -1), #U
        (0, 1),  #D 
        (-1, -1),#LU
        (-1, 1), #LD 
        (1, 1),  #RD
        (1, -1), #RU
    ]
    partsIdx = set()
    for direction in directions:
        if isValidIndex(gear.x + direction[1], len(ProcessedBoard.boardIndexed[0])) \
        and isValidIndex(gear.y + direction[0], len(ProcessedBoard.boardIndexed)) \
        and ProcessedBoard.boardIndexed[gear.y + direction[0]][gear.x + direction[1]] in ProcessedBoard.keys:
            partsIdx.add((ProcessedBoard.boardIndexed[gear.y + direction[0]][gear.x + direction[1]], gear.y + direction[0]))

    res = 1
    if len(partsIdx) == 2:
        for partIdx in partsIdx:
            res *= ProcessedBoard.partNumbers[partIdx[1]][ord(partIdx[0]) - ord('0') ].value
        return res

    else:
        return 0

res = 0
for y, line in enumerate(inputData):
    numbers = extractNumbers(line, y, inputData)

for gear in ProcessedBoard.gears:
    res += computeRatio(gear)


################ CODE HERE ######################

if test:
    assert res == int(outputData[0])
else:
    with open(outputFile, "w") as f:
        f.write(str(res))

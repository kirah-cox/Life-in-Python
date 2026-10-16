def main():
    simulateFutureGeneration(100000, glider)

glider = ((0, 0), (1, 0), (2, 0), (2, 1), (1, 2))
offsets = (-1, 0, 1)

def neighbors(x, y):
    neighborList = []
    for xoffset in offsets:
        for yoffset in offsets:
            if (xoffset != 0 or yoffset != 0):
                neighborList.append(((xoffset + x), (yoffset + y)))
    return neighborList

def aliveNeighbors(x, y, aliveList):
    aliveNeighborList = []
    for neighbor in neighbors(x, y):
        if (neighbor in aliveList):
            aliveNeighborList.append(neighbor)
    return aliveNeighborList

def getAllCells(aliveList):
    allCellList = set(aliveList)
    for cell in aliveList:
        allCellList.update(neighbors(cell[0], cell[1]))
    return allCellList

def determineCellSurvival(x, y, aliveList):
        if (len(aliveNeighbors(x, y, aliveList)) == 3):
            return True
        if (((x, y) in aliveList) and (len(aliveNeighbors(x, y, aliveList)) == 2)):
            return True
        else:
            return False

def determineNextGeneration(aliveList):
    aliveCellsList = []
    for cell in getAllCells(aliveList):
        if (determineCellSurvival(cell[0], cell[1], aliveList)):
            aliveCellsList.append(cell)
    return aliveCellsList

def simulateFutureGeneration(n, aliveList):
    for i in range(n):
        aliveList = determineNextGeneration(aliveList)
    print(n, "Generations")
    for cell in aliveList:
        print(cell)
from utils.calcutils import *

def simplexMax(matrix, maxZ):
    maxZ = [i * -1 for i in maxZ]
    maxZ += [0] * 4
    coords = checkLines(matrix, maxZ)
    if coords:
        while coords:
            matrix, maxZ = zeroByPivot(matrix, coords, maxZ)
            coords = checkLines(matrix, maxZ)
    return matrix, maxZ


def checkLines(matrix, maxZ):
    maxZMinIdx = vectorMin(maxZ)
    if maxZ[maxZMinIdx] < 0:
        vector = []
        for row in matrix:
            if row[maxZMinIdx]:
                vector.append(row[-1] / row[maxZMinIdx])
        rowMinIdx = vectorMin(vector)
        return [maxZMinIdx, rowMinIdx]
    else:
        return None        

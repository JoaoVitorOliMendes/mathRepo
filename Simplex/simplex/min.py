from utils.calcutils import *

def simplexMin(matrix, minZ):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] * -1

    minZ += [0] * 4
    coords = checkLines(matrix, minZ)
    if coords:
        while coords:
            pivot = matrix[coords[1]][coords[0]]
            matrix[coords[1]] = [matrix[coords[1]][i]/pivot for i in range(len(matrix[coords[1]]))]
            matrix, minZ = zeroByPivot(matrix, coords, minZ)
            coords = checkLines(matrix, minZ)
    return matrix, minZ


def checkLines(matrix, minZ):
    rsVector = [row[-1] for row in matrix]
    rowMin = vectorMin(rsVector)

    if rsVector[rowMin] < 0:
        vectorMinZDiv = []
        for i in range(len(minZ)):
            if matrix[rowMin][i]:
                x = abs(minZ[i]/matrix[rowMin][i])
                vectorMinZDiv.append(x)
            else:
                vectorMinZDiv.append(0.0)
        minVectorMinZDiv = vectorMinNonZero(vectorMinZDiv[0:-1])
        if minVectorMinZDiv != None:
            return [minVectorMinZDiv, rowMin]
        else:
            return None
    else:
        return None
def vectorMin(vector):
    minIdx = 0
    for i in range(1, len(vector)):
        if vector[i] < vector[minIdx]:
            minIdx = i
    return minIdx

def vectorMax(vector):
    minIdx = 0
    for i in range(1, len(vector)):
        if vector[i] > vector[minIdx]:
            minIdx = i
    return minIdx

def vectorMinNonZero(vector):
    minIdx = None
    for i in range(len(vector)):
        if minIdx == None and vector[i] != 0.0:
            minIdx = i
        elif minIdx != None and vector[i] != 0.0 and vector[i] < vector[minIdx]:
            minIdx = i
    return minIdx

def zeroByPivot(matrix, coords, maxZ):
    minColIdx = coords[0]
    minRowIdx = coords[1]
    pivot = matrix[minRowIdx][minColIdx]

    if pivot:
        for rowIdx in range(len(matrix)):
            if rowIdx != minRowIdx:
                quo = matrix[rowIdx][minColIdx] / pivot
                matrix[rowIdx] = [matrix[rowIdx][i] - (quo * matrix[minRowIdx][i]) for i in range(len(matrix[rowIdx]))]

        quoZ = maxZ[minColIdx] / pivot
        maxZ = [maxZ[i] - (quoZ * matrix[minRowIdx][i]) for i in range(len(maxZ))]
    return matrix, maxZ
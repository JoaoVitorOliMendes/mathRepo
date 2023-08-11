matrix = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
        ]
equals = [1000, 2000, 2500]

matrixLen = len(matrix)

for rowIndex in range(matrixLen):
    pivot = matrix[rowIndex][rowIndex]
    for keyIndex in range(len(matrix[rowIndex])):
        matrix[rowIndex][keyIndex] = matrix[rowIndex][keyIndex] / pivot
    equals[rowIndex] = equals[rowIndex] / pivot

for pivotRowIndex in range(matrixLen):
    pivot = matrix[pivotRowIndex][pivotRowIndex]
    for rowIndex in range(matrixLen):
        if rowIndex != pivotRowIndex:
            quo = matrix[rowIndex][pivotRowIndex] / pivot
            for keyIndex in range(len(matrix[rowIndex])):
                sub = quo * matrix[pivotRowIndex][keyIndex]
                matrix[rowIndex][keyIndex] -= sub
            equals[rowIndex] = equals[rowIndex] - (quo * equals[pivotRowIndex])

for rowIndex in range(matrixLen):
    pivot = matrix[rowIndex][rowIndex]
    for keyIndex in range(len(matrix[rowIndex])):
        matrix[rowIndex][keyIndex] = matrix[rowIndex][keyIndex] / pivot
    equals[rowIndex] = round(equals[rowIndex] / pivot)

print('Result')
print(equals)

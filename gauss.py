matrix = [
        [1, 1, 1],
        [2, 1, 4],
        [2, 3, 5]
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
    print('Pivot: ' + str(matrix[pivotRowIndex][pivotRowIndex]))
    for rowIndex in range(matrixLen):
        print('=================')
        if rowIndex != pivotRowIndex:
            print('Li: ' + str(rowIndex))
            quo = matrix[rowIndex][pivotRowIndex] / pivot
            print('quo: ' + str(matrix[rowIndex][pivotRowIndex]/pivot))
            for keyIndex in range(len(matrix[rowIndex])):
                sub = quo * matrix[pivotRowIndex][keyIndex]
                print('Sub: ' + str(sub))
                matrix[rowIndex][keyIndex] -= sub
            print(equals[rowIndex])
            equals[rowIndex] = equals[rowIndex] - (quo * equals[pivotRowIndex])
            print(equals[rowIndex])
            print(matrix)
            print(equals)

print('Result')
print(equals)
print(matrix)

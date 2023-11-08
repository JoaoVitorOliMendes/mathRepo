def splitInt(string):
    expression = []
    for char in string.split():
        expression.append(float(char))
    return expression

def makeMatrix(exp1, exp2, exp3, control):
    matrix = [exp1, exp2, exp3]
    for i in range(3):
        matrixAppend = [0] * 3
        matrixAppend[i] = control
        matrix[i][-1:-1] = matrixAppend
    return matrix

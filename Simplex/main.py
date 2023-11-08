from utils.stringutils import *
from utils.calcutils import *
from simplex.max import simplexMax
from simplex.min import simplexMin


maxZ = splitInt(input('Informe os valores de Max Z: \n')) # TROCAR MENSAGEM E NOME VARIAVEL
inpX = splitInt(input('Informe a expressão 1:\n'))
inpY = splitInt(input('Informe a expressão 2:\n'))
inpZ = splitInt(input('Informe a expressão 3:\n'))

'''
MIN
matrix = makeMatrix(inpX, inpY, inpZ, -1) *** -1
print(simplexMin(matrix, maxZ))
'''
'''
MAX
matrix = makeMatrix(inpX, inpY, inpZ, 1) *** -1
print(simplexMax(matrix, maxZ))
'''
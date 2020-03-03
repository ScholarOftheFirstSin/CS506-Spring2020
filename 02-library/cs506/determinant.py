
import copy
def caculate_determinant(matrix) :
    if len(matrix) == 0:
        raise ValueError('null matrix error')
    if len(matrix) == 1 :
        return matrix[0][0]
    sum = 0
    for index in range(len(matrix[0])) :
        origin = copy.deepcopy(matrix)
        origin.pop(0)
        for row in origin :
            row.pop(index)
        sum = sum + matrix[0][index] * caculate_determinant(origin) * ((-1) ** (1+index+1))
    return sum










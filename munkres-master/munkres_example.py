from munkres import Munkres, print_matrix
import sys

'''
matrix = [[5, 9, 1],
          [10, 3, 2],
          [8, 7, 4]]


matrix = [[1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0],
          [0, 1, 0, 0, 0],
          [0, 0, 0, 1, 1],
          [0, 0, 0, 1, 1]]

#only one
matrix = [[1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0],
          [0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 1]]

matrix = [[1, 0, 0, 0, 0],
          [0, 1, 0, 1, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 1]]



matrix = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

matrix = [[1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1]]
'''

matrix = [[1, 0, 0, 0, 0],
          [1, 0, 0, 0, 1],
          [1, 0, 0, 1, 0],
          [1, 1, 0, 0, 0],
          [1, 0, 1, 0, 0]]

cost_matrix = []
for row in matrix:
    cost_row = []
    for col in row:
        cost_row += [sys.maxsize - col]
    cost_matrix += [cost_row]

m = Munkres()
indexes = m.compute(cost_matrix)
print_matrix(matrix, msg='Highest profit through this matrix:')
total = 0
for row, column in indexes:
    print "row ", row, "column ", column
    value = matrix[row][column]
    total += value
    print '(%d, %d) -> %d' % (row, column, value)

print 'total profit=%d' % total
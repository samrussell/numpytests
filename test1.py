#!/usr/bin/python

from numpy import matrix

# Create some test matrices

matrix2_3 = matrix([[1, 2, 3],
                    [2, 4, 6],
                    ])

matrix3_5 = matrix([[1, 2, 3, 4 ,5], 
                    [2, 4, 6, 8, 10], 
                    [3, 6, 9, 12 ,15], 
                    ])

print matrix2_3
print matrix3_5

# Test here is 2x3 times 3x5 matrix

matrix2_5 = matrix2_3 * matrix3_5

print matrix2_5

# Test 2 - co-ordinate matrix

matrix3_3_identity = matrix([[1, 0, 0],
                             [0, 1, 0],
                             [0, 0, 1],])

matrix3_3_translation = matrix([[1, 0, 0],
                             [0, 1, 0],
                             [3, 4, 1],])

print matrix3_3_identity * matrix3_3_translation
print matrix3_3_translation * matrix3_3_identity

# affine transform

matrix1_3_coords = matrix([[1,1,1]])

transcoords =  (matrix1_3_coords * matrix3_3_translation)

print transcoords
print transcoords.item(0)
print transcoords.item(1)
print transcoords.item(2)

# print translation matrix

print "translation matrix"

for row in matrix3_3_translation:
  print row


# matrix addition

print matrix3_3_identity + matrix3_3_translation
print matrix3_3_translation + matrix3_3_identity


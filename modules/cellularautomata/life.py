# -*- coding: utf-8 -*-

required_matrices = ['cellular_binary_life']

def in_matrix(matrice, x, y):
    return x >= 0 and y >= 0 and x < matrice[0].size and y < matrice[0].size

def count_neighbors(matrice, y, x):
    count = 0
    for i in xrange(-1,2): for j in xrange(-1,2):
        if in_matrix(matrice, y+i, x+j) and matrice[y+i,x+j]:
            count += 1
    return count
				
def run(world, x, y, matrices):
    cellular_matrix = matrices['cellular_binary_life']
    neighbors = count_neighbors(cellular_matrix,y,x)
    if cellular_matrix[y,x] and neighbors == 2 or neighbors == 3:
	matrices['cellular_binary_life'][y,x] = True
    elif not cellular_matrix[y,x] and neighbors == 3:
	matrices['cellular_binary_life'][y,x] = True
    else:
	matrices['cellular_binary_life'][y,x] = False
	


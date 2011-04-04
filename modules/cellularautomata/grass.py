# -*- coding: utf-8 -*-
# License: See LICENSE file.

import numpy



required_matrices = ['cellular_binary_grass']



def run(world, matrices):
    cellular_matrix = matrices['cellular_binary_grass']
    # Reinterpret cast from bool (stored as uint8) to uint8
    mint = numpy.matrix(cellular_matrix, dtype=numpy.uint8, copy=False)
    # Matrix storing the number of neighbors of each cell
    neighbors = numpy.ndarray(mint.shape, dtype=numpy.uint8)
    # Start by copying a value : presence of a neighbor on the next line, same column
    neighbors.data[:] = numpy.roll(mint, -1, axis=0).data
    # Add the presence of a neighbor on the preceding line, same column
    numpy.add(neighbors, numpy.roll(mint, 1, axis=0), neighbors)
    # Idem for columns, same line
    numpy.add(neighbors, numpy.roll(mint, -1, axis=1), neighbors)
    numpy.add(neighbors, numpy.roll(mint, 1, axis=1), neighbors)
    # Now the preceding/next line, preceding/next column
    numpy.add(neighbors, numpy.roll(numpy.roll(mint, -1, axis=0), -1, axis=1), neighbors)
    numpy.add(neighbors, numpy.roll(numpy.roll(mint, 1, axis=0), -1, axis=1), neighbors)
    numpy.add(neighbors, numpy.roll(numpy.roll(mint, -1, axis=0), 1, axis=1), neighbors)
    numpy.add(neighbors, numpy.roll(numpy.roll(mint, 1, axis=0), 1, axis=1), neighbors)
    # Instead of giving True/False values we use dummy matrices simply to control the output dtype
    true = numpy.ndarray((1,1), dtype=bool); true.fill(True)
    false = numpy.ndarray((1,1), dtype=bool); false.fill(False)
    # We use bitwise operations to process the updates instead of logical operations
    # because it is typically faster.
    # But we have to be sure that True simply corresponds to 0x01, or and's will perform weird
    # As we have complete mastery of the values, only the initialization whould write true True (ie. 1)
    # inside the cells for this need to be asserted.

    #  - Presence of at least 3 neighbors
    neigh4 = numpy.where(neighbors >= 3, true, false)
    #    and the current cell is living = cell will still be living
    cm_n4 = numpy.bitwise_and(cellular_matrix, neigh4)
    # (Inversion of the presence of cells)
    ncm = numpy.bitwise_xor(cellular_matrix, true)
    # - Presence of at least 5 neighbors
    neigh5 = numpy.where(neighbors >= 5, true, false)
    #   and the cell is dead (remember the inversion) = cell will come to life
    numpy.bitwise_and(ncm, neigh5, ncm)
    # Combining the 2 rules by ORs
    numpy.bitwise_or(ncm, cm_n4, cellular_matrix)

    # Tell the matrix we've done a batch update, even if no __setitem__ have been called
    # so that it's colormatrix will in turn be recalculated
    cellular_matrix.set_modified()

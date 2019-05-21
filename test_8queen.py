#!/usr/bin/env python3
from app import BacktrackingNQueensOptimizedSafetyCheck
from app import connection

def get_number_of_solutions():
    nro_soluciones = []
    print()
    for i in range(1,13):
        solver = BacktrackingNQueensOptimizedSafetyCheck(i)
        solver.run()
        nro = solver.get_number_of_solutions()
        nro_soluciones.append(nro)
        print(f' N : {i}, total soluciones : {nro}')
    connection.close()
    return nro_soluciones


# N   distintas       todas las soluciones
# 1     1               1
# 2     0               0
# 3     0               0
# 4     1               2　
# 5     2               10
# 6     1               4　
# 7     6               40
# 8     12              92
# 9     46              352
# 10    92              724
# 11    341             2680
# 12    1787            14200　
# 13    9233            73712
# 14    45752           365596　
# 15    285053          2279184　
# 16    1846955         14772512
# 17    11977939        95815104
# 18    83263591        666090624
# 19    621012754       4968057848
# 20    4878666808      39029188884
# 21    39333324973     314666222712　
# 22    336376244042    2691008701644　

def test_8queen():
    actual = get_number_of_solutions()
    soluciones = [1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596,2279184,2279184,14772512]
    assert all([a == b for a, b in zip(actual, soluciones)])



#!/usr/bin/env python3
from app import BacktrackingNQueensOptimizedSafetyCheck
from app import flat_matrix,save_solutions,connection

if __name__ == "__main__":
    for i in range(1,10):
        solver = BacktrackingNQueensOptimizedSafetyCheck(i)
        for board in solver.get_boards():
            flatten = flat_matrix(board)
            save_solutions(i,board)
            print(i,solver.get_number_of_solutions(), flatten)
    connection.close()
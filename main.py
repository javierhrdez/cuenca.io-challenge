#!/usr/bin/env python3
from app import BacktrackingNQueensOptimizedSafetyCheck
from app import flat_matrix,save_solutions,connection
import datetime
import sys

if __name__ == "__main__":
    start_time = datetime.datetime.now()
    for i in range(1,20):
        solver = BacktrackingNQueensOptimizedSafetyCheck(i)
        for board in solver.get_boards():
            flatten = flat_matrix(board)
            save_solutions(i,board)
            elapsed_time = datetime.datetime.now() - start_time
            print(elapsed_time, i,solver.get_number_of_solutions(), flatten)
            if elapsed_time > datetime.timedelta(minutes=10):
                sys.exit(0)
    connection.close()
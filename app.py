#!/usr/bin/env python3
import sqlalchemy as db
import psycopg2
import time
from functools import wraps
import numpy as np

import socket
import time
import os

port = 5432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        s.connect(('db', port))
        s.close()
        break
    except socket.error as ex:
        time.sleep(0.1)

engine = db.create_engine('postgresql://postgres:password@db:5432/postgres')
connection = engine.connect()
metadata = db.MetaData()


solutions = db.Table(
   'solutions', metadata, 
   db.Column('id', db.Integer, primary_key = True, autoincrement=True), 
   db.Column('chessboard_size', db.Integer), 
   db.Column('solution', db.String), 
)

metadata.create_all(engine)

#https://github.com/edorado93/Save-The-Queens/blob/master/n-queens-backtracking-optimized.py

def timer(func):
   @wraps(func)
   def wrapper(*args, **kwargs):
      start = time.time() * 1000
      func(*args, **kwargs)
      end = time.time() * 1000
      print("Tiempo  de {} es {} ms".format(func.__name__, str(end - start)))
   return wrapper


def flat_matrix(sol):

   sol = np.array(sol)
   a = []
   for i in sol.T:
      result = np.where(i == 1)
      a.append(str(result[0][0]))
   flatten = ",".join(a)
   return flatten

def save_solutions(N,board):
   #save solution in database
   flatten = flat_matrix(board)
   ins = solutions.insert(None).values(chessboard_size = N, solution = flatten)
   connection.execute(ins)


class BacktrackingNQueensOptimizedSafetyCheck:

   def __init__(self, N):
      self.diagonals = {}
      self.anti_diagonals = {}
      self.rows = {}
      self.columns = {}
      self.N = N
      self.board = [[0 for x in np.arange(N)] for y in np.arange(N)]
      self.number_of_solutions = 0
    
   def is_cell_safe(self, r, c):
      if r in self.rows:
         return False
      if c in self.columns:
         return False
      if r - c in self.diagonals:
         return False
      if r + c  in self.anti_diagonals:
         return False

      return True

   def place_a_queen(self, r, c):
      self.rows[r] = True
      self.columns[c] = True
      self.diagonals[r - c] = True
      self.anti_diagonals[r + c] = True
      self.board[r][c] = 1
        

   def undo_placing_a_queen(self, r, c):
      del self.rows[r]
      del self.columns[c]
      del self.diagonals[r - c]
      del self.anti_diagonals[r + c]
      self.board[r][c] = 0

   #@timer
   def get_boards(self):
      for i in self.solve(0):
         yield i

   def run(self):
      for i in self.solve(0):
         pass

  
   def solve(self, column):
      if column == self.N:
         self.number_of_solutions += 1
         yield self.board
 
      for i in range(self.N):
         if self.is_cell_safe(i, column):
            self.place_a_queen(i, column)
            board = self.solve(column + 1)
            if board:
               for x in board:
                  yield x
            self.undo_placing_a_queen(i, column)


   def get_number_of_solutions(self):
      return self.number_of_solutions

   def get_board(self):
      return self.board

#if __name__ == "__main__":
#   for i in range(1,15):
#      solver = BacktrackingNQueensOptimizedSafetyCheck(i)
#      solver.run()
#      print(i,solver.get_number_of_solutions())
#   connection.close()
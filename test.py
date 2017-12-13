#!/usr/bin/python

import os
from random import *

class Board():
  def __init__(self):
    self.cell = [" "," "," "," "," "," "," "," "," "," "]

  def display(self):
    print (" %s | %s | %s " %(self.cell[1], self.cell[2],self.cell[3]))
    print ("-----------")
    print (" %s | %s | %s " %(self.cell[4], self.cell[5],self.cell[6]))
    print ("-----------")
    print (" %s | %s | %s " %(self.cell[7], self.cell[8],self.cell[9]))

  def initial_board(self):
    x = randint(1,9)
    y = randint(1,9)
    if self.cell[x] == " ":
      self.cell[x] = 2
    if self.cell[y] == " ":
      self.cell[y] = 2

  def update_cell(self, cell_no):
    if self.cell[cell_no] == " ":
        self.cell[cell_no] = 2

  def rmove(self,n):
    if self.cell[n] == " ":
       if (self.cell[n-1] == " ") and (self.cell[n-2] != " "):
         self.cell[n] = self.cell[n-2]
         self.cell[n-2] = " "
       elif (self.cell[n-2] == " ") and (self.cell[n-1] != " "):
         self.cell[n] = self.cell[n-1]
         self.cell[n-1] = " "
       elif (self.cell[n-2] != " ") and (self.cell[n-1] != " ") and (self.cell[n-2] == self.cell[n-1]):
         self.cell[n] = self.cell[n-2] + self.cell[n-1]
         self.cell[n-2] = " "
         self.cell[n-1] = " "
       elif self.cell[n-2] != self.cell[n-1]:
         self.cell[n] = self.cell[n-1]
         self.cell[n-1] = self.cell[n-2]
         self.cell[n-2] = " "
    elif self.cell[n] != " ":
      if (self.cell[n-1] == " ") and (self.cell[n-2]!= " ") and (self.cell[n-2]!= self.cell[n]):
        self.cell[n-1] = self.cell[n-2]
        self.cell[n-2] = " "
      elif (self.cell[n-1] == " ") and (self.cell[n-2]!= " ") and (self.cell[n-2] == self.cell[n]):
        self.cell[n] = self.cell[n-2] + self.cell[n]
        self.cell[n-2] = " "
      elif (self.cell[n-2] == " ") and (self.cell[n-1] == self.cell[n]):
        self.cell[n] = self.cell[n-1] + self.cell[n]
        self.cell[n-1] = " "
      elif (self.cell[n-2] == self.cell[n-1]) and (self.cell[n-1] == self.cell[n]):
        self.cell[n] = self.cell[n-1] + self.cell[n]
        self.cell[n-1] = self.cell[n-2]
        self.cell[n-2] = " "
      elif (self.cell[n-2] != " ") and (self.cell[n-1]!= " ") and (self.cell[n-2] == self.cell[n-1]) and (self.cell[n-1] != self.cell[n]):
        self.cell[n-1] = self.cell[n-2] + self.cell[n-1]
        self.cell[n-2] = " "
      elif (self.cell[n-2] != " ") and (self.cell[n-1]!= " ") and (self.cell[n] == self.cell[n-1]) and (self.cell[n-1] != self.cell[n-2]):
        self.cell[n] = self.cell[n] + self.cell[n-1]
        self.cell[n-1] = self.cell[n-2]
        self.cell[n-2] = " "
      
  def lmove(self,n):
    if self.cell[n] == " ":
       if (self.cell[n+1] == " ") and (self.cell[n+2] != " "):
         self.cell[n] = self.cell[n+2]
         self.cell[n+2] = " "
       elif (self.cell[n+2] == " ") and (self.cell[n+1] != " "):
         self.cell[n] = self.cell[n+1]
         self.cell[n+1] = " "
       elif (self.cell[n+2] != " ") and (self.cell[n+1] != " ") and (self.cell[n+2] == self.cell[n+1]):
         self.cell[n] = self.cell[n+2] + self.cell[n+1]
         self.cell[n+2] = " "
         self.cell[n+1] = " "
       elif self.cell[n+2] != self.cell[n+1]:
         self.cell[n] = self.cell[n+1]
         self.cell[n+1] = self.cell[n+2]
         self.cell[n+2] = " "
    elif self.cell[n] != " ":
      if (self.cell[n+1] == " ") and (self.cell[n+2]!= " ") and (self.cell[n+2]!= self.cell[n]):
        self.cell[n+1] = self.cell[n+2]
        self.cell[n+2] = " "
      elif (self.cell[n+1] == " ") and (self.cell[n+2]!= " ") and (self.cell[n+2] == self.cell[n]):
        self.cell[n] = self.cell[n+2] + self.cell[n]
        self.cell[n+2] = " "
      elif (self.cell[n+2] == " ") and (self.cell[n+1] == self.cell[n]):
        self.cell[n] = self.cell[n+1] + self.cell[n]
        self.cell[n+1] = " "
      elif (self.cell[n+2] == self.cell[n+1]) and (self.cell[n+1] == self.cell[n]):
        self.cell[n] = self.cell[n+1] + self.cell[n]
        self.cell[n+1] = self.cell[n+2]
        self.cell[n+2] = " "
      elif (self.cell[n+2] != " ") and (self.cell[n+1]!= " ") and (self.cell[n] == self.cell[n+1]) and (self.cell[n+1] != self.cell[n+2]):
        self.cell[n] = self.cell[n] + self.cell[n+1]
        self.cell[n+1] = self.cell[n+2]
        self.cell[n+2] = " "
      elif (self.cell[n+2] != " ") and (self.cell[n+1]!= " ") and (self.cell[n+2] == self.cell[n+1]) and (self.cell[n] != self.cell[n+2]):
        self.cell[n+1] = self.cell[n+2] + self.cell[n+1]
        self.cell[n+2] = " "

  def umove(self,n):
    if self.cell[n] == " ":
       if (self.cell[n+3] == " ") and (self.cell[n+6] != " "):
         self.cell[n] = self.cell[n+6]
         self.cell[n+6] = " "
       elif (self.cell[n+6] == " ") and (self.cell[n+3] != " "):
         self.cell[n] = self.cell[n+3]
         self.cell[n+3] = " "
       elif (self.cell[n+6] != " ") and (self.cell[n+3] != " ") and (self.cell[n+6] == self.cell[n+3]):
         self.cell[n] = self.cell[n+6] + self.cell[n+3]
         self.cell[n+6] = " "
         self.cell[n+3] = " "
       elif self.cell[n+6] != self.cell[n+3]:
         self.cell[n] = self.cell[n+3]
         self.cell[n+3] = self.cell[n+6]
         self.cell[n+6] = " "
    elif self.cell[n] != " ":
      if (self.cell[n+3] == " ") and (self.cell[n+6]!= " ") and (self.cell[n+6]!= self.cell[n]):
        self.cell[n+3] = self.cell[n+6]
        self.cell[n+6] = " "
      elif (self.cell[n+3] == " ") and (self.cell[n+6]!= " ") and (self.cell[n+6] == self.cell[n]):
        self.cell[n] = self.cell[n+6] + self.cell[n]
        self.cell[n+6] = " "
      elif (self.cell[n+6] == " ") and (self.cell[n+3] == self.cell[n]):
        self.cell[n] = self.cell[n+3] + self.cell[n]
        self.cell[n+3] = " "
      elif (self.cell[n+6] == self.cell[n+3]) and (self.cell[n+3] == self.cell[n]):
        self.cell[n] = self.cell[n+3] + self.cell[n]
        self.cell[n+3] = self.cell[n+6]
        self.cell[n+6] = " "
      elif (self.cell[n+6] != " ") and (self.cell[n+3]!= " ") and (self.cell[n+6] == self.cell[n+3]) and (self.cell[n+3] != self.cell[n]):
        self.cell[n+3] = self.cell[n+6] + self.cell[n+3]
        self.cell[n+6] = " "
      elif (self.cell[n+6] != " ") and (self.cell[n+3]!= " ") and (self.cell[n+6] != self.cell[n+3]) and (self.cell[n+3] == self.cell[n]):
        self.cell[n] = self.cell[n] + self.cell[n+3]
        self.cell[n+3] = self.cell[n+6]
        self.cell[n+6] = " "


  def dmove(self,n):
    if self.cell[n] == " ":
       if (self.cell[n-3] == " ") and (self.cell[n-6] != " "):
         self.cell[n] = self.cell[n-6]
         self.cell[n-6] = " "
       elif (self.cell[n-6] == " ") and (self.cell[n-3] != " "):
         self.cell[n] = self.cell[n-3]
         self.cell[n-3] = " "
       elif (self.cell[n-6] != " ") and (self.cell[n-3] != " ") and (self.cell[n-6] == self.cell[n-3]):
         self.cell[n] = self.cell[n-6] + self.cell[n-3]
         self.cell[n-6] = " "
         self.cell[n-3] = " "
       elif self.cell[n-6] != self.cell[n-3]:
         self.cell[n] = self.cell[n-3]
         self.cell[n-3] = self.cell[n-6]
         self.cell[n-6] = " "
    elif self.cell[n] != " ":
      if (self.cell[n-3] == " ") and (self.cell[n-6]!= " ") and (self.cell[n-6]!= self.cell[n]):
        self.cell[n-3] = self.cell[n-6]
        self.cell[n-6] = " "
      elif (self.cell[n-3] == " ") and (self.cell[n-6]!= " ") and (self.cell[n-6] == self.cell[n]):
        self.cell[n] = self.cell[n-6] + self.cell[n]
        self.cell[n-6] = " "
      elif (self.cell[n-6] == " ") and (self.cell[n-3] == self.cell[n]):
        self.cell[n] = self.cell[n-3] + self.cell[n]
        self.cell[n-3] = " "
      elif (self.cell[n-6] == self.cell[n-3]) and (self.cell[n-3] == self.cell[n]):
        self.cell[n] = self.cell[n-3] + self.cell[n]
        self.cell[n-3] = self.cell[n-6]
        self.cell[n-6] = " "
      elif (self.cell[n-6] != " ") and (self.cell[n-3]!= " ") and (self.cell[n-6] == self.cell[n-3]) and (self.cell[n-3] != self.cell[n]):
        self.cell[n-3] = self.cell[n-6] + self.cell[n-3]
        self.cell[n-6] = " "
      elif (self.cell[n-6] != " ") and (self.cell[n-3]!= " ") and (self.cell[n-6] != self.cell[n-3]) and (self.cell[n-3] == self.cell[n]):
        self.cell[n] = self.cell[n] + self.cell[n-3]
        self.cell[n-3] = self.cell[n-6]
        self.cell[n-6] = " "



  def right_move(self):
    gameboard.rmove(3)
    gameboard.rmove(6)
    gameboard.rmove(9)
           
  def left_move(self):
    gameboard.lmove(1)
    gameboard.lmove(4)
    gameboard.lmove(7)

  def up_move(self):
    gameboard.umove(1)
    gameboard.umove(2)
    gameboard.umove(3)

  def down_move(self):
    gameboard.dmove(7)
    gameboard.dmove(8)
    gameboard.dmove(9)

  def user_choice(self,user_input):
    if user_input == "u":
      gameboard.up_move()
    elif user_input == "d":
      gameboard.down_move()
    elif user_input == "l":
      gameboard.left_move()
    elif user_input == "r":
      gameboard.right_move()

  def win_check(self, num):
    for i in range(1,10):
      if self.cell[i] == num:
        return True 

  def reset(self):
    self.cell = [" "," "," "," "," "," "," "," "," "," "]

gameboard = Board()

select_game = int(raw_input("select the game board to play for: 4, 8, 16, 32,64 :- "))
gameboard.initial_board()
gameboard.display()

while True:
  user_input = raw_input("select the move u for upward direction, d for downwards, l for left and r for Right: ")
  gameboard.user_choice(user_input)
  y =  randint(1,9)
  gameboard.update_cell(y)
  os.system("clear")
  print " playing game board for: %s \n"%(select_game)
  gameboard.display()
  if gameboard.win_check(select_game):
    print "You Win!!! \n"
    play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
    if play_again == "Y":
      gameboard.reset()
      select_game = int(raw_input("select the game board to play for: 4, 8, 16,32,64 :- "))
      gameboard.initial_board()
      gameboard.display()
      continue
    else:
      break





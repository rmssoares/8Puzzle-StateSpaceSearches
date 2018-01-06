'''
Code developed by Nir Oren
Minimally modified by Ricardo Soares
Biggest change: Internal representation
(It's become horizontal, instead of vertical)
------------------------------
University of Aberdeen
MSc Artificial Intelligence
Modified in Python 2.7.14
'''

import sys
from random import randint

class TilePuzzle:
	def __init__(self,size):
		self.size=size
		self.puzzle=[]
		self.zero=(0,0)
		self.moves=["U","D","L","R"]
		count=1
		for i in range(0,size):
			self.puzzle.append([])
			for j in range(0,size):
				self.puzzle[i].append(count)
				count+=1
		self.puzzle[size-1][size-1]=0
		self.zero=(size-1,size-1)

	def readPuzzle(self,string):
		a=string.split(" ")
		count=0
		for i in range(0,self.size):
			for j in range(0,self.size):
				if int(a[count])==0:
					self.zero=(i,j)
				self.puzzle[i][j]=int(a[count])
				count+=1

	def checkPuzzle(self):
		count=1
		for i in range(0,self.size):
			for j in range(0,self.size):
				if self.puzzle[i][j]!=(count%(self.size*self.size)):
					return False
				count+=1
		return True

	
	def swap(self,(x1,y1),(x2,y2)):
		temp=self.puzzle[x1][y1]
		self.puzzle[x1][y1]=self.puzzle[x2][y2]
		self.puzzle[x2][y2]=temp

	def up(self):
		if (self.zero[0]!=0):
			self.swap((self.zero[0]-1,self.zero[1]),self.zero)
			self.zero=(self.zero[0]-1,self.zero[1])
	def down(self):
		if (self.zero[0]!=self.size-1):
			self.swap((self.zero[0]+1,self.zero[1]),self.zero)
			self.zero=(self.zero[0]+1,self.zero[1])

	def left(self):
		if (self.zero[1]!=0):
			self.swap((self.zero[0],self.zero[1]-1),self.zero)
			self.zero=(self.zero[0],self.zero[1]-1)


	def right(self):
		if (self.zero[1]!=self.size-1):
			self.swap((self.zero[0],self.zero[1]+1),self.zero)
			self.zero=(self.zero[0],self.zero[1]+1)
	
	def printPuzzle(self):
		for i in range(0,self.size):
			for j in range(0,self.size):
				print self.puzzle[i][j],
			print ""
			#print 

	def doMove(self,move):
		if move=="U":
			self.up()
		if move=="D":
			self.down()
		if move=="L":
			self.left()
		if move=="R":
			self.right()
	
	def permute(self,numPerm):
		for i in range(0,numPerm):
			self.doMove(self.moves[randint(0,3)])
	
	def parseMoveSequence(self,string):
		for m in string:
			self.doMove(m)
			
		

#t=tilePuzzle(int(sys.argv[1]))
#t.permute(int(sys.argv[2]))
#t.printPuzzle()


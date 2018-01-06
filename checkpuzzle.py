import puzzle
import sys
import math

puzzleString=sys.argv[1]
puzzleArray=puzzleString.split(" ")
p=puzzle.TilePuzzle(int(math.sqrt(len(puzzleArray))))
p.readPuzzle(puzzleString)
p.parseMoveSequence(sys.argv[2])
print(p.checkPuzzle())




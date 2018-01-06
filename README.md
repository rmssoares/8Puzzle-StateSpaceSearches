8-puzzle - State Space Searches
==============================

Overview
--------

The 8-puzzle problem consists of a puzzle composed by (n x n) - 1 tiles, numbered from 1 to n2– 1. The last position that would define the squared form of the puzzle is an empty space, used by the attempting solver to modify the puzzle’s composition, moving one of the adjacent pieces to this space. Our goal state is achieved when every numbered piece is in ascending order and the free space located in the bottom right corner position of the puzzle. To resolve this problem, two uninformed searches (Breadth-First Search and Iterative Deepening Search) and four informed searches (Greedy Search and A* Search, each with two different heuristics) were developed.

This project is built using Python 2.7.14. Part of the original code was created by Nir Oren, and modified by the author, Ricardo Soares.
It was developed for the purpose of Foundations of AI, a course in the MSc Artificial Intelligence, in the University of Aberdeen.

Code Structure
--------
Five classes build the bulk:
- `tilepuzzle.py`, which given an ordered board size and a certain number of permutations to inflict unto, generates a scrambled starting state, which is solved by every algorithm;
- `checkpuzzle.py`, which given a puzzle in a string format and a set of moves to do into such puzzle, checks if a goal state is obtained (which is perfect for testing purposes);
- `puzzle.py`, which implements the TilePuzzle object and its methods;
- `searches.py`, which is consisted by our search algorithms;
- `node.py`, which implements the Node object and its methods.

From these, `tilepuzzle.py`, `puzzle.py` and `checkpuzzle.py` were given by the course’s tutor and have gone through slight modifications to accommodate the student’s resolution. The approach the student has taken goes through running every algorithm orderly, one after the other, by generating a random puzzle. Hence, to run the program, one would do, for example:

`python tilepuzzle.py 3 10`

Generating a 3 by 3 puzzle, with ten permutations caused unto it.

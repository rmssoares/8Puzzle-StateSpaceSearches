# 8-puzzle - State Space Searches

The 8-puzzle problem consists of a puzzle composed by *(n x n) - 1* tiles, numbered from 1 to *n^2*– 1. The last position that would define the squared form of the puzzle is an empty space, used by the attempting solver to modify the puzzle’s composition, moving one of the adjacent pieces to this space. Our goal state is achieved when every numbered piece is in ascending order and the free space located in the bottom right corner position of the puzzle. To resolve this problem, two uninformed searches (Breadth-First Search and Iterative Deepening Search) and four informed searches (*Greedy Search* and *A\* Search*, each with two different heuristics) were developed.

## Code Structure
Five classes build the bulk:
- `tilepuzzle.py`, which given an ordered board size and a certain number of permutations to inflict unto, generates a scrambled starting state, which is solved by every algorithm;
- `checkpuzzle.py`, which given a puzzle in a string format and a set of moves to do into such puzzle, checks if a goal state is obtained (which is perfect for testing purposes);
- `puzzle.py`, which implements the TilePuzzle object and its methods;
- `searches.py`, which is consisted by our search algorithms;
- `node.py`, which implements the Node object and its methods.

From these, `tilepuzzle.py`, `puzzle.py` and `checkpuzzle.py` **were given by the course’s tutor** (*Dr. Nir Oren*, for the course of *Foundations of AI* in the *University of Aberdeen*) and have gone through slight modifications to accommodate the student’s resolution. The approach the student has taken goes through running every algorithm orderly, one after the other, by generating a random puzzle.

## Getting Started

The software provided was entirely done in *Python 2.7*. To start, clone the present repository into your local machine. If you're unaware of how to achieve this, please become familiar with the mechanisms of [GitHub](https://help.github.com/articles/set-up-git) repositories.

```
git clone git@github.com:thyriki/8Puzzle-StateSpaceSearches.git
```

### Prerequisites
Ensure that you have [Python 2.7](https://www.python.org/downloads/) installed and properly set up.

### Instructions

Navigate to the project's folder, and run the following command:

```
python tilepuzzle.py 3 10
```

According to the provided arguments, this would generate a 3 by 3 puzzle, with ten random permutations caused unto it.

## Authors

* **Ricardo Soares** - [rmssoares](https://github.com/rmssoares)

For any inquiries, feel free to open up an issue.


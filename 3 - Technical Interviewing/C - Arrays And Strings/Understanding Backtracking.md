# Understanding Backtracking

## What Is It/How Does It Work

Backtracking algorithms are like problem-solving strategies that help explore different options to find the solution.

- Work by trying out different paths and if one doesn't work, then backtrack and try another until he right one is found. It's like solving a puzzle by testing different pieces until they fit together perfectly.
- Useful for problems where you must generate all valid combinations, permutations, or subsets under constraints. 

Backtracking is a problem-solving algorithmic technique that involves finding a solution incrementally by trying different options and undoing them if they lead to a dead end.

The idea is simple:
    
- Choose – Start by making a choice that could lead toward a solution.
- Explore – Recursively move forward with this choice.
- Check validity – If the choice leads to an invalid state, undo it (backtrack) and try another option.
- Repeat – Continue this process until all possibilities are explored or a valid solution is found.

Backtracking ensures we don’t waste time pursuing impossible paths. Instead, it systematically explores only feasible ones by backing up whenever a choice fails.

It is commonly used in situations where you need to explore multiple possibilities to solve a problem, like searching for a path in a maze or solving puzzles like Sudoku. When a dead end is reached, the algorithm backtracks to the previous decision point and explores a different path until a solution is found or all possibilities have been exhausted.

A backtracking algorithm works by recursively exploring all possible solutions to a problem. It starts by choosing an initial solution, and then it explores all possible extensions of that solution. If an extension leads to a solution, the algorithm returns that solution. If an extension does not lead to a solution, the algorithm backtracks to the previous solution and tries a different extension.

## When To Use It

Backtracking algorithms are best used to solve problems that have the following characteristics:

- There are multiple possible solutions to the problem.
- The problem can be broken down into smaller subproblems.
- The subproblems can be solved independently.

Types of problems typically include:

- Constraint satisfaction problems: When you need to build a solution step by step and must satisfy certain conditions (e.g., N-Queens, Sudoku, Rat in a Maze).
- Search problems: When the solution space is large, but invalid or infeasible branches can be pruned early.
- Multiple solutions: When you need to explore all possible valid solutions, not just one.
- Combinatorial problems: When you must generate all valid combinations, permutations, or subsets under constraints.

## When Not to Use Backtracking

    Greedy or DP fits better: If the problem can be solved directly using a greedy strategy or dynamic programming, backtracking is overkill.
    No pruning possible: If all branches must be explored anyway (no constraints to cut early), brute force or iterative methods may be simpler.
    Large input size: Backtracking can be exponential in time. For very large inputs without strong pruning opportunities, it becomes impractical.
    Single optimal solution: If the task only needs one best solution with clear optimization criteria, algorithms like DP, greedy, or graph search may be faster.

## Applications Of Backtracking

- Solving puzzles (e.g., Sudoku, crossword puzzles)
- Finding the shortest path through a maze
- Scheduling problems
- Resource allocation problems
- Network optimization problems
- Combinatorial problems, such as generating permutations, combinations, or subsets.

## Recursion vs. Backtracking

- Backtracking uses recursion to explore different possibilities.
- Recursion explores all possible paths, without worrying about whether they are valid until the end. Backtracking: Explores only feasible paths, pruning invalid ones as soon as they are detected.
- The control in Recursion is managed automatically by function calls and the call stack. Backtracking manages explicitly using state.
- Recursion solves problems by breaking them into smaller, similar subproblems and solving them recursively. Backtracking solves problems with multiple choices, exploring options systematically, and backtracking when needed.
- Examples of Recursion are, Tree and Graph Traversal, Towers of Hanoi, Divide and Conquer Algorithms, Merge Sort, Quick Sort, and Binary Search. 
- Examples of Backtracking are, N Queen problem, Rat in a Maze problem, Knight’s Tour Problem, Sudoku solver, and Graph coloring problems.


## Links

[Backtracking Algorithm](https://www.geeksforgeeks.org/dsa/backtracking-algorithms/)

[Introduction to Backtracking](https://www.geeksforgeeks.org/dsa/introduction-to-backtracking-2/)
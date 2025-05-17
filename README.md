
# DFS Grid Pathfinding

This Python program implements a **Depth-First Search (DFS)** algorithm to find a path between two randomly selected valid positions (source and goal) in a randomly generated 2D grid.

## 🔍 Overview

* The grid is a square matrix of size `N x N`, where `N` is randomly chosen between 4 and 7.
* Each cell in the grid is either **1 (open path)** or **0 (blocked)**.
* The program randomly selects a valid **source** and **goal** cell (both having value 1 and not the same).
* DFS is performed from the source to find a path to the goal.
* The program outputs:

  * The generated grid
  * The source and goal positions
  * The DFS path
  * The topological order of visited nodes
  * Total moves required to reach the goal

## 📁 Files

* `labreport1.py`: Main Python file containing all code.

## ▶️ How to Run

Ensure you have Python 3 installed. Then run the file:



## 🧠 Classes & Functions

### `Node`

Represents a position in the grid.

* `x, y`: coordinates
* `depth`: depth from the source

### `DFS`

Main class that handles:

* Grid creation
* Source and goal selection
* DFS traversal logic

#### Key Methods:

* `__init__(self, N)`: Initializes the grid and selects valid source and goal.
* `get_valid_positions()`: Ensures both source and goal are on open paths.
* `dfs(x, y, depth)`: Recursive DFS implementation.
* `solve()`: Kicks off the process and prints all results.

## ✅ Sample Output

```
Grid:
1 1 0 1
1 0 1 1
0 1 1 0
1 1 0 1
Source: (0, 1)
Goal: (3, 1)
DFS Path: (0, 1) -> (0, 0) -> (1, 0) -> (2, 1) -> (3, 1)
Topological Order of Traversal: (0, 1) -> (0, 0) -> (1, 0) -> (2, 1) -> (3, 1)
Moves required: 4



## 📌 Notes

* DFS might not always find the shortest path, but it guarantees a path if one exists.
* The grid and positions are randomized for each run.

## 🔧 Future Improvements

* Add visualization using `matplotlib` or `pygame`.
* Add BFS or A\* for shortest path comparison.
* Allow user-defined grid size and manual source/goal input.

---

Let me know if you want this in `.md` format or added to your project directory.

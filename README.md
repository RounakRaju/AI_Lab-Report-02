# AI_Lab-Report-02
# Lab Report 02: A* Search Algorithm Implementation

**Student Information**
**Name: Rounak Hasan Raju** 
**ID: 232002242** 
**University: Green University of Bangladesh**
**Department: CSE**
**Course: Artificial Intelligence Lab (CSE 316)**
This repository contains a Python implementation of the A (A-Star) Search Algorithm*, developed as part of the Artificial Intelligence Lab (CSE 316) course. The project demonstrates how to find the shortest path between a starting point and a target in a 2D grid containing obstacles.
## Objective
The main objective is to implement the A* Search Algorithm and analyze its efficiency in solving shortest path problems in a grid environment. Specific goals include: Understanding how A* Search combines both cost and heuristic to find optimal paths.
Implementing a grid-based system where 0 represents a traversal path and 1 represents an obstacle (wall). Using Manhattan Distance as a heuristic function for estimating distance to the target.Ensuring the algorithm always finds the shortest path when it exists or correctly identifies when no path exists.
## How to Run
Firstly Ensure you have an input.txt file in the directory with the grid and coordinates. Run the Python script:
```bash
python lab2.py

## Example Test Case

**Input:**
```text
4 4
0 0 0 0
1 1 0 1
0 0 0 0
0 1 1 0
0 0
3 3
Start: 0 0
Target: 3 3

**Output:**
```text
Path found with cost 6 using A*
Shortest Path: [(0,0), (0,1), (0,2), (1,2), (2,2), (2,3), (3,3)]

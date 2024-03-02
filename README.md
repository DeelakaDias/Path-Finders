# Path-Finders
This repository contains the implementation of two search algorithms, Depth First Search (DFS) and A*, for finding the shortest path in a six-by-six maze. The programming language used for implementation is Python.

Task 1:

Sets up the maze according to the provided rules, including defining node coordinates, selecting starting and goal nodes, and randomly selecting barrier nodes.
Task 2:

Performs Depth First Search (DFS) on the randomly setup maze.
Outputs the visited nodes list, time taken to find the goal, and the final path.
Follows rules such as processing neighbors in increasing order, allowing valid moves horizontally, vertically, and diagonally, and disallowing moves through barrier nodes.
Task 3:

Develops a function to calculate the heuristic cost for each node using Manhattan distance.
Manhattan distance is calculated as the sum of absolute differences in x and y coordinates between a node and the goal node.
Task 4:

Utilizes the heuristic cost calculated in Task 3 to perform A* search on the maze.
Outputs the visited nodes list, time taken to find the goal, and the final path.
Task 5:

Repeats Tasks 2, 3, and 4 for three different random mazes.
Analyzes the results in terms of completeness, optimality, and time complexity.
Reports the mean and variance of the solution time and path length across the three mazes.
Overall, this repository provides a comprehensive solution to analyzing the efficiency and effectiveness of DFS and A* search algorithms in solving maze problems, considering different maze configurations and heuristic cost calculations.

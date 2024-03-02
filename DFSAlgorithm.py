import MazeGenerator


def valid_move(x, y):
    return 0 <= x < 6 and 0 <= y < 6 and "B" not in MazeGenerator.maze[x][y] # Adjusted indices


def finding_neighbors(x, y):
    neighbors = []
    # Check for left neighbor
    if x != 0 and "B" not in MazeGenerator.maze[x - 1][y]:
        neighbors.append((x - 1, y))
    # Check for top neighbor
    if y != 0 and "B" not in MazeGenerator.maze[x][y - 1]:
        neighbors.append((x, y - 1))
    # Check for bottom neighbor
    if y != 5 and "B" not in MazeGenerator.maze[x][y + 1]:
        neighbors.append((x, y + 1))
    # Check for right neighbor
    if x != 5 and "B" not in MazeGenerator.maze[x + 1][y]:
        neighbors.append((x + 1, y))
    # Check for top-left neighbor
    if x != 0 and y != 0 and "B" not in MazeGenerator.maze[x - 1][y - 1]:
        neighbors.append((x - 1, y - 1))
    # Check for top-right neighbor
    if x != 5 and y != 0 and "B" not in MazeGenerator.maze[x + 1][y - 1]:
        neighbors.append((x + 1, y - 1))
    # Check for bottom-left neighbor
    if x != 0 and y != 5 and "B" not in MazeGenerator.maze[x - 1][y + 1]:
        neighbors.append((x - 1, y + 1))
    # Check for bottom-right neighbor
    if x != 5 and y != 5 and "B" not in MazeGenerator.maze[x + 1][y + 1]:
        neighbors.append((x + 1, y + 1))
    for barrier_node_coordinates in MazeGenerator.barrier_nodes_coordinates_list:
        if barrier_node_coordinates in neighbors:
            neighbors.remove(barrier_node_coordinates)
    return neighbors


def heuristic(goal_node):
    y2, x2 = MazeGenerator.finding_coordinates(goal_node)
    for row in MazeGenerator.maze:
        for node in row:
            y1 = MazeGenerator.maze.index(row)
            x1 = row.index(node)
            MazeGenerator.maze[y1][x1] = abs(int(x1) - int(x2)) + abs(int(y1) - int(y2))
    print("Heuristic added maze: ")
    for row in MazeGenerator.maze:
        print(row)



def depth_first_search(start_node, goal_node):
    stack = [(start_node, [start_node])]  # Using a stack for DFS
    visited = set()

    while stack:
        node, final_route = stack.pop()
        x, y = MazeGenerator.finding_coordinates(node)
        if node == goal_node:
            return final_route
        if node not in visited:
            visited.add(node)
            neighbors = finding_neighbors(x, y)
            neighbors.sort()
            for neighbor_x, neighbor_y in neighbors:
                neighbor_node = neighbor_y * 6 + neighbor_x
                if neighbor_node not in visited:
                    stack.append((neighbor_node, final_route + [neighbor_node]))

    return []

# DFS Search
print("Performing Depth First Search...")
# Performing DFS Search
path_for_DFS = depth_first_search(MazeGenerator.start_node, MazeGenerator.goal_node)
visited_nodes_DFS = path_for_DFS  # Keep it as a list
time_to_find_goal_DFS = len(visited_nodes_DFS)  # Each node takes 1 minute
# Display results
print("Ultimate Route:", path_for_DFS)
print("Time to identify the objective:", time_to_find_goal_DFS, "minutes")
heuristic(MazeGenerator.goal_node)
import MazeGenerator


def heuristic(goal_node):
    y2, x2 = MazeGenerator.finding_coordinates(goal_node)
    for row in MazeGenerator.maze:
        for node in row:
            y1 = MazeGenerator.maze.index(row)
            x1 = row.index(node)
            MazeGenerator.maze[y1][x1] = abs(int(x1) - int(x2)) + abs(int(y1) - int(y2))
    print(MazeGenerator.maze)


# heuristic(MazeGenerator.goal_node)


def valid_move(x, y):
    return 0 <= x < 6 and 0 <= y < 6 and MazeGenerator.maze[y][x] != "B"


def finding_neighbors(x, y):
    neighbors = []

    # Check for left neighbor
    if x != 0 and "B" not in MazeGenerator.maze[y][x - 1]:
        neighbors.append((x - 1, y))

    # Check for top neighbor
    if y != 0 and "B" not in MazeGenerator.maze[y - 1][x]:
        neighbors.append((x, y - 1))

    # Check for bottom neighbor
    if y != 5 and "B" not in MazeGenerator.maze[y + 1][x]:
        neighbors.append((x, y + 1))

    # Check for right neighbor
    if x != 5 and "B" not in MazeGenerator.maze[y][x + 1]:
        neighbors.append((x + 1, y))

    # Check for top-left neighbor
    if x != 0 and y != 0 and "B" not in MazeGenerator.maze[y - 1][x - 1]:
        neighbors.append((x - 1, y - 1))

    # Check for top-right neighbor
    if x != 5 and y != 0 and "B" not in MazeGenerator.maze[y - 1][x + 1]:
        neighbors.append((x + 1, y - 1))

    # Check for bottom-left neighbor
    if x != 0 and y != 5 and "B" not in MazeGenerator.maze[y + 1][x - 1]:
        neighbors.append((x - 1, y + 1))

    # Check for bottom-right neighbor
    if x != 5 and y != 5 and "B" not in MazeGenerator.maze[y + 1][x + 1]:
        neighbors.append((x + 1, y + 1))

    for barrier_node_coordinates in MazeGenerator.barrier_nodes_coordinates_list:
        if barrier_node_coordinates in neighbors:
            neighbors.remove(barrier_node_coordinates)

    return neighbors


def a_star_search(start_node, goal_node):
    open_set = [(0, start_node, [])]
    closed_set = set()

    while open_set:
        open_set.sort()  # Sort the open set based on f-score
        _, current_node, path = open_set.pop(0)  # Pop the node with the lowest f-score

        if current_node == goal_node:
            return path + [current_node]

        if current_node in closed_set:
            continue

        closed_set.add(current_node)

        x, y = MazeGenerator.finding_coordinates(current_node)
        neighbors = finding_neighbors(x, y)

        for neighbor_x, neighbor_y in neighbors:
            neighbor_node = neighbor_y * 6 + neighbor_x
            if neighbor_node not in closed_set:
                new_path = path + [current_node]
                g_score = len(new_path)
                # h_score = heuristic(neighbor_node, goal_node)
                # f_score = g_score + h_score
                # open_set.append((f_score, neighbor_node, new_path))

    return []

# A* Search
print("Performing AStar Search...")
visited_nodes_AStar = set()
# Performing A* Search
path_for_AStar = a_star_search(MazeGenerator.start_node, MazeGenerator.goal_node)
visited_nodes_AStar = set(path_for_AStar)
time_to_find_goal_AStar = len(visited_nodes_AStar)
# Display results
print("Visited Nodes:", visited_nodes_AStar)
print("Time to identify the objective:", time_to_find_goal_AStar, "minutes")
print("Final Path:", path_for_AStar)
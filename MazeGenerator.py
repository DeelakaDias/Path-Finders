import random


def finding_coordinates(node):
    x = node % 6  # finding the column
    y = node // 6  # finding the row
    return x, y


maze = [
    ["0", "6", "12", "18", "24", "30"],
    ["1", "7", "13", "19", "25", "31"],
    ["2", "8", "14", "20", "26", "32"],
    ["3", "9", "15", "21", "27", "33"],
    ["4", "10", "16", "22", "28", "34"],
    ["5", "11", "17", "23", "29", "35"]
]


def generate_barrier_nodes(start_node, goal_node):
    # Generate the first barrier_node1
    barrier_node1 = random.randint(0, 35)
    while barrier_node1 == start_node or barrier_node1 == goal_node:
        barrier_node1 = random.randint(0, 35)

    # Generate the second barrier_node1
    barrier_node2 = random.randint(0, 35)
    while barrier_node2 == start_node or barrier_node2 == goal_node or barrier_node2 == barrier_node1:
        barrier_node2 = random.randint(0, 35)

    # Generate the third barrier_node1
    barrier_node3 = random.randint(0, 35)
    while barrier_node3 == start_node or barrier_node3 == goal_node or barrier_node3 == barrier_node1 or barrier_node3 == barrier_node2:
        barrier_node3 = random.randint(0, 35)

    # Generate the fourth barrier_node1
    barrier_node4 = random.randint(0, 35)
    while barrier_node4 == start_node or barrier_node4 == goal_node or barrier_node4 == barrier_node1 or barrier_node4 == barrier_node2 or barrier_node4 == barrier_node3:
        barrier_node4 = random.randint(0, 35)

    return barrier_node1, barrier_node2, barrier_node3, barrier_node4


# Generate start and goal nodes
start_node = random.randint(0, 11)
goal_node = random.randint(24, 35)
# Generate 4 barrier nodes using the function
barrier_node1, barrier_node2, barrier_node3, barrier_node4 = generate_barrier_nodes(start_node, goal_node)

start_node_coordinates = finding_coordinates(start_node)
goal_node_coordinates = finding_coordinates(goal_node)
barrier_node1_coordinates = finding_coordinates(barrier_node1)
barrier_node2_coordinates = finding_coordinates(barrier_node2)
barrier_node3_coordinates = finding_coordinates(barrier_node3)
barrier_node4_coordinates = finding_coordinates(barrier_node4)

barrier_nodes_coordinates_list = [barrier_node1_coordinates, barrier_node2_coordinates, barrier_node3_coordinates, barrier_node4_coordinates]

maze[start_node_coordinates[0]][start_node_coordinates[1]] = "S"  # start node of the maze will set

maze[goal_node_coordinates[0]][goal_node_coordinates[1]] = "G"  # goal node of the maze will set

maze[barrier_node1_coordinates[0]][barrier_node1_coordinates[1]] = "B1"  # barrier node1 of the maze will set

maze[barrier_node2_coordinates[0]][barrier_node2_coordinates[1]] = "B2"  # barrier node2 of the maze will set

maze[barrier_node3_coordinates[0]][barrier_node3_coordinates[1]] = "B3"  # barrier node3 of the maze will set

maze[barrier_node4_coordinates[0]][barrier_node4_coordinates[1]] = "B4"  # barrier node4 of the maze will set


print("Maze: ")
for row in maze:
    print(row)
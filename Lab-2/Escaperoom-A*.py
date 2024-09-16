import heapq
import random
import math

# Function to create a grid based on user-defined size and place the exit at the bottom-right corner
def create_grid(size):
    grid = [['C' for _ in range(size)] for _ in range(size)]
    grid[0][0] = 'P'  # 'P' marks the starting point at the top-left corner (0,0)
    grid[size-1][size-1] = 'E'  # 'E' marks the exit at the bottom-right corner
    return grid, (size-1, size-1)

# Function to add random obstacles to the grid
def add_obstacles(grid, num_obstacles):
    size = len(grid)
    for _ in range(num_obstacles):
        obstacle_x, obstacle_y = random.randint(0, size-1), random.randint(0, size-1)
        while grid[obstacle_x][obstacle_y] in ['P', 'E']:
            obstacle_x, obstacle_y = random.randint(0, size-1), random.randint(0, size-1)
        grid[obstacle_x][obstacle_y] = 'O'  # Place the obstacle 'O'
    return grid

# Function to check if a position is valid (within bounds and not blocked by an obstacle)
def is_valid_position(grid, x, y):
    size = len(grid)
    return 0 <= x < size and 0 <= y < size and grid[x][y] != 'O'

# Heuristic function: Calculates the straight-line (Euclidean) distance between the current node and the goal
def heuristic(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Function to print the grid at the current state (used for showing the path and visited cells)
def print_grid(grid, path=None):
    grid_copy = [row.copy() for row in grid]
    
    if path:
        for cell in path:
            if grid_copy[cell[0]][cell[1]] not in ['P', 'E']:
                grid_copy[cell[0]][cell[1]] = '*'
    
    # Print the grid
    for row in grid_copy:
        print(' '.join(row))
    print()

# A* algorithm function to find the shortest path
def a_star(grid, start, goal):
    size = len(grid)
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_score = {start: 0}
    parent = {start: None}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    shortest_path = []
    
    iteration = 0

    while open_list:
        iteration += 1
        _, current = heapq.heappop(open_list)

        if current == goal:
            # Once the goal is found, backtrack to create the shortest path
            shortest_path = []
            while current is not None:
                shortest_path.append(current)
                current = parent[current]
            shortest_path.reverse()
            break

        visited.add(current)

        for direction in directions:
            next_x, next_y = current[0] + direction[0], current[1] + direction[1]
            next_state = (next_x, next_y)

            if is_valid_position(grid, next_x, next_y):
                tentative_g_score = g_score[current] + 1

                if next_state not in g_score or tentative_g_score < g_score[next_state]:
                    g_score[next_state] = tentative_g_score
                    f_score = tentative_g_score + heuristic(next_state, goal)
                    heapq.heappush(open_list, (f_score, next_state))
                    parent[next_state] = current

    return shortest_path

# Function to print only the iterations that are part of the shortest path
def print_iterations_for_shortest_path(grid, path):
    print("Iterations for the shortest path:")
    for step in path:
        print(f"Step: {step}")
        print_grid(grid, path=[step])

# Main function to demonstrate the A* algorithm
def escape_room():
    size = 6  # Fixed grid size for demonstration
    num_obstacles = 8  # Number of obstacles in the grid

    grid, goal = create_grid(size)
    grid = add_obstacles(grid, num_obstacles)

    print("Initial Grid:")
    print_grid(grid)

    print("\nSearching for the exit using A* algorithm...\n")
    shortest_path = a_star(grid, (0, 0), goal)

    if shortest_path:
        print("\nShortest Path Found:")
        print_grid(grid, path=shortest_path)
        print_iterations_for_shortest_path(grid, shortest_path)
    else:
        print("No path found to the exit.")

# Run the game
escape_room()

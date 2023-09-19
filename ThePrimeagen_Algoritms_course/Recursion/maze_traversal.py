from copy import deepcopy, copy

maze = []
visited = []
road = []

with open("maze.txt", "r") as file:
    for line in file:
        maze.append([letter for letter in line])
        visited.append([False for char in range(len(line))])

start = "S"
finish = "F"
wall = "#"
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_not_out_of_bounds(x, y):
    if 0 <= x < len(maze):
        if 0 <= y < len(maze[0]):
            return True
    return False


def traverse(x, y, maze, visited):
    if not is_not_out_of_bounds(x, y):
        print(x, y)
        print("is out of bounds\n")
        return False

    elif maze[x][y] == wall:
        print(x, y)
        print("is wall\n")
        return False

    elif visited[x][y] == True:
        print(x, y)
        print("is visited already\n")
        return False

    elif maze[x][y] == finish:
        print(x, y)
        print("Found finish line!!!!!!!!!!!!!!!!\n")
        road.append((x, y))
        return True

    print(x, y)
    print("is OK. Going further\n")
    visited[x][y] = True
    road.append((x, y))

    for direction in directions:
        dir_x, dir_y = direction
        new_x, new_y = x + dir_x, y + dir_y
        if traverse(new_x, new_y, maze, visited=visited):
            return True

    popped = road.pop()
    print(f"Just popped this {popped}")


def main(x, y):
    result = traverse(x, y, maze, visited)
    print(result)


def print_path(a_maze=[line[:] for line in maze], road=road):
    for position in road:
        x, y = position
        a_maze[x][y] = "\033[92m@\033[0m"

    for line in a_maze:
        print("".join(line).strip())


def find_start(maze=maze):
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == "S":
                return (x, y)


if __name__ == "__main__":
    x, y = find_start()
    result = main(x, y)
    print("Here's the path: ", road)
    print_path()
    # print(maze)

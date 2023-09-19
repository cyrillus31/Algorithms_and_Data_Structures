import os
from copy import copy, deepcopy


def get_maze_and_visited(file):
    maze = []
    visited = []
    with open(file, "r") as file:
        for line in file:
            maze.append([letter for letter in line])
            visited.append([False for char in range(len(line))])
    return maze, visited


start = "S"
finish = "F"
wall = "#"
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def is_not_out_of_bounds(x, y, maze):
    if 0 <= x < len(maze):
        if 0 <= y < len(maze[0]):
            return True
    return False


def traverse(x, y, maze, visited, road):
    """
    This is the recursive funcion. It shall have base cases that stop recursion (one of which is desired).
    It also has a pre-recursive case, recursive-case and post-recursive case. Recursive case presents a logical fork
    that either allowes for the post-recursive case to run or not."""

    # THE FOLLWOING ARE THE BASE CASES
    if not is_not_out_of_bounds(x, y, maze):
        # print(x, y)
        # print("is out of bounds\n")
        return False

    elif maze[x][y] == wall:
        # print(x, y)
        # print("is wall\n")
        return False

    elif visited[x][y] == True:
        # print(x, y)
        # print("is visited already\n")
        return False

    elif maze[x][y] == finish:
        # print(x, y)
        # print("Found finish line!!!!!!!!!!!!!!!!\n")
        road.append((x, y))
        return True # THIS IS THE DESIRED BASE CASE SO IT RETURNS TRUE

    # print(x, y)
    # print("is OK. Going further\n")

    # THIS IS THE PRE-RECURSIVE CASE
    visited[x][y] = True
    road.append((x, y))

    # THIS IS THE RECURSIVE CASE
    for direction in directions:
        dir_x, dir_y = direction
        new_x, new_y = x + dir_x, y + dir_y
        if traverse(new_x, new_y, maze, visited, road):
            return True  # SHALL RETURN THE SAME THING AS THE DESIRED BASE CASE TO PREVENT POST RECURSIVE CASE FROM HAPPENING

    # THIS IS THE POST RECURSIVE CASE
    popped = road.pop()

    """
    BASICALLY, POST-RECURSIVE CASE UNDOES WHATEVER IS BEING DONE BY PRE-RECURSIVE CASE. 
    THE ONLY WAY TO STOP THAT 'UNDOING' IS BY REACHING THE DESIRED BASE CASE"""


def print_path(a_maze, road):
    a_maze = [line[:] for line in maze]
    for position in road:
        x, y = position
        a_maze[x][y] = "\033[92m@\033[0m"

    for line in a_maze:
        print("".join(line).strip())


def find_start(maze):
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == "S":
                return (x, y)


if __name__ == "__main__":
    root, folders, files = next(os.walk(os.getcwd()))
    for file in files:
        if ".py" in file:
            continue
        maze, visited = get_maze_and_visited(file)
        road = []
        x, y = find_start(maze)
        traverse(x, y, maze, visited, road)
        print("\n", file)
        print("Here's the path: ", road)
        print_path(maze, road)

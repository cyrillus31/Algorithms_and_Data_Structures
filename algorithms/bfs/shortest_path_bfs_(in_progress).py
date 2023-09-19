import os
from typing import Any
from collections import deque

START = "S"
END = "E"
WALL = "#"
nodes_map = {}


def create_maze(file) -> tuple[list[Any], list[Any]]:
    maze: list[str] = []
    visited: list[bool] = []
    with open(file, "r") as f:
        for line in f:
            maze.append([])
            visited.append([])
            for letter in line:
                maze[-1].append(letter)
                visited[-1].append(False)
    return (maze, visited)


def is_out_of_bounds(x, y):
    if 0 <= x < len(maze):
        if 0 <= y < len(maze[x]):
            return False
    return True


def bfs(x, y, maze, visited, path):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque()
    q.append({"pos": (x, y), "from_node": None, "cost": 0})
    while len(q) > 0:
        node = q.popleft()
        start_x, start_y = node["pos"]
        from_node = node["from_node"]
        cost = node["cost"]

        # check if this is the end
        if is_out_of_bounds(start_x, start_y):
            continue

        elif visited[start_x][start_y]:
            continue

        elif maze[start_x][start_y] == END:
            path.append({"pos": (x, y), "from_node": from_node, "cost": cost})
            q.append({"pos": (x, y), "from_node": from_node, "cost": cost})
            nodes_map[(start_x, start_y)] = {"from_node": from_node, "cost": cost}
            return path, q, nodes_map

        elif maze[start_x][start_y] == WALL:
            continue

        visited[start_x][start_y] = True
        path.append({"pos": (start_x, start_y), "from_node": from_node, "cost": cost})
        nodes_map[(start_x, start_y)] = {"from_node": from_node, "cost": cost}

        for direction in directions:
            dir_x, dir_y = direction
            x, y = start_x + dir_x, start_y + dir_y
            q.append({"pos": (x, y), "from_node": (start_x, start_y), "cost": cost + 1})


def find_start(maze):
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == START:
                return (x, y)
    raise Exception("Can't find start point")


def print_maze(maze):
    for line in maze:
        print("".join(line).strip())


def add_path_to_maze(maze, path):
    for point in path:
        x, y = point["pos"]
        maze[x][y] = "\033[92m@\033[0m"

    print_maze(maze)

def construct_road_back(nodes_map, finish):
    x, y = finish
    path_to_start = [(x, y)]
    while nodes_map[(x, y)]["from_node"]:
        n = nodes_map[(x, y)]["from_node"]
        path_to_start.append(n)
        x, y = n
    return path_to_start




if __name__ == "__main__":
    root, folders, files = next(os.walk(os.getcwd()))
    for file in files:
        if ".py" in file:
            continue

        path = []
        maze, visited = create_maze(file)

        x, y = find_start(maze)
        path, q, nodes_map = bfs(x, y, maze, visited, path)
        
        road_home = construct_road_back(nodes_map, q.pop()["pos"])
        add_path_to_maze(maze, road_home)





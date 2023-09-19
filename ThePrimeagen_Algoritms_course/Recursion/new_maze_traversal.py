maze = []
visited = []
path: list[tuple] = []

with open("maze_2.txt", "r") as file:
    for line in file:
        maze.append([letter for letter in line.strip()])
        visited.append([False for _ in range(len(line.strip()))])



directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
wall = "#"
empty = " "
finish = "E"
start = "S"


def is_out_of_bounds(x, y):
    if (0 <= x < len(maze)) and (0 <= y < len(maze[0])):
        return False
    return True


def traverse(x, y, visited):
    print(x, y)

    if is_out_of_bounds(x, y):
        print("out of bounds")
        return False

    if visited[x][y] is True:
        print("visited")
        return False


    if maze[x][y] == wall:
        print("it's a wall")
        return False

    if maze[x][y] == finish:
        path.append((x, y))
        print("Found the end")
        return True

    visited[x][y] = True
    path.append((x, y))

    for direction in directions:
        dir_x, dir_y = direction
        new_x, new_y = x + dir_x, y + dir_y
        if traverse(new_x, new_y, visited):
            return True

    path.pop()


def main(x_start, y_start):
    #     path.append((x_start, y_start))
    #     visited[x_start][y_start] = True 
    result = traverse(x_start, y_start, visited)
    if result:
        print(path)


if __name__ == "__main__":
    main(9, 1)

    for coordinate in path:
        x, y = coordinate
        maze[x][y] = "*"

    for line in maze:
        print("".join(line))


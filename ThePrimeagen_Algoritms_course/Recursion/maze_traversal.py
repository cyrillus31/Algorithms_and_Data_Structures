input = [line.strip() for line in open("input.txt", "r")][::-1] 

def find_start_and_end(input) -> tuple:
    for x, row in enumerate(input):
        for y, symbol in enumerate(row):
            if symbol == "S":
                start = (x, y)
            if symbol == "E":
                end = (x, y)

    return start, end


def walk(
        map: list[tuple], 
        current: tuple, 
        end: tuple, 
        seen: list[list[bool]],
        wall: str = "#", 
        result: list = []
        ):
    
    result.append(current)
    x, y = current

    try:
        # 1. out of bounds
        what = map[x][y]

        # 2. it's a wall
        if map[x][y] == wall:
            return False
    
        # 3. it's the end
        elif map[x][y] == "E":
            return True
    
        # 4. it's been visited already
        elif seen[x][y] == True:
            return False

    except IndexError:
        return False


    seen[x][y] = True

    moves = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
            ]

    for a, b in moves:
        x, y = result[-1]
        x, y = x + a, y + b
        if not walk(map, (x,y), end, seen, wall, result):
            result.pop()
        else:
            return result


def print_result_map(input):
    result_map = []
    for x, row in enumerate(input):
        result_row = ""
        for y, symbol in enumerate(row):
            if (x, y) in result:
                result_row += "o"
            else:
                result_row += symbol

        result_map.append(result_row)

    print("\nThe input:")
    [print(row) for row in input[::-1]]
    print("\nThe result:")
    [print(row) for row in result_map[::-1]]
    

if __name__=="__main__":
    seen = [[False for i in range(len(input[0]))] for i in range(len(input))]

    start, end = find_start_and_end(input)

    result = (walk(input, start, end, seen, "#", []))

    print(f"Resulting path is {result}")
    print_result_map(input)

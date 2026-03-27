import heapq

class Node:
    def __init__(self, x, y, g, h, parent=None):
        self.x = x
        self.y = y
        self.g = g  
        self.h = h  
        self.f = g + h  
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def astar(grid, start, target):
    rows, cols = len(grid), len(grid[0])

    open_list = []
    visited = {}

    sx, sy = start
    tx, ty = target

    start_node = Node(sx, sy, 0, heuristic(sx, sy, tx, ty))
    heapq.heappush(open_list, start_node)

    visited[(sx, sy)] = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while open_list:
        current = heapq.heappop(open_list)

        if (current.x, current.y) == (tx, ty):
            path = []
            while current:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]

        for dx, dy in directions:
            nx, ny = current.x + dx, current.y + dy
            new_g = current.g + 1

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                if (nx, ny) not in visited or new_g < visited[(nx, ny)]:
                    visited[(nx, ny)] = new_g
                    h = heuristic(nx, ny, tx, ty)
                    neighbor = Node(nx, ny, new_g, h, current)
                    heapq.heappush(open_list, neighbor)

    return None

def read_input():
    with open("input.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

    R, C = map(int, lines[0].split())

    grid = []
    for i in range(1, R + 1):
        grid.append(list(map(int, lines[i].split())))

    sr, sc = map(int, lines[R + 1].split())
    tr, tc = map(int, lines[R + 2].split())

    return grid, (sr, sc), (tr, tc)

def format_path(path):
    return "[" + ", ".join(f"({x},{y})" for x, y in path) + "]"

if __name__ == "__main__":
    try:
        grid, start, target = read_input()
        path = astar(grid, start, target)

        if path:
            cost = len(path) - 1
            print(f"Path found with cost {cost} using A*")
            print("Shortest Path:", format_path(path))
        else:
            print("Path not found using A*")

    except Exception as e:
        print("Error:", e)

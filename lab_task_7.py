# Task 1
# A* algurithom
class Node:
    def __init__(self, position, parent=None):
        self.position = position 
        self.parent = parent       
        self.g = 0                
        self.h = 0                
        self.f = 0         

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f


def heuristic(start, node):

    return abs(start[0] - node[0]) + abs(start[1] - node[1])


def astar(start, goal, grid):
    open_list = []
    closed_set = set()
    
    start_node = Node(start)
    goal_node = Node(goal)

    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1] 
        open_list.remove(current_node)
        closed_set.add(current_node.position)
        x, y = current_node.position
        neighbors = [(x + dx, y + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]]
        for next_pos in neighbors:
            if (0 <= next_pos[0] < len(grid) and
                0 <= next_pos[1] < len(grid[0]) and
                grid[next_pos[0]][next_pos[1]] == 0 and
                next_pos not in closed_set):
                g_cost = current_node.g + 1
                h_cost = heuristic(next_pos, goal_node.position)
                next_node = Node(next_pos, current_node)
                next_node.g = g_cost
                next_node.h = h_cost
                next_node.f = g_cost + h_cost

                if any(open_node for open_node in open_list if open_node == next_node and next_node.g >= open_node.g):
                    continue

                open_list.append(next_node)

    return None 


grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
    ]

start = (0, 0)
goal = (4, 4) 
path = astar(start, goal, grid)
print("Path from start to goal:", path)

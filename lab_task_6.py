#Task 1

def recursive(graph, start, visited, level):
    print(f"Level {level}: {start}")
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            recursive(graph, neighbor, visited, level + 1)

def bfs(graph, start):
    visited = [False] * len(graph) 
    recursive(graph, start, visited, 0)

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}
bfs(graph, 0)
 
#Task 2


class Node:
    def __init__(self, value):
        self.value = value 
        self.adj = []  

def bfs(start_node):
    visited = set()  
    queue = [start_node] 
    visited.add(start_node)  

    while queue:
        current_node = queue.pop(0)  
        print(current_node.value) 

        for neighbor in current_node.adj:
            if neighbor not in visited:  
                visited.add(neighbor)  
                queue.append(neighbor)  


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node0.adj = [node1, node2]
node1.adj = [node0, node3, node4]
node2.adj = [node0, node5]
node3.adj = [node1]
node4.adj = [node1]
node5.adj = [node2]

bfs(node0)


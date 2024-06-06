import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, color_map=None, ax=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    if color_map:
        for node in tree.nodes(data=True):
            node_id = node[0]
            if node_id in color_map:
                colors[list(tree.nodes).index(node_id)] = color_map[node_id]
    
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    if ax is None:
        plt.figure(figsize=(8, 5))
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.show()
    else:
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, ax=ax)

def build_min_heap(arr):
    heapq.heapify(arr)
    return build_heap(arr)

def build_heap(arr):
    if not arr:
        return None

    nodes = [Node(val) for val in arr]
    n = len(nodes)

    for i in range(n // 2):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]

    return nodes[0]

def hex_color_gradient(start_color, end_color, steps):
    start_color = int(start_color.lstrip('#'), 16)
    end_color = int(end_color.lstrip('#'), 16)
    start_r = (start_color >> 16) & 255
    start_g = (start_color >> 8) & 255
    start_b = start_color & 255
    end_r = (end_color >> 16) & 255
    end_g = (end_color >> 8) & 255
    end_b = end_color & 255

    color_list = []
    for step in range(steps):
        r = round(start_r + (step * (end_r - start_r) / (steps - 1)))
        g = round(start_g + (step * (end_g - start_g) / (steps - 1)))
        b = round(start_b + (step * (end_b - start_b) / (steps - 1)))
        color_list.append(f'#{r:02X}{g:02X}{b:02X}')
    return color_list

def dfs(node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    if node:
        visited.add(node)
        order.append(node)
        dfs(node.left, visited, order)
        dfs(node.right, visited, order)

    return order

def bfs(root):
    visited = set()
    order = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node and node not in visited:
            visited.add(node)
            order.append(node)
            queue.append(node.left)
            queue.append(node.right)

    return order

def visualize_traversals(tree_root, dfs_order, bfs_order):
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    # Visualize DFS
    dfs_color_map = {}
    dfs_colors = hex_color_gradient("#000080", "#ADD8E6", len(dfs_order))
    for i, node in enumerate(dfs_order):
        dfs_color_map[node.id] = dfs_colors[i]
    draw_tree(tree_root, dfs_color_map, ax=axes[0])
    axes[0].set_title("DFS Order")

    # Visualize BFS
    bfs_color_map = {}
    bfs_colors = hex_color_gradient("#800000", "#FFC0CB", len(bfs_order))
    for i, node in enumerate(bfs_order):
        bfs_color_map[node.id] = bfs_colors[i]
    draw_tree(tree_root, bfs_color_map, ax=axes[1])
    axes[1].set_title("BFS Order")

    plt.show()

if __name__ == "__main__":
    heap_array = [10, 1, 3, 5, 4, 0]

    min_heap_root = build_min_heap(heap_array)

    dfs_order = dfs(min_heap_root)
    print("DFS Order:", [node.val for node in dfs_order])

    bfs_order = bfs(min_heap_root)
    print("BFS Order:", [node.val for node in bfs_order])

    visualize_traversals(min_heap_root, dfs_order, bfs_order)
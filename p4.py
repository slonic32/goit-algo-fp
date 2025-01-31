import uuid

import networkx as nx
import matplotlib.pyplot as plt

import heapq


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def heap_to_tree(heap):
	if not heap:
		return None
	nodes = []
	for value in heap:
		nodes.append(Node(value))
   
	for i in range(len(nodes)):
		left = 2 * i + 1
		right = 2 * i + 2
		if left < len(nodes):
			nodes[i].left = nodes[left]
		if right < len(nodes):
			nodes[i].right = nodes[right]
	return nodes[0]

def draw_heap(heap):
	tree_root = heap_to_tree(heap)
	if tree_root:
		draw_tree(tree_root)

# Приклад використання
heap = [1, 2, 3, 4, 5, 6, 7]
heapq.heapify(heap)
draw_heap(heap)


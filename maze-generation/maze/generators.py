import random
from maze import Maze
from networkx.utils import UnionFind

def aldous_broder(maze):
    start = random.choice(maze.graph.nodes())
    current = start
    while not all(maze.reachable(cell) for cell in maze.graph.nodes()):
        dest = random.choice(maze.neighbors(current))
        if not maze.reachable(dest):
            yield 'connect', (current, dest)
        current = dest
aldous_broder.initial_maze = Maze.all_walls

def prim(maze):
    start = random.choice(maze.graph.nodes())
    walls = maze.walls(start)
    while walls:
        wall = random.choice(walls)
        if not maze.reachable(wall[1]):
            yield 'connect', wall
            walls.extend(maze.walls(wall[1]))
        walls.remove(wall)
prim.initial_maze = Maze.all_walls

def kruskal(maze):
    walls = []
    for node in maze.graph.nodes():
        walls.extend(w for w in maze.walls(node) if w not in walls)
    cells = UnionFind()
    for c in maze.graph.nodes(): cells[c]
    random.shuffle(walls)
    for c1, c2 in walls:
        if cells[c1] != cells[c2]:
            yield 'connect', (c1, c2)
            cells.union(c1, c2)
kruskal.initial_maze = Maze.all_walls

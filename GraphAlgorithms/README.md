# Graph Algorithms

This directory contains several important graph algorithms implemented in C++. These algorithms are widely used in computer science for pathfinding, graph traversal, and analysis.

## Included Algorithms

1. **Dijkstra's Algorithm**:
   - Finds the shortest path in a weighted graph.
   - Suitable for graphs with non-negative weights.

2. **Kruskal’s Algorithm**:
   - Greedy approach to finding the Minimum Spanning Tree (MST).
   - Works well for sparse graphs.

3. **Prim's Algorithm**:
   - Another method for finding the MST, better suited for dense graphs.

4. **Bellman-Ford Algorithm**:
   - Finds the shortest path in graphs with negative weights.
   - Detects negative weight cycles.

5. **Floyd-Warshall Algorithm**:
   - Finds shortest paths between all pairs of vertices.

6. **Depth-First Search (DFS)**:
   - Explores graph depth-wise.
   
7. **Breadth-First Search (BFS)**:
   - Explores graph level-wise.

## How to Run

Each algorithm is implemented in its respective `.cpp` file. You can compile and run the programs using a C++ compiler, for example:

```bash
g++ dijkstra.cpp -o dijkstra
./dijkstra

#include <iostream>
#include <vector>
#include <climits>

using namespace std;

struct Edge {
    int src, dest, weight;
};

void bellman_ford(int vertices, int edges, const vector<Edge>& graph, int source) {
    vector<int> dist(vertices, INT_MAX);
    dist[source] = 0;

    for (int i = 1; i <= vertices - 1; i++) {
        for (const auto& edge : graph) {
            if (dist[edge.src] != INT_MAX && dist[edge.src] + edge.weight < dist[edge.dest]) {
                dist[edge.dest] = dist[edge.src] + edge.weight;
            }
        }
    }

    // Check for negative weight cycles
    for (const auto& edge : graph) {
        if (dist[edge.src] != INT_MAX && dist[edge.src] + edge.weight < dist[edge.dest]) {
            cout << "Graph contains negative weight cycle" << endl;
            return;
        }
    }

    // Print distances
    for (int i = 0; i < vertices; i++) {
        cout << "Distance from source " << source << " to " << i << " is " << dist[i] << endl;
    }
}

int main() {
    vector<Edge> graph = {
        {0, 1, -1}, {0, 2, 4}, 
        {1, 2, 3}, {1, 3, 2}, 
        {1, 4, 2}, {3, 1, 1}, 
        {3, 2, 5}, {4, 3, -3}
    };

    int vertices = 5;
    int edges = graph.size();
    bellman_ford(vertices, edges, graph, 0);
    return 0;
}

#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

typedef pair<int, int> pii;

void dijkstra(int source, const vector<vector<pii>>& graph) {
    int n = graph.size();
    vector<int> dist(n, INT_MAX);
    priority_queue<pii, vector<pii>, greater<pii>> pq;

    dist[source] = 0;
    pq.push({0, source});

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        for (const auto& edge : graph[u]) {
            int v = edge.first;
            int weight = edge.second;

            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    // Print the distance from source to each vertex
    for (int i = 0; i < n; i++) {
        cout << "Distance from source " << source << " to " << i << " is " << dist[i] << endl;
    }
}

int main() {
    // Example graph as an adjacency list
    vector<vector<pii>> graph = {
        {{1, 4}, {2, 1}},  // Edges from vertex 0
        {{0, 4}, {2, 2}, {3, 1}}, // Edges from vertex 1
        {{0, 1}, {1, 2}, {3, 5}}, // Edges from vertex 2
        {{1, 1}, {2, 5}} // Edges from vertex 3
    };

    dijkstra(0, graph); // Run Dijkstra's algorithm from vertex 0
    return 0;
}

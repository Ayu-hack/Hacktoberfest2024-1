#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

void dijkstra(vector<vector<pair<int, int>>> &graph, int source) {
    vector<int> dist(graph.size(), INT_MAX);
    dist[source] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, source});

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        for (auto &neighbor : graph[u]) {
            int v = neighbor.first, weight = neighbor.second;
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    for (int i = 0; i < dist.size(); i++)
        cout << "Distance from " << source << " to " << i << " is " << dist[i] << endl;
}

int main() {
    int V = 5;
    vector<vector<pair<int, int>>> graph(V);
    graph[0].push_back({1, 10});
    graph[0].push_back({4, 5});
    graph[1].push_back({2, 1});
    graph[1].push_back({4, 2});
    graph[2].push_back({3, 4});
    graph[3].push_back({0, 7});
    graph[4].push_back({1, 3});
    graph[4].push_back({2, 9});
    graph[4].push_back({3, 2});

    dijkstra(graph, 0);

    return 0;
}

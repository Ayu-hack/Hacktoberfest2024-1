#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

typedef pair<int, int> pii;

void prims(int start, const vector<vector<pii>>& graph) {
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    vector<bool> inMST(graph.size(), false);
    int totalWeight = 0;

    pq.push({0, start});

    while (!pq.empty()) {
        // Use a temporary variable to store the top element
        pii current = pq.top();
        pq.pop();
        
        int weight = current.first; // Get the weight from the pair
        int u = current.second;      // Get the vertex from the pair

        if (inMST[u]) continue;

        inMST[u] = true;
        totalWeight += weight;

        for (const auto& edge : graph[u]) {
            int v = edge.first;
            int w = edge.second;

            if (!inMST[v]) {
                pq.push({w, v});
            }
        }
    }

    cout << "Total weight of Minimum Spanning Tree: " << totalWeight << endl;
}

int main() {
    vector<vector<pii>> graph = {
        {{1, 2}, {2, 3}},
        {{0, 2}, {2, 1}, {3, 4}},
        {{0, 3}, {1, 1}, {3, 2}},
        {{1, 4}, {2, 2}}
    };

    prims(0, graph);
    return 0;
}

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void bfs(int start, const vector<vector<int>>& graph) {
    vector<bool> visited(graph.size(), false);
    queue<int> q;

    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int vertex = q.front();
        q.pop();
        cout << vertex << " ";

        for (int neighbor : graph[vertex]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}

int main() {
    vector<vector<int>> graph = {
        {1, 2}, // Edges from vertex 0
        {0, 3, 4}, // Edges from vertex 1
        {0, 5}, // Edges from vertex 2
        {1}, // Edges from vertex 3
        {1, 5}, // Edges from vertex 4
        {2, 4} // Edges from vertex 5
    };

    cout << "BFS traversal starting from vertex 0: ";
    bfs(0, graph);
    return 0;
}

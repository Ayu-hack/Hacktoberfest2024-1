#include <iostream>
#include <vector>

using namespace std;

void dfs(int vertex, vector<bool>& visited, const vector<vector<int>>& graph) {
    visited[vertex] = true;
    cout << vertex << " ";

    for (int neighbor : graph[vertex]) {
        if (!visited[neighbor]) {
            dfs(neighbor, visited, graph);
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

    vector<bool> visited(graph.size(), false);
    cout << "DFS traversal starting from vertex 0: ";
    dfs(0, visited, graph);
    return 0;
}


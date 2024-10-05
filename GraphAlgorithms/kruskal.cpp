#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int src, dest, weight;
};

bool compare(Edge a, Edge b) {
    return a.weight < b.weight;
}

int findParent(int v, vector<int>& parent) {
    if (parent[v] == -1) return v;
    return findParent(parent[v], parent);
}

void unionNodes(int u, int v, vector<int>& parent) {
    parent[u] = v;
}

void kruskal(int vertices, const vector<Edge>& edges) {
    vector<int> parent(vertices, -1);
    vector<Edge> mst;

    for (const auto& edge : edges) {
        int u = findParent(edge.src, parent);
        int v = findParent(edge.dest, parent);

        if (u != v) {
            mst.push_back(edge);
            unionNodes(u, v, parent);
        }
    }

    cout << "Edges in Minimum Spanning Tree:" << endl;
    for (const auto& edge : mst) {
        cout << edge.src << " -- " << edge.dest << " == " << edge.weight << endl;
    }
}

int main() {
    vector<Edge> edges = {
        {0, 1, 10},
        {0, 2, 6},
        {0, 3, 5},
        {1, 3, 15},
        {2, 3, 4}
    };

    int vertices = 4;
    sort(edges.begin(), edges.end(), compare);
    kruskal(vertices, edges);
    return 0;
}

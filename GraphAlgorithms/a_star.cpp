#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <unordered_map>

using namespace std;

typedef pair<int, int> pii;

struct Node {
    int vertex;
    int cost;
    int heuristic;
    int total;

    bool operator>(const Node& other) const {
        return total > other.total;
    }
};

int heuristic(int a, int b) {
    return abs(a - b); // Example heuristic
}

void a_star(int source, int goal, const vector<vector<pii>>& graph) {
    priority_queue<Node, vector<Node>, greater<Node>> pq;
    unordered_map<int, int> cost;
    pq.push({source, 0, heuristic(source, goal), 0});
    cost[source] = 0;

    while (!pq.empty()) {
        Node current = pq.top();
        pq.pop();

        if (current.vertex == goal) {
            cout << "Path found with cost: " << current.cost << endl;
            return;
        }

        for (const auto& edge : graph[current.vertex]) {
            int next_vertex = edge.first;
            int weight = edge.second;

            int new_cost = current.cost + weight;
            if (cost.find(next_vertex) == cost.end() || new_cost < cost[next_vertex]) {
                cost[next_vertex] = new_cost;
                pq.push({next_vertex, new_cost, heuristic(next_vertex, goal), new_cost + heuristic(next_vertex, goal)});
            }
        }
    }
    cout << "Path not found" << endl;
}

int main() {
    vector<vector<pii>> graph = {
        {{1, 1}, {2, 4}},
        {{0, 1}, {2, 2}, {3, 5}},
        {{0, 4}, {1, 2}, {3, 1}},
        {{1, 5}, {2, 1}}
    };

    a_star(0, 3, graph);
    return 0;
}

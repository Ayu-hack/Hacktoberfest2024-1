// Java program to find maximum number of edge disjoint paths
import java.util.*;

class Solution
{
    // Number of vertices in given graph
    static int V = 8;

    // Returns true if there is a path from source 's' to sink 't' in residual graph.
    static boolean bfs(int rGraph[][], int s, int t, int parent[])
    {
        // Create a visited array and mark all vertices as not visited
        boolean []visited = new boolean[V];

        // Create a queue, enqueue source vertex and mark source vertex as visited
        Queue <Integer> q = new LinkedList<>();
        q.add(s);
        visited[s] = true;
        parent[s] = -1;

        // Standard BFS Loop
        while (!q.isEmpty())
        {
            int u = q.peek();
            q.remove();

            for (int v = 0; v < V; v++)
            {
                if (visited[v] == false && rGraph[u][v] > 0)
                {
                    q.add(v);
                    parent[v] = u;
                    visited[v] = true;
                }
            }
        }

        // If we reached sink in BFS starting from source, return true, else false
        return (visited[t] == true);
    }

    // Returns the maximum number of edge-disjoint paths from s to t
    static int findDisjointPaths(int graph[][], int s, int t)
    {
        // Create a residual graph and fill it with capacities
        int [][]rGraph = new int[V][V];
        for (int u = 0; u < V; u++)
            for (int v = 0; v < V; v++)
                rGraph[u][v] = graph[u][v];

        int []parent = new int[V]; 
        int max_flow = 0; // No flow initially

        // Augment the flow while there is path from source to sink
        while (bfs(rGraph, s, t, parent))
        {
            // Find minimum residual capacity along the path filled by BFS
            int path_flow = Integer.MAX_VALUE;
            for (int v = t; v != s; v = parent[v])
            {
                int u = parent[v];
                path_flow = Math.min(path_flow, rGraph[u][v]);
            }

            // Update residual capacities along the path
            for (int v = t; v != s; v = parent[v])
            {
                int u = parent[v];
                rGraph[u][v] -= path_flow;
                rGraph[v][u] += path_flow;
            }

            // Add path flow to overall flow
            max_flow += path_flow;
        }

        // Return the overall flow (max_flow is equal to maximum number of edge-disjoint paths)
        return max_flow;
    }

    // Driver Code
    public static void main(String[] args)
    {
        // Let us create a graph shown in the above example
        int graph[][] = {{0, 1, 1, 1, 0, 0, 0, 0},
                         {0, 0, 1, 0, 0, 0, 0, 0},
                         {0, 0, 0, 1, 0, 0, 1, 0},
                         {0, 0, 0, 0, 0, 0, 1, 0},
                         {0, 0, 1, 0, 0, 0, 0, 1},
                         {0, 1, 0, 0, 0, 0, 0, 1},
                         {0, 0, 0, 0, 0, 1, 0, 1},
                         {0, 0, 0, 0, 0, 0, 0, 0}};

        int s = 0;
        int t = 7;
        System.out.println("There can be maximum " + 
                           findDisjointPaths(graph, s, t) + 
                           " edge-disjoint paths from " + s + " to " + t);
    }
}

#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <limits>
#include <algorithm>
using namespace std;

pair<vector<long long>, vector<int>> dijkstra(int n, const vector<vector<pair<int,int>>>& adj, int s) {
    const long long INF = numeric_limits<long long>::max()/4;
    vector<long long> dist(n, INF);
    vector<int> parent(n, -1);
    using P = pair<long long,int>;
    priority_queue<P, vector<P>, greater<P>> pq;
    dist[s] = 0;
    pq.push({0, s});
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        for (auto [v, w] : adj[u]) {
            long long nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                parent[v] = u;
                pq.push({nd, v});
            }
        }
    }
    return {dist, parent};
}

vector<int> reconstruct(const vector<int>& parent, int t) {
    vector<int> path;
    while (t != -1) { path.push_back(t); t = parent[t]; }
    reverse(path.begin(), path.end());
    return path;
}

int main() {
    int n = 5;
    vector<vector<pair<int,int>>> adj(n);
    auto add = [&](int u, int v, int w){ adj[u].push_back({v,w}); adj[v].push_back({u,w}); };
    add(0,1,4); add(0,2,1); add(2,1,2); add(1,3,1); add(2,3,5); add(3,4,3);
    auto res = dijkstra(n, adj, 0);
    cout << res.first[4] << "\n";
    auto path = reconstruct(res.second, 4);
    for (int x : path) cout << x << " ";
    cout << "\n";
    return 0;
}

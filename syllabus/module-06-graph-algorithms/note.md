Title
Graph Algorithms

Concept summary
We model systems as vertices connected by edges and apply search and optimization over this structure. Core tools include traversal with queues and stacks shortest paths minimum spanning trees and detection of connectivity and cycles.

Key results to be comfortable with
Breadth first search explores in layers and yields shortest path lengths in unweighted graphs
Depth first search reveals discovery and finish times and supports cycle detection and topological ordering
Dijkstra with a priority queue solves single source shortest paths with nonnegative weights
Union find with path compression and union by rank supports fast connectivity queries and powers Kruskal for minimum spanning trees
Strongly connected components in directed graphs can be found by two depth first passes using finishing order

Worked example
Problem
Given a directed weighted graph with nonnegative weights find the shortest distance from a source to every vertex.

Idea
Maintain a distance array and a priority queue keyed by current best distance. Repeatedly extract the vertex with smallest tentative distance then relax its outgoing edges. If a relaxation improves a neighbor push the new pair into the queue.

Solution outline
Initialize all distances to infinity except the source which is zero
Push the pair source and zero into the priority queue
While the queue is not empty pop the pair with smallest distance
If that distance is greater than the stored one skip it
For each outgoing edge try to improve the neighbor by relaxing
Store parent pointers to recover paths

Full solution with analysis
Each edge may trigger at most one improvement that matters with a push into the queue. Using a binary heap the total time is O of m log n where m is edges and n is vertices. Correctness follows from the greedy property that once a vertex is removed from the queue with its smallest distance known no future path can beat it when weights are nonnegative.

Flowchart step list
Start
Read number of vertices and edges and the source
Set all dist to infinity and parent to minus one
Set dist of source to zero
Push pair of zero and source into the priority queue
While queue not empty
Pop current distance and vertex u
If current distance is greater than dist u continue
For each neighbor v with edge weight w
If dist u plus w is less than dist v then update dist v and set parent v to u and push new pair
End loops
Return dist and parent arrays
End

Coding lab
Goals
Implement Dijkstra with a priority queue and path recovery
Compare with breadth first search on unweighted graphs by setting all weights to one

Tasks
Write a function for Dijkstra that returns both distances and parents
Write a function that reconstructs a path to a target
Generate random sparse graphs and measure run time growth
Verify that when all weights are one the distances match breadth first search layers

Practice set
One prove that Dijkstra fails when negative edges are present by constructing a small counterexample
Two compute a minimum spanning tree by Kruskal with union find then compare its total weight with Prim on the same graph
Three find strongly connected components with a two pass method and show the condensation graph is acyclic
Four detect a cycle in an undirected graph with union find then repeat with depth first search and back edge logic
Five compute topological ordering in a directed acyclic graph and use it to solve single source shortest paths in linear time for that class

Reflection
Which invariant guarantees that the distance of the extracted vertex is final
How do priority queue implementations affect constant factors in practice

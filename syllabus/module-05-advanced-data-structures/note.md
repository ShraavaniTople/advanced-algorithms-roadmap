Title
Advanced Data Structures

Concept summary
We use specialized structures to support fast updates and queries on dynamic data. Key ideas are partial sums with logarithmic time operations balancing through tree shapes path compression for connectivity and potential based arguments for amortized bounds.

Key results to be comfortable with
Heaps for priority operations in logarithmic time
Disjoint set union with path compression and union by rank with near constant amortized time
Fenwick tree for prefix sums and point updates in logarithmic time
Segment tree for range queries and updates with flexible merge logic
Hashing with load factor control and expected constant time

Worked example
Problem
Maintain an array A of length n under two operations point update at index i by adding delta and query prefix sum up to index i.

Idea
Use a Fenwick tree also called a binary indexed tree that stores partial sums at indices determined by the least significant one bit. Updates walk upward by adding that bit and queries walk downward by subtracting that bit.

Solution outline
Represent tree as an array bit of length n plus one using one based indexing
To update add delta to bit at position i then set i to i plus i and its least significant one bit until i exceeds n
To query prefix sum set s to zero then while i is positive add bit i to s and set i to i minus i and its least significant one bit
Range sum for l r is prefix r minus prefix l minus one

Full solution with analysis
Each update and prefix query changes or reads at most log n positions because the least significant one bit jump halves the remaining distance to zero on average. Time per operation is theta of log n and space is theta of n.

Flowchart step list
Start
Initialize bit with zeros
For update at index i with delta
While i at most n add delta to bit i and set i to i plus i and its least significant one bit
For prefix query at index i set sum to zero
While i greater than zero add bit i to sum and set i to i minus i and its least significant one bit
Return sum
End

Coding lab
Goals
Implement Fenwick tree in Python and C plus plus
Verify that range sums match a naive prefix array on random tests

Practice set
One implement disjoint set union and show the effect of path compression on a sequence of union and find operations
Two implement a segment tree for range minimum query with point updates
Three design a heap based scheduler that always runs the job with the earliest deadline
Four implement an open addressing hash table and study performance as load factor grows
Five compare Fenwick and segment tree for range sum with point updates and discuss when each is simpler

Reflection
Which implementation detail of Fenwick indexing felt most subtle
How do I decide between Fenwick and segment tree for a given problem

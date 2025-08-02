Title
Dynamic Programming

Concept summary
Dynamic programming solves problems by breaking them into overlapping subproblems storing partial results and building the final answer from these stored values. The key moves are to define a clear state write a correct recurrence choose an evaluation order and prove optimal substructure and correctness.

Key results to be comfortable with
State design and dimension choices
Recurrence writing and boundary handling
Bottom up tables versus top down memoization
Space reduction by rolling arrays
Recovery of the actual solution path from parent pointers

Worked example
Problem
Zero one knapsack. Given capacity C and n items with weight w i and value v i choose a subset with maximum total value without exceeding capacity.

Idea
Define dp i c as the best value using the first i items with capacity c. Either skip item i or take it if it fits. Transition is max of skipping or taking.

Solution outline
State dp i c for i from zero to n and c from zero to C
Base cases dp zero c equals zero and dp i zero equals zero
Transition dp i c equals max of dp i minus one c and v i plus dp i minus one c minus w i when w i is at most c
Answer is dp n C

Full solution with analysis
The table has n plus one by C plus one entries. Each entry uses O one work. Total time is O of n times C and space is O of n times C or O of C with a rolling array. Proof of correctness uses induction on i and c and the optimal substructure from the last decision of taking or skipping item i.

Flowchart step list
Start
Read n C arrays w and v
Create table dp of size n plus one by C plus one filled with zeros
For i from one to n
For c from zero to C
If w i is at most c then set take to v i plus dp i minus one c minus w i else set take to minus infinity
Set skip to dp i minus one c
Set dp i c to the larger of take and skip
End loops
Return dp n C
End

Coding lab
Goals
Implement bottom up and top down versions and compare performance
Recover the chosen set of items

Tasks
Write a bottom up table solver
Write a memoized recursive solver
Add a reconstruction function that returns the indices of chosen items
Plot run time for growing C with fixed n

Practice set
One coin change minimum coins for a target using unlimited coin counts
Two longest increasing subsequence with an O of n log n method after first building the O of n squared table to understand the leap
Three edit distance between two strings with reconstruction of an alignment
Four grid paths with obstacles and space reduction
Five schedule weighted intervals by sorting and using predecessor links

Reflection
Where did I hesitate in writing the recurrence
Could I choose a smaller state that still captures the needed information

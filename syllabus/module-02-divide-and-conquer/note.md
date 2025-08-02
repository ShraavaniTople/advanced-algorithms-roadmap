Title
Divide and Conquer

Concept summary
Divide and conquer solves a problem by splitting it into smaller parts solving each part recursively and combining the partial results. Analysis often follows a recurrence solved by substitution recursion trees or the master theorem.

Key results to be comfortable with
Recurrence analysis by substitution
Recursion tree cost summation
Master theorem cases and their boundaries
Design of combine steps such as merging and partitioning
Turning a naive quadratic method into a near linear method by careful combining

Worked example
Problem
Count the number of inversions in an array. An inversion is a pair i j with i less than j and A i greater than A j.

Idea
Use a merge sort style recursion. During the merge of the left and right halves count how many right elements move before the remaining left elements.

Solution outline
Split the array into left half and right half
Recursively count inversions in each half
During merge when you take an element from the right half before the left pointer all remaining elements in the left half form inversions with that right element
Sum the three counts

Full solution with analysis
Let T n be the work to count inversions on size n. The merge does linear work so T n equals two times T n over two plus a linear term. By the master theorem T n is theta of n log n.

Flowchart step list
Start
Input array A and its length n
If n equals one then return zero
Split A into L and R
Call count on L to get cL
Call count on R to get cR
Merge L and R into A while counting cross inversions cC
Return cL plus cR plus cC
End

Coding lab
Goals
Implement the inversion counter in Python and in C plus plus
Write a test driver that generates random arrays and checks against a simple quadratic checker for small n

Tasks
Implement inversion_count in Python
Implement the same in C plus plus using vectors
Write a checker that counts by brute force for small inputs
Measure run time growth for several sizes and record the counts

Practice set
One design a divide and conquer method to find the closest pair of points in the plane with time theta of n log n
Two explain why the combine step is the key to the speedup in many problems
Three derive the master theorem for equal split from a recursion tree
Four write a divide and conquer method that counts the number of pairs i j with A i plus A j equal to a target value using sorted halves
Five argue when substitution is safer than the master theorem

Reflection
What recurrences still feel tricky
When should I prefer direct telescoping sums over the master theorem

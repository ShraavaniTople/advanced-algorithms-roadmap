Title
Greedy Methods

Concept summary
Greedy algorithms build a solution by repeatedly making the locally best choice according to a scoring rule with the hope that this leads to a global optimum. They often work when the problem has the greedy choice property and optimal substructure.

Key results to be comfortable with
Understanding the greedy choice property and optimal substructure
Proving correctness using exchange arguments
Recognizing when greedy fails and dynamic programming is needed
Designing the selection rule for each problem
Implementing greedy efficiently with appropriate data structures

Worked example
Problem
Activity selection. Given start and finish times for n activities find the maximum number of activities that can be scheduled in a single room without overlaps.

Idea
Sort activities by finish time and always choose the next one that starts after or when the last chosen one finishes.

Solution outline
Sort by finish time
Initialize an empty list of chosen activities
Keep a variable tracking the finish time of the last chosen activity
Iterate over the sorted list and choose an activity if its start time is at least the finish time of the last chosen activity
Return the list

Full solution with analysis
Sorting takes O of n log n and the selection loop takes O of n. Total time O of n log n. Correctness can be shown by exchange argument: any optimal solution can be transformed into the greedy solution without decreasing the number of activities.

Flowchart step list
Start
Read list of activities with start and finish times
Sort activities by finish time
Set last finish to minus infinity
For each activity in sorted order
If start time is at least last finish then select activity and update last finish
End loop
Return selected activities
End

Coding lab
Goals
Implement the activity selection algorithm in Python and C plus plus
Verify output on a small sample and on random inputs

Practice set
One prove correctness of the greedy choice for activity selection
Two show a case where sorting by start time instead of finish time fails
Three solve fractional knapsack by sorting by value density
Four design a greedy for minimum number of coins in a coin system that is canonical
Five give a counterexample where greedy coin change fails for a non canonical system

Reflection
When is it easy to guess the correct greedy rule
When should I suspect greedy might fail and test with counterexamples

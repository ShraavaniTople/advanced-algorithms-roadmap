Title
Analysis Foundations

Concept summary
We study how running time and memory scale with input size. We compare growth by asymptotic notation prove bounds with clear logic and use invariants to reason about correctness. The goal is to make cost arguments that hold for large inputs not just small trials.

Key results to be comfortable with
Meaning of big O big Omega and big Theta
How to prove an upper bound with a direct inequality
How to prove a lower bound by embedding a simpler hard instance
Using loop invariants to prove correctness
Amortized analysis through potential and accounting viewpoints

Worked example
Problem
Show that one plus two plus three and so on up to n is in Theta of n squared.

Solution outline
Compute the exact sum n times n plus one over two then sandwich it between n squared over two and n squared to get both an upper and a lower bound.

Full solution with analysis
Let S n be the sum of the first n integers. S n equals n times n plus one over two. For n at least one we have n squared over two is at most S n and S n is at most n squared. Hence S n is in Theta of n squared.

Flowchart step list for comparing growth of two functions f and g
Start
Write f and g explicitly
Find simple upper bounds on f and simple lower bounds on g
Take the ratio f over g and simplify
If the ratio goes to zero then f is little o of g
If the ratio goes to infinity then f dominates g
If the ratio tends to a nonzero constant then f is Theta of g
End

Coding lab idea
Empirically compare growth of n log n and n to the power one point five using random inputs and simple loops. Plot counts to see divergence. The proof lives in algebra but the plot builds intuition.

Practice set
One prove that n log n is little o of n to the power one plus epsilon for any fixed positive epsilon
Two prove that any polynomial is little o of two to the power n
Three show that binary search runs in Theta of log n by counting the number of times the search range halves
Four use a loop invariant to prove correctness of insertion sort
Five design a potential function that gives an amortized constant cost for push and pop on a dynamic array that doubles when full

Reflection
Which direction of a bound do I find harder to prove and why
What is my default plan when a direct inequality is messy

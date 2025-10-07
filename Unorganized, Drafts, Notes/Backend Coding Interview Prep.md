# Backend Coding Interview Prep

## Preparation

### Picking The Right Programming Language For You

It’s important to choose a good programming language as early as possible in preparation, so you do all of your practice problems with the given language. 

If you’re a backend engineer but Python is not your strongest programming language (say you’re more experienced with Java, Rust, Scala, Go, etc.), my recommendation depends on if your interview is over a a Whiteboard (in-person) or over VC with an online IDE (e.g. Coderpad or HackerRank).

### Skills To Practice

#### Problem Understanding

This is your skill of understanding the problem that is being asked of you and aligning with the interviewer over expectations.

- How well do you ask questions to make sure you really grok the interview question and all the edge cases and nuances?
- How well do you pick test cases to really test your problem understanding?
- How well do you align with the interviewer on expectations (run-time, code complexity, what the solution looks like).

#### Problem Solving And Communication

Now that you understand the problem, how effective are you in coming up with a solution both in abstract as well as on paper and communicating it to the interviewer?

- How well do you come up with a solution that works given the interviewer constraints/expectations?
- How well do you communicate that solution to the interviewer as you’re implementing it, so they get signal on your problem-solving?

#### Implementation

You now need to get code down into the whiteboard or IDE that matches your proposed solution.

- How quickly and effortlessly are you able to get code down?
- Do you display a mastery of the language you’ve chosen? Are you able to implement things the idiomatic way for the given language?

#### Testing and Debugging

You need to then test and debug your code. This is a very different process if it’s on the whiteboard vs. over an online IDE.

- How well do you come up with test cases that convince your interviewer your code is completely solid?
- If there is a bug, how effectively do you find where the bug is?

#### Reflecting On The Solution

Sometimes you’ll be asked to come up with O(n) for time and space and also reflect on how you’d make changes to your solution (e.g. I could make it faster if I used caching/memoization, etc.). Not every interview question will have this component, but that’s also a skill to develop.

### Practice Interviews

- When practicing, don’t just focus on the outcome (did I write correct code or not) but also make sure that you exhibited all of the behaviors (e.g. aligning with the interviewer, setting up the right test cases, debugging thoughtfully).
- Practice the art of interviewer alignment. When watching back your coding interviews, check to see if you double-checked a few test cases with your interviewer to really understand the problem.
- Try to isolate which skills you need the most work on and have your practice partner test those skills in particular. For ex: if you are very good at (2) problem-solving/communication but are not as good at (3) testing/debugging, doing a bunch of practice problems where you don’t debug anything won’t be as useful in helping you improve.

## Problems You'll See

### Custom Data Structures

The interviewer will ask you to come up with some type of custom data structure to solve a problem. Make sure you review your standard LinkedLists, HashMaps, Binary Trees and how to combine and mix them together to solve various problems.

### Binary Search

You may have to incorporate some form of binary search into your problem solving.

### String Manipulation

Get comfortable tokenizing and manipulating strings in ways to solve specific problems.

### Graph Traversal

Get experience identifying problems as graph problems and mapping the problem as some type of traversal on the graph or doing cycle detection, etc.

### Momoization

Memoization often fits as a “part 2” to an existing interview question. For example, you’ll be asked to solve some problem, and then apply memoization in order to make it more performant / tractable.

### Stacks And Recursion

## What Not To Prepare For

### Leetcode Hard Problems

These generally don’t show up because they usually don’t provide much signal to the interviewer about your ability. Leetcode Hard problems tend to focus on pattern-matching some difficult algorithm to some problem type.

### Dynamic Programming

Generally, dynamic programming probably won’t be in your interview (or if it is, it would be the bonus solution for some question that you can solve some other way).

### Niche Algorithms

There’s a class of optimal algorithms that you study in Computer Science class that are probably not as useful to study.

- For example, it’s unlikely that an interviewer will have you do a graph traversal that would require Dijkstra’s algorithm, when simple BFS/DFS/recursion would not suffice.
- As another example, it’s unlikely the interviewer would ask you a problem where you’d have to do Linear Time Selection in O(n) when a much easier O(n log n) would not be acceptable.
- If you ever run into one of these, and your interviewer is asking if you can do better than O(n log n ), you can always tell the interviewer, “I know there’s an O(n) solution based on Quicksort Linear Time Selection but I don’t remember the specific algorithm”.

## During The Interview

### Getting Time Checks From The Interviewer

### Aligning With The Interviewer

Before you even write a single line of code, you should try to align with the interviewer if your solution is reasonable. Make sure you align on which edge cases/error conditions you’ll worry about. Some examples:

- “I’m writing a brute force solution, is that okay with you?”
- “I can implement this with memoization or without, which do you prefer?”
- “Can I assume that the inputs won’t include negative numbers?”
- “What happens if an entity points to itself in a cycle? Should I worry about this case?”

### Breaking Down The Problem Into Smaller Ones

### Hint-Asking vs. Clarification

It’s okay to ask for hints, but the best interviewees are able to frame their “hints” as “clarification questions.” When you do this effectively, the interviewer doesn’t register you ask as “hint” but rather blames themselves for not providing a more clear question (or even gives you bonus points for checking edge cases!) There are several techniques/examples for how to do this:

- If you’re stuck or confused, try writing out some more test cases / examples and validating expectations.
- Stall for more time by validating trivial constraints with the interviewer (e.g. if the input is 0 or null).
You can often fish for a hint by simply acting confident and asking a clarifying question. For example: “I know there’s a brute force solution, but I’m pretty sure there might be a more performant one — do you want me to search for that one, or just go with the brute force one?”

## Links

[Backend Coding Interview Prep](https://tonygwu.medium.com/coding-interview-preparation-07ee75fd3753)
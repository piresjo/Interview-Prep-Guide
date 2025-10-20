# Technical Interviews: the 8 Most Common Mistakes Programmers Make

## #1: Jumping To Code Before Sketching Out The Solution

Start by explaining your thought process, and thinking out loud about how to break the problem down into simpler pieces. When you are ready to begin, write pseudocode to clarify your approach. Along the way use examples to spell out key steps in your algorithm.

You should also mention the brute force/naive solution early on before you’re writing anything. There are several reasons for this. First, it helps you avoid any awkward silence moments while you’re still trying to figure out the optimal solution. Second, a brute force solution can sometimes lead to an optimal one by optimizing parts of it. Lastly, as an engineer, your prime directive is to code a solution that works. Correctness takes precedence over efficiency.

## #2: Weak Computer Science Fundamentals

Carve out some time and brush up on/learn data structures & algorithms. Not only will this help you ace your coding interviews, but it’ll also make you a better software engineer. Good grasp of basic DS&A should be part of any software engineer’s toolkit.

## #3: Being Quiet

It’s a common cognitive bias to exaggerate the extent to which our thoughts are apparent to others, so err on the side of over-communicating. While performing a task, walk your interviewer through your steps and reasoning. Talking and coding at the same time doesn’t come naturally to many of us.

## #4: Poor Command Of Programming Language

If you have the option, always interview in your strongest programming language. Interviewers are often flexible and would allow you to choose the programming language you want to interview in.

If this isn’t the case — for instance, if you’re interviewing for a Frontend position where JavaScript is required — do yourself a favor and brush up on your programming language skills beforehand.

## #5: Not Using Tests

There are three times during the interview where I’d recommend to use tests. The first time is right after your interviewer finished asking you the coding question. Use an example or two to verify you understood the question (see #6 below for more details). The second time is after you sketched out your solution. Use a non-trivial test case to walk your interviewer through your pseudocode and to validate its correctness. Finally, once you’re done implementing your code, dry-test your code again to make sure you don’t have any bugs.

## #6: Misunderstanding The Question

The first thing you must do after your interviewer finished explaining the question is to repeat it back to them in your own words to validate that you understood it correctly. If you got it wrong, they’ll tell you. Doing this simple thing will spare you from the costly error of answering a completely different question. An error that we sometimes realize we’ve made only midstream when there’s no time left to change course.

While repeating the question, bring up few simple examples of input, and make sure you are correct about the expected output. It’ll make it easier for your interviewer to know whether you understood the question. The other thing you want to do is ask whether you can make certain assumptions. For instance, you can ask whether you can assume the input is valid or within a specific range. Or, depending on the question, ask whether the input is sorted. Lastly, it’s also a good practice to clarify with your interviewer whether they want you to optimize for time or space.

## #7: Ignoring Edge Cases

Use tests around the boundaries of your algorithm’s input. If your algorithm fails on some of these edge cases, check first if you can fix your algorithm by introducing some quick incremental changes to it. If you can’t, ask your interviewer whether you should handle these edge cases. If the answer is yes and you can’t seem to think of anything, engage your interviewer and try to solicit their help to guide you in the right direction.

## #8: Sloppy Code

Here are the things you should avoid:

- Giving random/non-descriptive names to variables, functions, etc. Some examples: using single character names for non-index variables. Or calling your function ‘func’. Competitive program.ing developers especially need to be careful here since they’re used to using super short names in their programs in order to code faster. This won’t work in tech interviews.
- Inconsistent coding style. While everyone has their own style of programming and we should accept it for what it is, mixing randomly coding standards is never a good idea. It signals sloppiness. For instance, employing different naming conventions. Or using tabs in some parts of your code and then in others spaces. You could be either on camp Richard or camp Winnie, but not on both. Similarly, if you put braces on the same line, don’t later put them in a new line. Other examples abound, but I think you get the point.
- Using defensive coding, such as NULL checks and lots of special cases, without really stopping to think about whether they were necessary. This leads to more complicated code that is hard to understand and debug.

## Links

[Technical Interviews: the 8 Most Common Mistakes Programmers Make](https://blog.pramp.com/top-8-mistakes-in-technical-interviews-according-to-data-27d2572bda1f)

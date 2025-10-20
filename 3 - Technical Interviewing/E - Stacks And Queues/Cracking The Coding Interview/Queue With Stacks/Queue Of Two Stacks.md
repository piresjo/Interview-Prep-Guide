# Queue Using Two Stacks

## Problem

Create a queue using two stacks.

## Things To Note

Recall the properties of stacks and queues. The big distinction between the two is that elements of the stack go in and out in a Last In First Out (LIFO) fashion (think of a Pez dispenser; the candy you put in last is the first one to exit the dispenser) and queue elements interact in a First In, First Out (FIFO) fashion (think of a line to a theater; the first one in line is the first one out of the line).

We need to use two of a structure that follows LIFO to create a data structure that follows FIFO.

## Solution Explained

There are two ways we can implement this. One way makes the enqueue process expensive so that the dequeue is in constant time. The other way makes the dequeue process expensive so that the enqueue is in constant time.

This will cover the former.

For the implementation, the first stack will be the actual queue and the second queue will be used to ensure a FIFO pattern. To enqueue, we add the elements in the first stack to the second stack. Then we add the element we're adding to the queue to the first stack. Then we put the elements in the second stack back to the first stack. That will ensure the element you first enqueued is at the top of the stack and the element you just enqueued will be at the bottom of the stack.

For the dequeue, we can just pop the top element from the stack.

## Full Solution

```python
class Queue:
    def __init__(self):
        self.stackA = []
        self.stackB = []

        def enqueue(self, x):
            while self.stackA:
                self.stackB.append(self.stackA.pop())

            self.stackA.append(x)

            while self.stackB:
                self.stackA.append(self.stackB.pop())

        def dequeue(self):
            if not self.stackA:
                return None
            return self.stackA.pop()
```

## Analysis

Here, the enqueue process has to go through all the elements already in the queue (twice) and it has to add another element. This means that the enqueue process is being done in linear time (`O(n)`).

For the dequeue, we're just popping the top element off the stack. That means this is being  done in constant time (i.e. `O{1}`).

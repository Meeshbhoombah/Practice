# Technical Interview Preparation
**Week 1 – Wednesday, February 7th, 2018**
Problem Solving Practice Session
- 15 minutes: Write down 3 problem-solving strategies you want to use in technical interviews. 
  Discuss your strategies with a partner, and then share with the group.
- 30 minutes: Solve the programming problems below (in pseudocode or real code) on a small 
  whiteboard (or paper, if you prefer) as if you're in a technical interview.
- 20 minutes: Find a partner, explain your solution, review code and give feedback. Then 
  switch and repeat the process to give feedback in the opposite direction.
- 5 minutes: Discuss pitfalls, solutions, and problem solving strategies as a group.

## Programming Problems
1. Given a list of `n` numbers `a = [a0, a1, ..., an-1]` and a target sum `t`, find a pair of
   indexes `(i, j)` whose values add to the target sum. i.e., `a[i] + a[j] = t`

   Example: `find_pair(a=[1, 5, 3, 7, -2, 1], t=3)` returns `(1, 4)`
   Be sure to analyze the time complexity of your solution and attempt to improve it.
2. Given a string containing `n` words (such as a sentence or paragraph of text), return a 
   list of the `k` most commonly occurring words in descending order of frequency.
3. Reverse a linked list. (Use the same nodes, do not create new node objects). You can 
   assume this Python class exists:
   ```python
   class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
   ```


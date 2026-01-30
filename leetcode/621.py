# https://leetcode.com/problems/task-scheduler/description/


"""
621. Task Scheduler
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""

# learnings
""" 
Couldn't understand the question at first. Felt dumb, why is this medium?;)
Read the hints and comments to understand the question. Know that I need to use heaps but how to use it to solve this is tricky.
Whenever we have this kind of task, we first need to see how to reduce the largest number down so that we can reduce overall time together.
Don't go from small to big here as we need to optimize for the time.

Learnt how to use heaps along with queues together. 
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        vals = Counter(tasks)
        maxHeap = [-i for i in vals.values()]
        heapq.heapify(maxHeap)
        time_ = 0
        queue = deque()
        while maxHeap or queue:
            time_+=1
            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)
                if val:
                    queue.append((val, n + time_))
            if queue and queue[0][1] == time_:
                heapq.heappush(maxHeap, queue.popleft()[0])
            
        return time_
        
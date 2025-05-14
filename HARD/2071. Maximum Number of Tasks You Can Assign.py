# 2071. Maximum Number of Tasks You Can Assign
# Attempted
# Difficulty: Hard

# You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

# Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

# Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.



# Example 1:

# Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
# Output: 3
# Explanation:
# We can assign the magical pill and tasks as follows:
# - Give the magical pill to worker 0.
# - Assign worker 0 to task 2 (0 + 1 >= 1)
# - Assign worker 1 to task 1 (3 >= 2)
# - Assign worker 2 to task 0 (3 >= 3)
# Example 2:

# Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
# Output: 1
# Explanation:
# We can assign the magical pill and tasks as follows:
# - Give the magical pill to worker 0.
# - Assign worker 0 to task 0 (0 + 5 >= 5)
# Example 3:

# Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
# Output: 2
# Explanation:
# We can assign the magical pills and tasks as follows:
# - Give the magical pill to worker 0 and worker 1.
# - Assign worker 0 to task 0 (0 + 10 >= 10)
# - Assign worker 1 to task 1 (10 + 10 >= 15)
# The last pill is not given because it will not make any worker strong enough for the last task.


# Constraints:

# n == tasks.length
# m == workers.length
# 1 <= n, m <= 5 * 104
# 0 <= pills <= m
# 0 <= tasks[i], workers[j], strength <= 109

from typing import List

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(tasks)
        m = len(workers)
        tasks.sort()  # Sort tasks in ascending order
        workers.sort()  # Sort workers in ascending order
        
        def canComplete(k):
            from collections import deque
            if k > m:  # Can't complete more tasks than workers
                return False
                
            # Get k smallest tasks and k strongest workers
            curr_tasks = deque(tasks[:k])
            curr_workers = workers[m-k:]  # Get k strongest workers
            pills_remaining = pills
            worker_idx = k - 1  # Start from strongest worker
            
            while curr_tasks:
                task = curr_tasks[-1]  # Get largest remaining task
                worker = curr_workers[worker_idx]
                
                if worker >= task:  # Can complete without pill
                    curr_tasks.pop()
                    worker_idx -= 1
                elif pills_remaining > 0 and worker + strength >= task:
                    # Try finding the weakest worker who can do this task with a pill
                    left, right = 0, worker_idx
                    best = -1
                    while left <= right:
                        mid = (left + right) // 2
                        if curr_workers[mid] + strength >= task:
                            best = mid
                            right = mid - 1
                        else:
                            left = mid + 1
                            
                    if best != -1:  # Found a worker who can do it with pill
                        curr_tasks.pop()
                        pills_remaining -= 1
                        curr_workers.pop(best)
                        worker_idx -= 1
                    else:
                        return False
                else:
                    return False
                    
            return True
        
        # Binary search for the maximum number of tasks
        left, right = 0, min(n, m)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canComplete(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return result


# Example function call
solution = Solution()

# Example 1
tasks1 = [3, 2, 1]
workers1 = [0, 3, 3]
pills1 = 1
strength1 = 1
result1 = solution.maxTaskAssign(tasks1, workers1, pills1, strength1)
print(result1)  # Output: 3

# Example 2
tasks2 = [5, 4]
workers2 = [0, 0, 0]
pills2 = 1
strength2 = 5
result2 = solution.maxTaskAssign(tasks2, workers2, pills2, strength2)
print(result2)  # Output: 1

# Example 3
tasks3 = [10, 15, 30]
workers3 = [0, 10, 10, 10, 10]
pills3 = 3
strength3 = 10
result3 = solution.maxTaskAssign(tasks3, workers3, pills3, strength3)
print(result3)  # Output: 2
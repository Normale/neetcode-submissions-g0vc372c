from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)

        # heap stores: (-remaining_count, task_name)
        max_heap = []
        for task_name, count in task_counts.items():
            heapq.heappush(max_heap, (-count, task_name))

        # cooldown stores: (time_when_available_again, -remaining_count, task_name)
        cooldown = deque()

        time = 0

        while max_heap or cooldown:
            time += 1

            if max_heap:
                remaining_count, task_name = heapq.heappop(max_heap)

                # We processed this task once
                remaining_count += 1

                if remaining_count < 0:
                    cooldown.append((time + n, remaining_count, task_name))

            # Move cooled-down tasks back into the heap
            if cooldown and cooldown[0][0] == time:
                _, remaining_count, task_name = cooldown.popleft()
                heapq.heappush(max_heap, (remaining_count, task_name))

        return time
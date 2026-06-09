from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        t = 0
        last_done = dict()
        while True:
            most_common = c.most_common(1)[0]
            if most_common[1] == 0:
                break
            task = most_common[0]
            # check last done
            if t - last_done.get(task, float('-inf')) > n:
                print(f"doing {task} at time {t}")
                last_done[task] = t
                c[task] -= 1
            t += 1
        return t
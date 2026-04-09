class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = Counter(tasks)
        maxHeap = [-s for s in maxHeap.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        while q or len(maxHeap):
            time += 1
            if not maxHeap:
                time = q[0][1]
            
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        
        return time



        
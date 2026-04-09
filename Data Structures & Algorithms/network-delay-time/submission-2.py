class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u,v,w in times:
            edges[u].append((v,w))
        
        minHeap = [(0,k)]
        visit = set()
        t = 0
        while minHeap:
            weight, src = heapq.heappop(minHeap)
            if src in visit:
                continue
            visit.add(src)
            t = weight
            for dest,weightD in edges[src]:
                if dest not in visit:
                    heapq.heappush(minHeap,(weight + weightD,dest))
        return t if len(visit) == n else -1
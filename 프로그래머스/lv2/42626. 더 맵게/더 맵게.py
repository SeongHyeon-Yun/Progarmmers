import heapq as h

def solution(scoville, K):
    answer = 0
    h.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            return answer
        
        min1 = h.heappop(scoville)
        min2 = h.heappop(scoville)
        new_scoville = min1 + (min2 * 2)
        h.heappush(scoville, new_scoville)
        answer += 1

        
        
    return answer
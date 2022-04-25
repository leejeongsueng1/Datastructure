import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        a_food = heapq.heappop(scoville)
        b_food = heapq.heappop(scoville)
        new_food = a_food+ (2 * b_food)
        heapq.heappush(scoville,new_food)
        answer += 1
        if len(scoville) == 1 and scoville[0] <K:
            return -1
    
    return answer
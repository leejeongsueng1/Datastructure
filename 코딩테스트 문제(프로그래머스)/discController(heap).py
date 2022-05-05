import heapq

def solution(jobs):
    answer = 0
    heapq.heapify(jobs)
    job_list=[]
    heapq.heapify(job_list)
    for j in jobs:
        heapq.heappush(job_list,j[1])
        

    return answer



solution([[0, 3], [1, 9], [2, 6]])
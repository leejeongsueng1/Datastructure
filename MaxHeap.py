"""
최대힙

가장 큰 노드가 루트노드에 위치해야함
자식 노드는 부모노드보다 작아야 하고 완전 이진트리를 만족해야함

## Python 리스트를 이용한 최대힙 구현

    - 0번째 노드는 None으로 초기화 
        ==> 1번째 부터 데이터를 채워넣어 인덱스 계산을 편하게 하기 위함

    - 1번째 원소는 root node

    - 부모노드의 인덱스가 m 일때 좌, 우 자식노드의 인덱스는 각각 2m, 2m+1
    - 자식노드의 인덱스가 m 일때 부모노드의 인덱스는 m//2


## 리스트로 구현한 최대힙에서 insert 연산구현

    - 우선 리스트의 마지막에 주어진 데이터를 append
    - 해당 위치 인덱스를 m으로 잡고 m//2 인 부모노드와 비교하여
    - 자식이 더 클 경우 자리교체

    - 위 과정일 반복한 후 부모가 더 클 시에 반복문 탈출 및 종료



## 리스트로 구현한 최대힙에서 remove 연산구현

    - 최대힙에서 remove연산은 항상 최대값을 반환하는 연산
        ==> 루트노드가 존재하면 반환하면 됨
    
    - 우선 리스트의 가장 마지막 값과 루트(위치 인덱스 =1)의 위치를 스왑 후 마지막 값 pop(-1)
        ==> 루트 노드의 값을 빼내고 마지막원소를 채워넣음

    - 루트노드에 채워 넣었던 값을 자식노드들과 비교해가며 아래로 내려감
        ==> 재정렬 효과
    
    - 재귀적 호출을 통해 전체 정렬을 함

## maxHeapify

    - smallest(? 최댓값을 구해야하는데;;)
        ==> 부모노드, 자식노드(left, right) 세가지중 가장 큰 값의 인덱스를  가질 인덱스 변수
    
    - 먼저 left 자식노드가 존재하는 지 확인 후 left노드의 값이 samllest 의 값 보다 큰지 확인
        ==> left가 더 크다면 smallest 는 left로 교체
    
    - 다음 right 자식노드가 존재하는 지 확인후 right노드의 값이 smallest의 값보다 큰지 확인
        ==> right가 더 크다면 smallest 는 right로 교체

    - smallest가 i와 다르다면 두 값을 교체
        ==> 재귀적 호출을 통해 자료구조 끝까지 정렬



"""



class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        m = len(self.data)-1
        while m>1:
            if self.data[m] > self.data[m//2]:
                self.data[m],self.data[m//2] = self.data[m//2],self.data[m]
                m = m//2
            else:
                break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def maxHeapify(self,i):
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = i*2

        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = i*2 +1

        smallest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if left < len(self.data) and self.data[left]> self.data[smallest]:
            # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.
            smallest = left

        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if right < len(self.data) and self.data[right] > self.data[smallest]:
            # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            smallest = right

        if smallest != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[smallest], self.data[i] = self.data[i], self.data[smallest]

            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(smallest)

                


def heapsort(unsorted):
    H = MaxHeap()
    for e in unsorted:
        H.insert(e)
    
    sorted = []
    d = H.remove()
    while d:
        sorted.append(d)
        d = H.remove()
    return sorted
                


maxHeap = MaxHeap()

maxHeap.insert(1)
maxHeap.insert(5)
maxHeap.insert(3)
maxHeap.insert(4)
maxHeap.insert(2)
maxHeap.insert(7)
maxHeap.insert(6)
maxHeap.insert(9)

print(maxHeap.data)


print(heapsort([1,9,4,6,7,3,5,8])[::-1])
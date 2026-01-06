import sys, heapq

input = sys.stdin.readline

def ans(heap, n):
    for _ in range(n):
        x = int(input())
        if x == 0:
            if heap:
                print(heapq.heappop(heap))
            else:
                print(0)
        else:
            heapq.heappush(heap, x)

if __name__ == '__main__':
    n = int(input())
    heap = []
    ans(heap, n)




import math
import queue
from collections import defaultdict

def condition(x):
    a = str(x)
    b = a[::-1]
    if a == b and len(a) % 2 == 0:
        return True
    else : return False

if __name__ == "__main__" :
    T = int(input())
    for i in range(T):
        n = int(input())
        q = queue.Queue()
        a = []
        v = 0
        cnt = defaultdict(int)
        for i in range(0, 10, 2):
            value = v * 10 + i
            if cnt[value] == 0 and value < n:
                q.put(value)
                cnt[value] = 1
            for j in range(0, 10, 2):
                if cnt[value * 10 + j] == 0 and value * 10 + j < n:
                    q.put(value * 10 + j)
                    cnt[value * 10 + j] = 1

        while not q.empty():
            v = q.get()
            if v >= n:
                break
            if condition(v) == True:
                a.append(v)
            for i in range(0, 10, 2):
                value = v * 10 + i
                if cnt[value] == 0 and value < n:
                    q.put(value)
                    cnt[value] = 1
                for j in range(0, 10, 2):
                    if cnt[value * 10 + j] == 0 and value * 10 + j < n:
                        q.put(value * 10 + j)
                        cnt[value * 10 + j] = 1

        for i in range(len(a)):
            print(a[i], end = " ")
        print()
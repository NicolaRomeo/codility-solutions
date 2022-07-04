#OddOccurrencesInArray
from collections import Counter

def solution(A):
    if not A:
        return A
    if len(A) % 2 == 0:
        return len(A)

    c = Counter(A)
    new_list = [k for k,v in c.items() if v == 1 or v % 2 == 1]
    if new_list:
        return new_list[0]
    else:
        return A[0]


if __name__ == '__main__':
    # here you can test all the solutions with the following pattern
    A = [8,8,2,4,5,2,4,5,8]
    res = solution(A)
    print(res)

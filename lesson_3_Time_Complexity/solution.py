import math
'''
LINEAR COMPLEXITY (SLOWER)
    counter = 0
    while X < Y:
        counter += 1
        X += D
    return counter

'''

# Complexity: O(1)
def solution(X,Y,D):

    res = math.ceil((Y - X) / D)

    return res


if __name__ == '__main__':
    # here you can test all the solutions with the following pattern
    X = 1
    Y=1001
    D=10
    res = solution(X,Y,D)
    print(res)
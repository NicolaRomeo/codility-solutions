#Cyclic Rotation

def solution(A, K):
    if not A:
        return []
    for i in range(K):
        rotated_list = [0] * len(A)
        rotated_list[0] = A[-1]
        A.pop()
        for j in range(len(A)):
            rotated_list[j+1] = A[j]
        A = rotated_list
    return A


if __name__ == '__main__':
    # here you can test all the solutions with the following pattern
    A = []
    num_of_rotations = 3
    res = solution(A, num_of_rotations)
    print(res)
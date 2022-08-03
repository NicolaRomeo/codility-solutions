def solution(A):

    #here we just do a list comparison between the permutation and our list
    permutation = [i for i in range(1, len(A)+1)]

    if sorted(A) == sorted(permutation):
        return 1
    else:
        return 0


if __name__ == '__main__':
    A= [4,1,2,3,6]
    print(solution(A))
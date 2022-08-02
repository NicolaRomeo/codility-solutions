def solution(A):
    '''
    the array should contains elements from 1 to len(A).
    But one element is missing. Therefore we will have an array
    containing elements from 1 to len(A)+1. If for instance 1 is missing,
    and the array length is 7, then the remaining elements will be 2 to 8 (7 elements).
    The assumption is indeed that each element of array A is an integer within the range [1..(N + 1)].
    If we sum all of the elements from 1 to len(A)+2 and subtract from the sum of the
    actual list, we'll get the number that we want.
    '''
    if len(A) == 0:
        return 1
    return sum(range(1, len(A)+2)) - sum(A)

if __name__ == '__main__':
    A = [2,1,3,4,6,8,7]
    res = solution(A)
    print(res)
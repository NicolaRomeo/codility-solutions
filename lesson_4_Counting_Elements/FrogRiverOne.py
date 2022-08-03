def solution(X, A):
    """
    the basic assumption here is that
    each element of array A is an integer within the range [1..X].
    So we don't have to bother about random numbers.
    We make a dictionary because it allows us to only save the positions
    that are moving us forward: we overwrite the positions that are
    already covered.
    We return the index when there are X elements in the dictionary.
    """
    # count unique leaf positions and stop when there are enough
    leaves = {}
    for second in range(0, len(A)):
        leaves[A[second]] = True
        if len(leaves) == X:
            return second
    return -1

if __name__ == '__main__':
    A= [1,3,1,4,2,3,5,4]
    print(solution(5, A))
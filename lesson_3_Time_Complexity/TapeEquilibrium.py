def solution(A):

    #first we instantiate a minimal difference for comparison.
    assert len(A) > 1
    first_part = 0
    second_part = sum(A)
    min_diff = None

    # we don't split on the last element, so it's A[:-1]
    for num in A[:-1]:
        first_part += num
        second_part -= num
        curr_diff = abs(first_part - second_part)

        if min_diff is None or curr_diff < min_diff:
            min_diff = curr_diff
    return min_diff

if __name__ == '__main__':
    print(solution([-1000, 1000]))
def solution(N):
    binary_value = bin(N).replace("0b", "")
    binary_value = list(binary_value)
    all_binary_gaps = [0]
    binary_gap = 0
    zero_before = False
    one_before = False
    for i in binary_value:
        if i == '1':
            one_before = True
            if zero_before:
                one_after = True
                all_binary_gaps.append(binary_gap)
                binary_gap = 0
        if i == '0':
            if one_before:
                binary_gap += 1
                zero_before = True
    return max(all_binary_gaps)

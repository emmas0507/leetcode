def swap_adjacent_LR_string(start, end):
    i = 0
    j = 0
    n = len(start)
    while i < n and j < n:
        while start[i] == 'X':
            i = i + 1
        while end[j] == 'X':
            j = j + 1
        if start[i] != end[j]:
            return False
        if (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
            return False
        i = i + 1
        j = j + 1
    return True

start = "RXXLRXRXL"
end = "XRLXXRRLX"
print(swap_adjacent_LR_string(start, end))

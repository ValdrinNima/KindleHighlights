def solve(arr):
    workarr = []
    i = 0
    while arr[0:2] != [0,0]:
        for x in range(2):
            arr = sorted(arr)
            ind = (arr.index(max(arr)))
            bla = arr.pop(ind) - 1
            workarr.append(bla)
        arr.extend(workarr)
        arr = sorted(arr)
        i += 1
        workarr = []
    return i


print(solve([423,134,123]))


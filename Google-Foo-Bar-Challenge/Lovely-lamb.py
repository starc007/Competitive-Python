def solution(total_lambs):
    dList = []
    i = 0
    total = 0
    while i<total_lambs:
        cValue = 2**i
        dList.append(cValue)
        total += cValue
        if total > total_lambs:
            break
        i += 1

    fList = [1,1]
    fTotal = 2
    j = 2
    while j <total_lambs:
        val = fList[j-1] + fList[j-2]
        fList.append(val)
        fTotal += int(fList[j])
        if fTotal > total_lambs:
            break
        j += 1

    res = len(fList) - len(dList)
    return abs(res)

print(solution())                
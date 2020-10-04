def solution(l):
    if len(l) < 3: return 0

    cd = 0
    for i in range(1, len(l) - 1):
        X = len([x for x in l[:i] if l[i] % x == 0])  
        Z = len([z for z in l[i + 1:] if z % l[i] == 0])   
        cd += X * Z  
    return cd

print(solution([1,1]))
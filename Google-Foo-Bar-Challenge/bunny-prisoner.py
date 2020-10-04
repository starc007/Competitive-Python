def solution(x, y):
    ground = sum(i+1 for i in range(x))
    up = sum(j for j in range(x,x+y-1))
    return str(ground+up)

print(solution(5,1000000))


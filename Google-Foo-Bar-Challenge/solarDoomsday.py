import  math
def solution(area):
    aList = []
    _helper(area,aList)
    aList.reverse()
    for i in range(len(aList)):
        print(aList[i],end=",")

def _helper(area,aList):
    a = 0
    if area >= 1 and area <= 1000000:
        b = int(math.sqrt(area))
        if b<0: return a
        else:
            a = int(math.pow(b, 2));
            nArea = area - a;
            _helper(nArea, aList);
            aList.append(a);
        return a

solution(15324)

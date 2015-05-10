import random
mxxx = [0]*27
for _ in range(100):
    counter = 27*[0]
    for _ in range(10000):
        randy = random.randint(1,27)-1
        counter[randy] += 1
    mx = max(counter)
    mn = min(counter)
    mxx = (-1,-1)

    for i in range(len(counter)):
        cai = counter[i]
        if cai > mxx[1]:
            mxx = (i,cai)
    print (mxx[0]+1)
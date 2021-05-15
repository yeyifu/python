import time
stime=time.time()
a = ''
for i in range(10000000):
    a += 'axt'
etime=time.time()
print('运行时长：'+str(etime-stime))

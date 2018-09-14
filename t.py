
# -*- coding: utf-8 -*-
import time 
start_time=time.time()
k=0
for i in range(0,100000000000):
	k=k+i
end_time=time.time()
print(k,end_time-start_time)
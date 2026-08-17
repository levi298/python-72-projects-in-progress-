import time 


seconds=int(input("how many seconds to go :"))


for i in range (1,seconds+1): # for simpler for i in range(seconds,0,-1)
    print(seconds)
    seconds= seconds-1
    time.sleep(1)
    
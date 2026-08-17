import random 


scret = random.randint(1,100)
print(scret)



count = 1
while count <= 5: 
 guess=int(input("enter ur guess: "))
 if guess > scret :
     print("too HIGH")
 elif guess < scret :
     print("too LOWW")
 elif guess== scret :
     print("good")
     break
 count +=1 
if guess==scret:
 print("nice u won the num was :",scret)
else:
    print("u looose N the num was:",scret)
    
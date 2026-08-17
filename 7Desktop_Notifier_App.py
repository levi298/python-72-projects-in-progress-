import time
from plyer import notification 

title = input("what will be the title : ")

message = input("ur massage : ")

x=int(input("how many notification u want :  "))
seconds=int(input("set time : "))
seconds=seconds*60
for x in range (0,x):
    time.sleep(seconds) 
    notification.notify(

    title = title,
    message = message

    )


window_size=int(input("enter the window size: "))
sent=0
while(1):
    for i in range(0,window_size):
        print("frame",sent,"has been transmitted")
        sent=sent+1
        if(sent==window_size):
            break
        
    ack=int(input("enter the last acknowledgement received: "))
    if(ack==window_size):
        break
    else:
        sent=ack+1
print("transmission completed!!")

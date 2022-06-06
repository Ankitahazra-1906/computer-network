frame_size=int(input("enter the frame size: "))
for i in range(0,frame_size):
    frame=i+1
    while(True):
        ack=int(input("enter the acknowledgement: "))
        if frame==ack:
            print(str(i+1)+" is transmitted")
            print(str(i+1)+" acknowledgement is received")
            break
        else:
            print(str(i+1)+" acknowledgement is not received")
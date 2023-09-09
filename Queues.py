from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.list1=LinkedList()
        self.size=0
    def enqueue(self,c):
        self.list1.addToTail(c)
        self.size+=1
    def dequeue(self):#O(1)
        temp=self.list1.head
        self.list1.deleteHead()
        return temp.value.toString()
    def size(self):
        return self.size
    def isEmpty(self):
        if self.size==0:
            return True
        return False
    def front(self):
        if self.size==0:
            return "no cars"
        else:
            return self.list1.head.toString()
        

        
class Car:
    def __init__(self,name,color,plate):
        self.name=name
        self.color=color
        self.plate=plate
    def toString(self):
        return "Car name : "+self.name+"\n color : "+self.color+"\n plate number : "+str(self.plate)
    
def choice1():
    name=input("enter the name of the car : ")
    color=input("enter the color of the car : ")
    plate=input("enter the plate number : ")
    try:
        plate=int(plate)

    except:
        print("invalid input ")
    queue.enqueue(Car(name,color,plate))
    


    

queue=Queue()
choice1()
count=1
while(count>0):

    ch=input("1. To insert a car to the queue\n2. To remove the car from the queue \n")
    if ch=="1":
        choice1()
        count+=1
    

    elif ch=="2":
        print( queue.dequeue())
        count-=1




        



    

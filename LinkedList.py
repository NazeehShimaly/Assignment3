class Node:
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

class LinkedList:
    def __init__(self ):
        self.head=None
        self.tail=None
        self.size=0
    def addTohead(self,value):
        node=Node(value)
        if(self.size==0):
            self.head=node
            self.tail=node
            self.size+=1
            
        elif(self.size==1):
            self.head=node
            self.head.next=self.tail
            self.size+=1
           

        else:
            temp=self.head
            self.head=node
            self.head.next=temp
            self.size+=1
            
        
    def addToTail(self,value):
        node=Node(value)
        if(self.size==0):
            self.head=node
            self.tail=node
            self.size+=1
           
        
        elif(self.size==1):
            self.tail=node
            self.head.next=self.tail
            self.size+=1
          
        else:
            self.tail.next=node
            self.tail=self.tail.next
            self.size+=1
           
        
    def deleteHead(self):
        if(self.size==0):
            return None
        elif(self.size==1):
            temp=self.head
            self.head=None
            self.tail==None
            self.size-=1
            return temp.value

        else:
            temp=self.head.value
            self.head=self.head.next
            self.size-=1
            return temp
    def deleteTail(self):
        if(self.size==0):
            return None
        elif(self.size==1):
            temp=self.head
            self.head=None
            self.tail==None
            self.size-=1
            return temp.value
        else:
            temp=self.head
            t=self.tail
            for i in range (1,self.size-1):
                temp=temp.next
            self.tail=temp
            self.tail.next=None
            self.size-=1
            return  t



            
    

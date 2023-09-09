from LinkedList import LinkedList
class stack:
    def __init__(self):
        self.list2=[]
        self.len=0
    def additem(self,item):#O(n)=1
        self.list2.append(item)
        self.len+=1
    def removeItem(self):#O(n)=1
        temp=self.list2[len(self.list2)-1]
        self.list2.pop()
        self.len-=1
        return temp
class Queues:
    def __init__(self):
        self.linkedList=LinkedList()
    def addItem(self,item):#O(n)=1
        self.linkedList.addToTail(item)

    def removeItem(self):#O(n)=1
        temp=self.linkedList.head
        self.linkedList.deleteHead()
        return temp


def isPandrom(x):#O(n)=2n=n where n is the length of x
    y=tostack(x)
    temp=""
    for i in y.list2:
        temp=temp+y.removeItem()
    if str(x)==temp:
        return True
    return False

    
def tostack(x):# is part of the above function
    x=str(x)
    y=stack()
    for i in x:
        y.additem(i)
    return y

def isbalanced(expression):#O(n)=n*n where n is the length of the expression and num of the closing bracket in the stack
    openingBrackets="({["
    closingbracket="]})"
    count=0

    Stack=stack()
    for char in expression:
        if char in openingBrackets:
            Stack.additem(char)
            count+=1
        elif char in closingbracket:
            if char=="]":
                if "[" not in Stack.list2:
                    return False
                else:
                    count-=1
            if char==")":
                if "(" not in Stack.list2:
                    return False
                else:
                    count-=1
            if char=="}":
                if "{" not in Stack.list2:
                    return False
                else:
                    count-=1
    if count==0:
        return True
    return False
#print(isbalanced("(1+2)-3*[41+6}"))




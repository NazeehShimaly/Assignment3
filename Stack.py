from ass3 import stack
def decoding(messgae:str):
    Stack=stack()
    mess=""
    for char in messgae:
        if char=="*":
            mess=mess+Stack.removeItem()
        else:
            Stack.additem(char)
    while Stack.len!=0:
        mess=mess+Stack.removeItem()
    return mess
print(decoding("SIVLE ****** DAED TNSI ***"))


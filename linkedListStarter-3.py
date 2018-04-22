def createNode(value):
    node = {}
    node['data'] = value
    node['next'] = None
    return node

def addtoHead(alist, value):
    newnode = createNode(value)
    newnode['next'] = alist  #put the new node as the first node in the list
    return newnode

def printList(alist):
    ptr = alist
    while ptr != None:
        print(ptr['data'], "->", end=' ')
        ptr = ptr['next']
        
    print("None")

def generateList(alist, pythonList):
    #pythonList might look like [10, 20, 40, 83]
    for i in pythonList:
        alist = addtoHead(alist, i)
    return alist

def concatenateLists(alist, blist):
    #find the end of alist
    ptr = alist
    if ptr == None:
        return blist
    while ptr['next'] != None:
        ptr = ptr['next']

    #ptr now points to the last node in list alist
    ptr['next'] = blist
    return alist

def sumNodes(aList):
    summation = 0
    ptr = aList
    while ptr != None:
        summation = summation + ptr['data']
        ptr = ptr['next']
    return summation
        
    
        

def main():
    myList = None
    myList = addtoHead(myList, 20)
    myList = addtoHead(myList, 30)
    myList = addtoHead(myList, 40)
    printList(myList)
    myFirstList = None
    mySecondList = None
    mySecondList = generateList(mySecondList, [100, 200, 400, 450, 600])
    printList(mySecondList)
    concatenateLists(myList, mySecondList)
    printList(myList)
    printList(mySecondList)
    concatenateLists(myFirstList, mySecondList)
    print("The sum is ", sumNodes(mySecondList))



    
    

main()

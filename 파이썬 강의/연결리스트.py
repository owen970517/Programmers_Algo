class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next =None
    #특정 원소 참조
    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr
    #리스트 순회
    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result
    def insertAt(self,pos,newNode):
        if pos <1 or pos>self.nodeCount+1:
            return False
        if pos !=1 and pos == self.nodeCount+1:
            prev = self.tail
        else :
            prev = self.getAt(pos-1)
        return self.insertAfter(prev,newNode)
    # 두 개의 연결 리스트 연결 
    def concat(self,L2):
        self.tail.next = L2.head.next
        if L2.tail:
            self.tail = L2.tail
        self.nodeCount+=L2.nodeCount
    def insertAfter(self,prev ,newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount +=1
        return True
    def popAfter(self,prev) :
        curr = prev.next
        prev.next = curr.next
        if prev.next == None:
            if self.nodeCount == 1:
                self.tail = None
            else :
                self.tail = prev
        self.nodeCount-=1        
        return curr.data
    def popAt(self,pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        prev = self.getAt(pos-1)
        return self.popAfter(prev)
def solution(x):
    return 0

a = Node(67)
b = Node(34)
c = Node(28)
d = Node(30)
e = Node(50)
f = Node(70)
L = LinkedList()
L.insertAt(1,a)
L.insertAt(2,d)
L.insertAt(3,e)
L.insertAt(3,f)



print(L.traverse())

class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        index = len(self.data)-1
        while index >1 :
            if  self.data[index] >self.data[index//2]  :
                self.data[index//2] , self.data[index] = self.data[index],self.data[index//2]
                index = index//2

                


def solution(x):
    return 0
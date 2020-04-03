# The main idea is to keep a sorted list 
# find the max difference in sorted list 
# and assign the position.

class ExamRoom:

    def __init__(self,N):
        self.N = N
        self.sl = []

    def seat(self):
        if len(self.sl)==0:
            pos=0
        else:
            pos=0
            maxi=self.sl[0]-0
            for i in range(1,len(self.sl)):
                if (self.sl[i]-self.sl[i-1])//2>maxi:
                    pos=(self.sl[i]+self.sl[i-1])//2
                    maxi=(self.sl[i]-self.sl[i-1])//2
            if self.N-1-self.sl[-1]>maxi:
                pos=self.N-1
                maxi=self.N-1-self.sl[-1]
        self.sl.append(pos)
        self.sl.sort()
        print(self.sl)
        
    def leave(self,v):
        self.sl.remove(v)
        
# driver code
e=ExamRoom(10)
e.seat()
e.seat()
e.seat()
e.leave(0)
e.leave(4)
e.seat()
e.seat()
e.seat()
e.seat()
e.seat()
e.seat()
e.seat()
e.seat()
e.seat()
e.leave(0)
e.leave(4)
e.seat()
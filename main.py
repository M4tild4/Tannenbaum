K = [11]
l=[1,2,3,4,5,6,7,8,9,10,11]
l2=[3,3,3]
y= range(10,0,-2)
def krone(l):
    for k in K:
        for i in l:
            print((K[0]-i)*" ",(2*i-1)*"x", sep="")

def stamm(l2):
    for i in l2:
        print(9*" ",i*"x", sep="")

krone(l)
stamm(l2)


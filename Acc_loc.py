
t=0.1

acc =[100,200,300]

u=0

def distance (p):
 y=p**2/2
 return y

k=[0]*3

for i in range(0,3,1):
 k[i]=distance(t)*acc[i]
 
print("X_co: ", k[0])
print("Y_co: ", k[1])
print("Z_co: ", k[2])

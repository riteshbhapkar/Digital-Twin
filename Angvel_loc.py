
t=0.1

#test ang vels:
ang_vel = [100,200,300]

def distance (p):
 y=p*t
 return y

k=[0]*3

for i in range(0,3,1):
 k[i]=distance(ang_vel[i])


print("X_co: ", k[0])
print("Y_co: ", k[1])
print("Z_co: ", k[2])
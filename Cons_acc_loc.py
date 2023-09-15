t=0.1

acc =[100,200,300]


def distance (p):
 y=p**2/2
 return y


#calculation of v
while(t>0):
 v_x=acc[0]*t
 pos_x=distance(t)*acc[0]+(v_x*t)
 print("X_co: ", pos_x)
 
 v_y=acc[1]*t
 pos_y=distance(t)*acc[1]+(v_y*t)
 print("Y_co: ", pos_y)
 
 v_z=acc[2]*t
 pos_z=distance(t)*acc[2]+(v_z*t)
 print("Z_co: ", pos_z)
 print(" ")
 
 t=t+0.1
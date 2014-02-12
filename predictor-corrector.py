#####################
dt = 0.1
x0=1.
v0=0.
m=1.
k=1.
#####################
#spring function to return v and a
def spring(t,x):
    return np.array([x[1], -k/m*x[0]]) 

#Runge Kutta method
def RungKutta(x,f,t,dt):
    RK1 = f(t,x) * dt
    RK2 = f(t + dt/2, x + RK1/2) * dt
    RK3 = f(t + dt/2, x + RK2/2) * dt
    RK4 = f(t+ dt, x + RK3) * dt    
    return x + (1.0/6.0)*(RK1 + 2*RK2 + 2*RK3 + RK4)
 
 def Pre(x0,x1,f,t,dt):
    xp = x0 + (f(t,x1)*2*dt)
    return x1 + (0.5)*(f(t,xp) + f(t,x1))*dt
    
PC_time = [0]
PC_state = [np.array([x0,v0])]
while PC_time[-1] < 20: 
    if size(PC_time) == 1:
        PC_state.append(RungKutta(PC_state[-1],spring,PC_time[-1],dt))
        PC_time.append(PC_time[-1] + dt)
    PC_state.append(Pre(PC_state[-1-1],PC_state[-1],spring,PC_time,dt))
    PC_time.append(PC_time[-1] + dt)
PC_state = np.array(PC_state[:])
#the if statement is what I was talking about at the end of class, but I couldnt get it to work inside to the def of the pre

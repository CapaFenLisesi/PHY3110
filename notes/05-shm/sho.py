from visual import *
from visual.graph import *

L=0.11 #unstretched length of the spring
A=L/1.1 #amplitude of the oscillation

scene.autoscale=0
scene.range=1.2*L
scene.background=color.white

#put the wall at -L so that the other end of the spring is at the origin when unstretched
wall=box(pos=vector(-L,0,0), width=L/2., height=L/2., length=L/20., color=color.red)

#put the object at the position x=A so that the spring is initially stretched an amount A
mass=cylinder(pos=vector(A,0,0), axis=vector(L/20.,0,0), radius=L/10., color=(0.5,0.5,0.5))

spring=helix(pos=wall.pos, axis=mass.pos-wall.pos, radius=L/10., color=(1,0.7,0.2), thickness=L/100.)

xaxis=arrow(pos=vector(0,0,0), axis=vector(L,0,0), color=color.black, shaftwidth=L/50.)
yaxis=arrow(pos=vector(0,0,0), axis=vector(0,L,0), color=color.black, shaftwidth=L/50.)


graph=gdisplay(x=0,y=0,width=400, height=400,
			title='x vs t for object oscillating on a spring',
			xtitle='t (s)',
			ytitle='x (m)',
			xmax=4,
			ymax=1.1*A,
			ymin=-1.1*A,
			background=color.white,
			foreground=color.black)
			
function=gcurve(color=color.magenta)

mass.m=0.05
mass.v=vector(0,0,0)
mass.p=mass.m*mass.v

#spring constant
k=5	

#damping constant for velocity-dependent damping force
omega=sqrt(k/mass.m)
b=0.022

#damping constants for constant-magnitude damping force
c=0

dt=0.001
t=0

scene.mouse.getclick()

while t<6:
	rate(100)
	s=mass.pos

	if(mag(mass.p)==0):
		Fnet=-k*s
	else:
		#velocity dependent damping force
		Fnet= -k*s+-b*mag(mass.p/mass.m)*norm(mass.p)
		#constant magnitude damping force like friction
#		Fnet=-k*s-c*norm(mass.p)
	mass.p= mass.p+Fnet*dt
	mass.pos= mass.pos+mass.p/mass.m*dt

	spring.axis=mass.pos-spring.pos
	t=t+dt
	
	function.plot(pos=(t,mass.pos.x))
#	print t, "\t", mass.pos.x
	

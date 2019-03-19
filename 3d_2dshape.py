import sys
import time
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

window = 0

width, height = 800, 600

	
            

def init():
	glClearColor(1.0, 1.0, 1.0, 0.0)
	glColor3f(0.0,0.0,0.0)
	glPointSize(4.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-500.0, 500.0, -500.0, 500.0)
def trans3d():
	alpha = math.atan2(float(vy),float(vz)) #x-axis angle
	beta = math.atan2(float(vx),float(vz)) #y -axis angle 
	for i in range(nodes):  #only z-axis rotation to view point
		x=int(verticies[i][0])
		y=int(verticies[i][1])
		z=int(verticies[i][2])
		verticies[i][1]=(y*math.cos(alpha)*1.0-z*math.sin(alpha)*1.0)
		verticies[i][2]=(y*math.sin(alpha)*1.0+z*math.cos(alpha)*1.0)
	for i in range(nodes):
		x=int(verticies[i][0])
		y=int(verticies[i][1])
		z=int(verticies[i][2])
		verticies[i][2]=(z*math.cos(beta)*1.0-x*math.sin(beta)*1.0)
		verticies[i][0]=(z*math.sin(beta)*1.0+x*math.cos(beta)*1.0)
		
	
	alpha = math.atan2(float(vx),float(vy)) #x-axis angle
	beta = math.atan2(float(vz),float(vy)) #y -axis angle 
	for i in range(nodes):  #only z-axis rotation to view point
		x=int(verticies[i][0])
		y=int(verticies[i][1])
		z=int(verticies[i][2])
		verticies[i][0]=(x*math.cos(alpha)*1.0+y*math.sin(alpha)*1.0)
		verticies[i][1]=(-(x*math.sin(alpha)*1.0)+y*math.cos(alpha)*1.0)
	for i in range(nodes):
		x=int(verticies[i][0])
		y=int(verticies[i][1])
		z=int(verticies[i][2])
		verticies[i][1]=(y*math.cos(beta)*1.0-z*math.sin(beta)*1.0)
		verticies[i][2]=(y*math.sin(beta)*1.0+z*math.cos(beta)*1.0)
		
	alpha = math.atan2(float(vy),float(vx)) #x-axis angle
	beta = math.atan2(float(vz),float(vx)) #y -axis angle 
	for i in range(nodes):  #only z-axis rotation to view point
		x=int(verticies[i][0])
		y=int(verticies[i][1])
		z=int(verticies[i][2])
		verticies[i][0]=(x*math.cos(alpha)*1.0-y*math.sin(alpha)*1.0)
		verticies[i][1]=(y*math.sin(alpha)*1.0+x*math.cos(alpha)*1.0) 
		x=int(verticies[i][0])
		y=int(verticies[i][1])
		z=int(verticies[i][2])
		verticies[i][0]=(x*math.cos(beta)*1.0-z*math.sin(beta*1.0))
		verticies[i][2]=(x*math.sin(beta)*1.0+z*math.cos(beta)*1.0)
	for edge in edges:
		glBegin(GL_LINES)
		for i in edge:
			glVertex2f(verticies[i][0],verticies[i][1])
		glEnd()
	
def drawPolygon():
	glBegin(GL_LINES)
	for edge in edges:
		for i in edge:
		    	glVertex2f(verticies[i][0],verticies[i][1])
	glEnd()
	

def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0,0.0,0.0)
	#drawPolygon()
	trans3d() #simple x-y plane view through z-axis view
	glutSwapBuffers()	
	glFlush()
		


def main():

	global edges,nodes,Edges
	global choice
	global verticies,fverticies
	global tx,ty,tz,sx,sy,sz,alpha,beta,shx,shy,shz
	global vx,vy,vz
	print("For Polygon")
	
	nodes=int(input("Enter no of Nodes:  "))
	
	verticies=[([0]*3)for row in range(nodes)]
	fverticies=[([0]*3)for row in range(nodes)]
	for i in range(nodes):
		print("Enter Shape node Co-ordinate ",i+1)
		x,y,z=input().split()
		fverticies[i][0]=verticies[i][0]=int(x)
		fverticies[i][1]=verticies[i][1]=int(y)
		fverticies[i][2]=verticies[i][2]=int(z)
	Edges=int(input("Enter no of Edge:  "))
	
	edges=[([0]*2)for row in range(Edges)]
	for i in range(Edges):
		print("Enter Shape edge point ",i+1)
		x,y=input().split()
		edges[i][0]=int(x)
		edges[i][1]=int(y)
	
	print("3d shape view in 2d plane :")
	vx,vy,vz=input("Enter view point with respect origin ::  ").split()
	
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
	glutInitWindowSize(width, height)
	glutInitWindowPosition(0,0)
	glutCreateWindow(b'Basic Transformations')
	glutDisplayFunc(display)
	init()
	glutMainLoop()

main()

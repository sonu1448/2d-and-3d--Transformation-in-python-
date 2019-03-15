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

def drawPolygon():
	glBegin(GL_POLYGON)
	glColor3f(0.0,0.0,1.0)
	for i in range(edges):
		glVertex2f(sptr[i][0],sptr[i][1])
	glEnd()
def drawfinalshap():
	glBegin(GL_POLYGON)
	glColor3f(1.0,0.0,0.0)
	for i in range(edges):
		glVertex2f(ptr[i][0],ptr[i][1])
	glEnd()
def PolygonTrans(tx,ty):
	for i in range(edges):
		ptr[i][0],ptr[i][1]=(ptr[i][0]+float(tx),ptr[i][1]+float(ty))

def PolygonScale(sx,sy):
	for i in range(edges):
		ptr[i][0]=(ptr[i][0]*float(sx))
		ptr[i][1]=(ptr[i][1]*float(sy))

def PolygonRotation(angle):
	angleRad=float(angle)*(3.14159265/180)
	for i in range(edges):
		ptr[i][0]=(ptr[i][0]*math.cos(angleRad)-ptr[i][1]*math.sin(angleRad))
		ptr[i][1]=(ptr[i][0]*math.sin(angleRad)+ptr[i][1]*math.cos(angleRad))
		
def PllygonShare(shx,shy):
	for i in range(edges):
		ptr[i][0]=(int(ptr[i][0])*float(shx)+int(ptr[i][1]))
		ptr[i][1]=(int(ptr[i][1])*float(shy)+int(ptr[i][0]))	
		
def PllygonImage(sx,sy,tx,ty):
	sx=int(sx)
	sy=int(sy)
	tx=int(tx)
	ty=int(ty)
	a =float(math.atan2(float(ty)-float(sy),float(tx)-float(sx)))
	a= float(a)(180/3.14159265)
	PolygonTrans(-sx,-sy)
	PolygonRotation(-a)
	for i in range(edges):
		ptr[i][0]=(ptr[i][0])
		ptr[i][1]=-(ptr[i][1])
	PolygonRotation(a)
	PolygonTrans(sx,sy)
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0,0.0,0.0)
	drawPolygon()
	drawfinalshap()	
	glutSwapBuffers()	
	glFlush()
		


def main():

	global edges
	global choice
	global ptr,sptr
	global tx,ty,sx,sy,angle,shx,shy
	
	print("For Polygon")
	edges=int(input("Enter no of Edge:  "))
	ptr=[([0]*2)for row in range(edges)]
	sptr=[([0]*2)for row in range(edges)]
	for i in range(edges):
		print("Enter Co-ordinate for Vertex ",i+1)
		x, y=input().split()
		sptr[i][0]=ptr[i][0]=float(x)
		sptr[i][1]=ptr[i][1]=float(y)
		choice =1
	while(choice):
		print("0. for Exit ")
		print("1. Translation ")
		print("2. Scaling ")
		print("3. Rotation ")
		print("4. share ")
		print("5. Image about line")
		choice=int(input("ENTER YOUR CHOCE according to manue  :: "))
		if choice==1:
			tx, ty=input("Enter The Translation factor x and y").split()
			PolygonTrans(tx,ty)
		elif choice==2:
			sx,sy=input("Enter The Scaling factor x and y").split()
			PolygonScale(sx,sy)
		elif choice==3:
			angle=input("Enter Angle of Rotation	")
			PolygonRotation(angle)
		elif choice==4:
			shx,shy=input("Enter The Shairing factor x and y 	").split()
			PllygonShare(shx,shy)
		elif choice==5:
			sx,sy,tx,ty=input("Enter arbitrary line starting and ending point ").split()
			PllygonImage(sx,sy,tx,ty)
		else:
			break
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
	glutInitWindowSize(width, height)
	glutInitWindowPosition(0,0)
	glutCreateWindow(b'Basic Transformations')
	    
	    
	glutDisplayFunc(display)
	init()
	glutMainLoop()

main()

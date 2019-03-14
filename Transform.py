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
		glVertex2f(ptr[i][0],ptr[i][1])
	glEnd()
	
def drawPolygonTrans(tx,ty):
	glBegin(GL_POLYGON)
	glColor3f(1.0,1.0,0.0)
	for i in range(edges):
		glVertex2f(ptr[i][0]+float(tx),ptr[i][1]+float(ty))
	glEnd()
	
def drawPolygonScale(sx,sy):
	glBegin(GL_POLYGON)
	glColor3f(1.0,0.0,0.0)
	for i in range(edges):
		glVertex2f(ptr[i][0]*float(sx),ptr[i][1]*float(sy))
	glEnd()
	
def drawPolygonRotation(angle):
	angleRad=float(angle)*(3.14159265/180)
	glBegin(GL_POLYGON)
	glColor3f(1.0,0.0,0.0)
	for i in range(edges):
		glVertex2f(ptr[i][0]*math.cos(angleRad)-ptr[i][1]*math.sin(angleRad),ptr[i][0]*math.sin(angleRad)+ptr[i][1]*math.cos(angleRad))
	glEnd()
def drawPllygonShare(shx,shy):
	glBegin(GL_POLYGON)
	glColor3f(1.0,0.0,0.0)
	for i in range(edges):
		glVertex2f(int(ptr[i][0])*float(shx)+int(ptr[i][1]),int(ptr[i][1])*float(shy)+int(ptr[i][0]))
	glEnd()
	
	
def drawPllygonImage(sx,sy,tx,ty):
	sx=int(sx)
	sy=int(sy)
	tx=int(tx)
	ty=int(ty)
	glBegin(GL_POLYGON)
	#glColor3f(1.0,0.0,0.0)
	a = math.atan2(int(ty)-int(sy),int(tx)-int(sx)) 
	a=(a*180)/3.14159265
	a=-a
	for i in range(edges):
		ptr[i][0]=(ptr[i][0]-sx)
		ptr[i][1]=(ptr[i][1]-sy)
	"""for i in range(edges):
		glColor3f(0.0,0.0,1.0)
		glVertex2f(ptr[i][0],ptr[i][1])"""
	for i in range(edges):
		p=int(ptr[i][0])
		q=int(ptr[i][1])
		ptr[i][0]=int(p*math.cos(a)-q*math.sin(a))
		ptr[i][1]=int(p*math.sin(a)+q*math.cos(a))
	"""	for i in range(edges):
		glColor3f(1.0,0.0,0.0)
		glVertex2f(ptr[i][0],ptr[i][1])
		"""
	for i in range(edges):
		glColor3f(1.0,1.0,0.0)
		ptr[i][0]=(ptr[i][0])
		ptr[i][1]=-(ptr[i][1])
	"""for i in range(edges):
		glVertex2f(ptr[i][0],ptr[i][1])"""
	a=-a
	for i in range(edges):
		glColor3f(0.0,1.0,0.0)
		p=int(ptr[i][0])
		q=int(ptr[i][1])
		ptr[i][0]=(p*math.cos(a)-q*math.sin(a))
		ptr[i][1]=(p*math.sin(a)+q*math.cos(a))
	"""for i in range(edges):
		glVertex2f(ptr[i][0],ptr[i][1])"""
	for i in range(edges):
		glColor3f(1.0,0.0,0.0)
		glVertex2f(ptr[i][0]*(1)+float(sx),ptr[i][1]*int(1)+float(sy))	
		
	glEnd()
	
def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0,0.0,0.0)
	if(choice==1):
		drawPolygon()
		drawPolygonTrans(tx,ty)
	elif choice==2:
		drawPolygon()
		drawPolygonScale(sx,sy)
	elif choice==3:
		drawPolygon()
		drawPolygonRotation(angle)
	elif choice==4:
		drawPolygon()
		drawPllygonShare(shx,shy)
	else:
		drawPolygon()
		drawPllygonImage(sx,sy,tx,ty)	
	glutSwapBuffers()	
	glFlush()
		


def main():

	global edges
	global choice
	global ptr
	global tx,ty,sx,sy,angle,shx,shy
	print("1. Translation ")
	print("2. Scaling ")
	print("3. Rotation ")
	print("4. share ")
	print("5. Image about line")
	choice=int(input("ENTER YOUR CHOCE according to manue  :: "))
	print("For Polygon")
	
	edges=int(input("Enter no of Edge:  "))
	
	ptr=[([0]*2)for row in range(edges)]
	for i in range(edges):
		print("Enter Co-ordinate for Vertex ",i+1)
		x, y=input().split()
		ptr[i][0]=float(x)
		ptr[i][1]=float(y)
	
	if choice==1:
		tx, ty=input("Enter The Translation factor x and y").split()
	elif choice==2:
		sx,sy=input("Enter The Scaling factor x and y").split()
	elif choice==3:
		angle=input("Enter Angle of Rotation	")
	elif choice==4:
		shx,shy=input("Enter The Shairing factor x and y 	").split()
	else:
		sx,sy,tx,ty=input("Enter arbitrary line starting and ending point ").split()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
	glutInitWindowSize(width, height)
	glutInitWindowPosition(0,0)
	glutCreateWindow(b'Basic Transformations')
	    
	    
	glutDisplayFunc(display)
	init()
	glutMainLoop()

main()

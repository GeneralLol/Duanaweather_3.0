'''
This program is the test program for Python GUI with pyOpenGL. 

'''

import sys
from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *

def main():
    pass

#Handler for rendering and such
def display():
    #Clear previous buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    #Render stuff
    
    #Write the new buffer in place
    glutSwapBuffers()
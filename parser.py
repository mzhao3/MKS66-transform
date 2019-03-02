from display import *
from matrix import *
from draw import *
import os
"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    text = f.read()
    text = text.splitlines()

    #print(type(g))
    #for x in range(len(text)):

    for x in range(len(text)):
        #print x
        if (text[x].strip() == "line"):
            edges = text[x + 1]
            edges = edges.split()
            #print(edges)
            #x0 = int(edges[0])
            #y0 = int(edges[1])
            #z0 = int(edges[2])
            x1 = int(edges[3])
            y1 = int(edges[4])
            z1 = int(edges[5])
            add_point( points, x1, y1, z1 )
            print_matrix(points)
            x = x + 2
        if (text[x].strip() == "display"):
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            os.system("open pic.png")
        if (text[x].strip() == "ident"):
            ident(transform)
        if (text[x].strip() == "scale"):
            scalar = text[x + 1]
            scalar = scalar.split()
            sx = int(scalar[0])
            sy = int(scalar[1])
            sz = int(scalar[2])
            m_scale = make_scale(sx, sy, sz)
            matrix_mult(m_scale, transform)
            x = x + 2
        if (text[x].strip() == "move"):
            translator = text[x + 1]
            translator = translator.split()
            tx = int(translator[0])
            ty = int(translator[1])
            tz = int(translator[2])
            m_trans = make_translate(tx, ty, tz)
            matrix_mult(m_trans, transform)
            x = x + 2
        if (text[x].strip() == "rotate"):
            rotator = text[x + 1]
            rotator = rotator.split()
            axis = rotator[0]
            theta = int(rotator[1])

            if (axis.strip() == 'x'):
                m_rot = make_rotX(theta)
            if (axis.strip() == 'y'):
                m_rot = make_rotY(theta)
            if (axis.strip() == 'z'):
                m_rot = make_rotZ(theta)

            matrix_mult(m_rot, transform)
            x = x + 2
        if (text[x].strip() == "apply"):
            matrix_mult(transform, points)
            save_ppm(screen, "pic.png")
        if (text[x].strip() == "save"):
            name = text[x + 1]
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_ppm(screen, "pic.png")
        #print x

    #print text

"""tile.py: Simulation of pattern of tiles

__author__ = 'Sang'
__pkuid__ = '1600017765'
__email__ = 'johnbirdsang@pku.edu.cn'
"""

import turtle
import time


def tile(floor, pattern):
    """Main function of agrithom.
    """
    if floor[2:] == '1' * M*N:
        pats.append(pattern[:])
        return 0
    
    blank = int(floor[2:].index('0'))
    bx = blank % M
    by = blank // M
    
    if ((bx > (M-m)) or (by > (N-n))): #Horizonal
        pos_h = ['1'] * M*N
    else:
        pos_h = ['0'] * M*N
        for i in range(m):
            for j in range(n):
                pos_h[blank + i + j*M] = '1'
    pos_h = ''.join(pos_h)
    if not (int(pos_h, 2) & int(floor, 2)):
        floor = bin(int(pos_h, 2) | int(floor, 2))
        pattern.append((blank, 'h'))
        tile(floor, pattern)
        pattern.remove((blank, 'h'))
        floor = bin(int(pos_h, 2) ^ int(floor, 2))

    if ((bx > (M-n)) or (by > (N-m))): #Vertical
        pos_v = ['1'] * M*N
    else:
        pos_v = ['0'] * M*N
        for i in range(m):
            for j in range(n):
                pos_v[blank + j + i*M] = '1'
    pos_v = ''.join(pos_v)
    if not (int(pos_v, 2) & int(floor, 2)):
        floor = bin(int(pos_v, 2) | int(floor, 2))
        pattern.append((blank, 'v'))
        tile(floor, pattern)
        pattern.remove((blank, 'v'))
        floor = bin(int(pos_v, 2) ^ int(floor, 2))
    

def input_t():
    """get USER's input.
    Use turtle module to display.
    """
    tup = eval(turtle.textinput('Input', \
'''Please input the size of the floor and the tile.
Type in form of (M, N, m, n) where
    M*N is the size of the floor and
    m*n is the size of the tile:'''))
    return tup


def translate(piece):
    """Translate the position of a tile in a pattern
    from the form of (pos_of_lefttop, 'direct') into
    (.., i+m*j, ..) and (x1, x2, y1, y2) in order to
    br printed or to be painted.
    """
    (blank, direct) = piece
    poslist = []
    x1 = blank % M
    y1 = blank // M
    if direct == 'h':
        x2 = x1 + m - 1
        y2 = y1 + n - 1
    elif direct == 'v':
        x2 = x1 + n - 1
        y2 = y1 + m - 1
    for j in range(y1, y2 + 1):
        poslist.extend(range(x1 + M * j, x2 + 1 + M * j))
    return (tuple(poslist), (x1, x2, y1, y2))


def choose_t():
    """Choose a pattern by USER.
    Use turtle module to display.
    """
    prompt1 = 'Choose one of the pattern following.\n'
    prompt2 = ''
    for i in range(len(pats)):
        poslist = []
        for i_piece in pats[i]:
            poslist.append(translate(i_piece)[0])
        pro = str(i) + '):\t' + str(poslist)
        prompt2 = prompt2 + pro + '\n'
    prompt3 = 'Type the number before the pattern:'
    prompt = prompt1 + prompt2 + prompt3

    print(prompt1 + prompt2)
    num = int(turtle.numinput('Choose a pattern',\
                            prompt, 0, 0, len(pats)-1))
    pattern = pats[num]
    return pattern


def paint(pattern):
    """Paint the pattern chosen
    """
    turtle.width(4)
    turtle.shape('circle')
    ul = 500 / max(M, N) #unit length
    leb = - ul * M * 0.5 #left border
    upb = ul * N * 0.5 #up border
    turtle.fillcolor('lightgrey')
    
    for i in pattern:
        turtle.begin_fill()
        (x1, x2, y1, y2) = translate(i)[1]
        le = leb + x1 * ul
        rt = leb + (x2+1) * ul
        up = upb - y1 * ul
        dn = upb - (y2+1) * ul
        turtle.penup()
        turtle.goto(le, up)
        turtle.showturtle()
        turtle.pendown()
        turtle.goto(rt, up)
        turtle.goto(rt, dn)
        turtle.goto(le, dn)
        turtle.goto(le, up)
        turtle.end_fill()
        turtle.hideturtle()
        for pos in translate(i)[0]:
            turtle.penup()
            x = pos % M + 0.5
            y = pos // M + 0.8
            turtle.goto(leb + ul * x, upb - ul * y)
            turtle.write(arg=pos, align='center',
                         font=('Arial', int(ul/2.5), 'normal'))
            turtle.pendown()
            
        
def main():
    """Main function.
    """
    global M, N, m, n, pats
    pats = []
    (M, N, m, n) = input_t()
    floor = '0b' + '0' * M*N
    tile(floor, [])
    paint(choose_t())


if __name__ == '__main__':
    main()

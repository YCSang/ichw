"""tile.py: Simulation of pattern of tiles

__author__ = 'Sang'
__pkuid__ = '1600017765'
__email__ = 'johnbirdsang@pku.edu.cn'
"""

import turtle

##This fuction Line 11-39 is added
def recur(pat, M, N, m, n):
    is_Finished = True
    for i_piece in pat:
        is_Finished = is_Finished and check_tile(i_piece, m, n)
    if is_Finished:
        pat.sort()
        if pat not in pats:
            pats.append(pat[:])
        return 0
    if not check_pat(pat, m, n):
        return 0

    for piece in pat:
        if not check_tile(piece, m, n):
            (x1, x2, y1, y2) = piece
            pat.remove(piece)
            for i in range(x1, x2):
                new_pieces = [(x1, i, y1, y2), (i+1, x2, y1, y2)]
                pat.extend(new_pieces)
                recur(pat, M, N, m, n)
                for k in new_pieces:
                    pat.remove(k)
            for j in range(y1, y2):
                new_pieces = [(x1, x2, y1, j), (x1, x2, j+1, y2)]
                pat.extend(new_pieces)
                recur(pat, M, N, m, n)
                for k in new_pieces:
                    pat.remove(k)
            pat.append(piece)
            
            
def dissect(M, N, m, n):
    """Main function.
    M and N refer to size of floor.
    m and n refer to size of tile.
    """
    list_pat = [[(0, M-1, 0, N-1)]]
    is_Finished = False

    while not is_Finished:
        new_list_pat = []
        is_Finished = True
        for i_pat in list_pat:
            if check_pat(i_pat, m, n):
                for i_piece in i_pat:
                    if not check_tile(i_piece, m, n):
                        new_list_pat.extend(split(i_piece, i_pat[:]))
                        is_Finished = False
                    else:
                        is_Finished = is_Finished \
                                      and check_tile(i_piece, m, n)
        if not is_Finished:
            list_pat = new_list_pat[:]

    patterns = []
    for i_pat in list_pat:
        if check_pat(i_pat, m, n):
            i_pat.sort()
            if i_pat not in patterns:
                patterns.append(i_pat)

    return patterns


def check_pat(pat, m, n):
    """Check if this pattern reasonable, which means
    this pattern can be filled up by given tiles.
    piece is a tuple like (x1, x2, y1, y2)
    """
    is_Pattern = True
    for i in pat:
        (x1, x2, y1, y2) = i
        M_ = x2 - x1 + 1
        N_ = y2 - y1 + 1
        is_Size = ((M_*N_) % (m*n) == 0)
##        is_M = (M_ % m == 0) or (M_ % n == 0)
##        is_N = (N_ % m == 0) or (N_ % n == 0)

        ##This part Line 90-91 is added
        is_M = (M_ > m) or (M_ > n)
        is_N = (N_ > m) or (N_ > n)
        
        is_Piece = is_Size and is_M and is_N
        is_Pattern = is_Pattern and is_Piece
    return is_Pattern


def check_tile(piece, m, n):
    """Check if this pattern is just in
    the same shape as the given tile.
    piece is a tuple like (x1, x2, y1, y2)
    """
    (x1, x2, y1, y2) = piece
    M_ = x2 - x1 + 1
    N_ = y2 - y1 + 1
    is_Tile = ((M_ == m) and (N_ == n)) or ((M_ == n) and (N_ == m))
    return is_Tile


def split(piece, pat):
    """Split one piece in to two pieces
    and add them into lists.
    piece is a tuple like (x1, x2, y1, y2)
    """
    (x1, x2, y1, y2) = piece
    pat.remove(piece)
    derivates = []
    for i in range(x1, x2):
        new_pieces = [(x1, i, y1, y2), (i+1, x2, y1, y2)]
        new_pat = pat[:]
        new_pat.extend(new_pieces)
        derivates.append(new_pat)
    for j in range(y1, y2):
        new_pieces = [(x1, x2, y1, j), (x1, x2, j+1, y2)]
        new_pat = pat[:]
        new_pat.extend(new_pieces)
        derivates.append(new_pat)
    return derivates


def translate(piece, M):
    """Translate the position of a tile in a pattern
    from the form of (x1, x2, y1, y2) into (.., i+m*j, ..)
    """
    (x1, x2, y1, y2) = piece
    poslist = []
    m = x2 - x1 + 1
    for j in range(y1, y2 + 1):
        poslist.extend(range(x1 + M * j, x2 + 1 + M * j))
    return tuple(poslist)


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


def choose_t(patterns, M):
    """Choose a pattern by USER.
    Use turtle module to display.
    """
    prompt1 = 'Choose one of the pattern following.\n'
    prompt2 = ''
    for i in range(len(patterns)):
        poslist = []
        for i_piece in patterns[i]:
            poslist.append(translate(i_piece, M))
        pro = str(i) + '):\t' + str(poslist)
        prompt2 = prompt2 + pro + '\n'
    prompt3 = 'Type the number before the pattern:'
    prompt = prompt1 + prompt2 + prompt3

    num = int(turtle.numinput('Choose a pattern',\
                            prompt, 0, 0, len(patterns)-1))
    pattern = patterns[num]
    return pattern


def paint(pattern, M, N):
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
        (x1, x2, y1, y2) = i
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
        for pos in translate(i, M):
            turtle.penup()
            x = pos % M + 0.5
            y = pos // M + 0.9
            turtle.goto(leb + ul * x, upb - ul * y)
            turtle.write(arg=pos, align='center',
                         font=('Arial', int(ul/2.5), 'normal'))
            turtle.pendown()


def main():
    """Main function.
    """
    turtle.setup(600, 600)
    (M, N, m, n) = input_t()
    
    ##This part Line 220-224 is added
    global pats                         
    pats = []
    floor = [(0, M-1, 0, N-1)]
    recur(floor, M, N, m, n)
    print(len(pats))
    
##    patterns = dissect(M, N, m, n)
    
    pattern = choose_t(patterns, M)
    paint(pattern, M, N)


if __name__ == '__main__':
    main()

"""tile.py: Simulation of pattern of tiles

__author__ = 'Sang'
__pkuid__ = '1600017765'
__email__ = 'johnbirdsang@pku.edu.cn'
"""

import turtle


def dissect(M, N, m, n):
    """Main function of algebra.
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
            pat = []
            for i_piece in i_pat:
                (x1, x2, y1, y2) = i_piece
                piece = (x1+M*y1, x2+M*y2)
                pat.append(piece)
            pat.sort()
            if pat not in patterns:
                patterns.append(pat)

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
        is_M = (M_ % m == 0) or (M_ % n == 0)
        is_N = (N_ % m == 0) or (N_ % n == 0)
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


def input_t():
    """get USER's input.
    Use turtle module to display.
    """
    scr1 = turtle.Screen()
    tup = eval(scr1.textinput('Input', \
'''Please input the size of the floor and the tile.
Type in form of (M, N, m, n) where
    M*N is the size of the floor and
    m*n is the size of the tile:'''))
    return tup


def choose_t(patterns):
    """Choose a pattern by USER.
    Use turtle module to display.
    """
    prompt1 = 'Choose one of the pattern following.\n'
    prompt2 = ''
    for i in range(len(patterns)):
        pro = str(i) + '):\t' + str(patterns[i])
        prompt2 = prompt2 + pro + '\n'
    prompt3 = 'Type the number before the pattern:'
    prompt = prompt1 + prompt2 + prompt3
    
    scr2 = turtle.Screen()
    num = int(scr2.numinput('Choose a pattern',\
                            prompt, 0, 0, len(patterns)-1))
    pattern = patterns[num]
    return pattern


def paint(pattern, M, N):
    """Paint the pattern chosen
    """
    turtle.width(4)
    turtle.hideturtle()
    ul = 500 / max(M, N) #unit length
    leb = - ul * M * 0.5 #left border
    upb = ul * N * 0.5 #up border
    turtle.fillcolor('lightgrey')
    
    for i in pattern:
        turtle.begin_fill()
        x1 = i[0] % M
        y1 = i[0] // M
        x2 = i[1] % M
        y2 = i[1] // M
        le = leb + x1 * ul
        rt = leb + (x2+1) * ul
        up = upb - y1 * ul
        dn = upb - (y2+1) * ul
        turtle.penup()
        turtle.goto(le, up)
        turtle.pendown()
        turtle.goto(rt, up)
        turtle.goto(rt, dn)
        turtle.goto(le, dn)
        turtle.goto(le, up)
        turtle.end_fill()
        

def main():
    """Main function.
    """
    turtle.setup(600, 600)
    (M, N, m, n) = input_t()
    patterns = dissect(M, N, m, n)
    pattern = choose_t(patterns)
    paint(pattern, M, N)


if __name__ == '__main__':
    main()

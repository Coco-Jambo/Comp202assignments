#Réda Alidrissi-Omari
#261068776

MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'


def get_nth_row_from_map(map_string, n, width, height):
    """(String, int, int, int)->String
    Returns a srting that is the nth row from map_string that is bounded by the width and height of the map.
    Where n, height and width are positive integers
    
    >>>  get_nth_row_from_map('...>>>^^^', 2, 3, 3)
    '^^^'
    >>>  get_nth_row_from_map('...>>>^^^', 3, 3, 3)
    ''
    >>>  get_nth_row_from_map('...>>>^^^', 0, 3, 3)
    '...'
    """
    nth_row = map_string[width*n:(n*width)+width]
    return nth_row

def print_treasure_map(map_string, width, height):
    """(String, int, int)->None
    Prints a map bounded by height and width using map_string, where height and width are positive integers
    >>> print_treasure_map("...<<^>>>",3,3)
    ...
    <<^
    >>>
    
    >>> print_treasure_map("..>><<",2,3)
    ..
    >>
    <<

    >>> print_treasure_map("..>><<..",4,2)
    ..>>
    <<..
    """
    i=0
    while i < height:
        print(get_nth_row_from_map(map_string, i, width, height))
        i+=1

def change_char_in_map(map_string, row, column, c, width, height):
    """ (String, int, int, String, int, height)->String
    Returns a String which is the original map_string bounded by width and height with the character at
    the row and column in the inputs being replaced by the character c. Where row, column, width and height
    are positive integers.
    
    >>> change_char_in_map('.........', 2, 1, 'X', 3, 3)
    '.......X.'
    >>> change_char_in_map('.........', 2, 2, 'X', 3, 3)
    '........X'
    >>> change_char_in_map('.........', 2, 3, 'X', 3, 3)
    '.........'
    """
    if column>(width-1) or row>(height-1):
        new_map_string = map_string
    else:
        #this variable is created just to make the line below smaller
        x = width*row+column
        new_map_string = map_string[:x] +c+ map_string[1+x:]
    
    return new_map_string

def get_proportion_travelled(map_string):
    """(String)->float
    Returns the percentage of the map_string with BREADCRUMB_SYMBOL as a float
    rounded to two decimal values
    
    >>> get_proportion_travelled('.X..X.XX.')
    0.44
    >>> get_proportion_travelled('.X..X....')
    0.22
    >>> get_proportion_travelled('XXX.>>')
    0.5
    """
    
    percentage = float(map_string.count(BREADCRUMB_SYMBOL)/len(map_string))
    return round(percentage,2)
    
def get_nth_map_from_3D_map(map_string, n, width, height, depth):
    """(String, int, int, int, int)->String
    Returns a srting that is the nth map from map_string that is bounded by the width, height, and dedpth of the map.
    Where n, height, width and depth are positive integers
    
    >>> get_nth_map_from_3D_map('.X.XXX.X..v.vXv.v.', 0, 3, 3, 2)
    '.X.XXX.X.'
    >>> get_nth_map_from_3D_map('....,,,,', 0, 2, 2, 2)
    '....'
    >>> get_nth_map_from_3D_map('....,,,,', 1, 2, 2, 2)
    ',,,,'
    """
    nth_row = map_string[(width*height*n):(width*height*n)+(height*width)]
    return nth_row

def print_3D_treasure_map(map_string, width, height,depth):
    """(String, int, int, int)->None
    Prints a map bounded by height, width and depth using map_string, where height, width and depth
    are positive integers
   
   >>> print_3D_treasure_map('.X.XXX.X..v.vXv.v.', 3, 3, 2)
    .X.
    XXX
    .X.

    .v.
    vXv
    .v.
    
    >>> print_3D_treasure_map('...,,,...,,,...,,,', 3, 3, 2)
    ...
    ,,,
    ...

    ,,,
    ...
    ,,,
    
    >>> print_3D_treasure_map('>>>>....<<<<,,,,', 4, 2, 2)
    >>>>
    ....

    <<<<
    ,,,,
    """
    
    i=0
    while i < height*depth:
        if(i != 0 and i%height == 0):
            print("")
        
        print(get_nth_row_from_map(map_string, i, width, height))
        i+=1

def change_char_in_3D_map(map_string, row, column, depth_index, c, width, height, depth):
    """(String, int, int, int, String, int, int, int)->String
    Returns a String which is the original map_string bounded by width, height and depth, with the character at
    the row, column and depth index in the inputs being replaced by the character c. Where row, column, width,
    height, depth and depth_index are positive integers.
    
    >>> change_char_in_3D_map('.X.XXX.X..v.vXv.v.', 0, 0, 0, '#', 3, 3, 2)
    '#X.XXX.X..v.vXv.v.'
    >>> change_char_in_3D_map('.X.XXX.X..v.vXv.v.', 0, 0, 1, '#', 3, 3, 2)
    '.X.XXX.X.#v.vXv.v.'
    >>> change_char_in_3D_map('.X.XXX.X..v.vXv.v.', 2, 2, 1, '#', 3, 3, 2)
    '.X.XXX.X..v.vXv.v#'
    """
    if column>(width-1) or row>(height-1) or depth_index>(depth-1):
        new_map_string = map_string
    else:
        #these are just variables created to make the lines below smaller
        x = width*row+column
        y=(depth_index*(width*height+ width*row + column))
        
        if depth_index ==0:
            new_map_string = map_string[:x] +c+ map_string[1+x:]
        else:
            new_map_string = map_string[:y] +c+ map_string[1+y:]
    
    return new_map_string
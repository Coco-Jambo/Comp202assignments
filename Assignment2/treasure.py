#Réda Alidrissi-Omari
#261068776

import random 
import treasure_utils as utils

def generate_treasure_map_row(width, is3D):
    """ (int, boolean)-> String
    Returns a randomly generated String of length width and contains special characters if is3D is True,
    where width is a positive integer
    
    >>> random.seed(50056)
    >>> generate_treasure_map_row(9, True)
    '<^.v|.vv>'
    
    >>> random.seed(50056)
    >>> generate_treasure_map_row(9, False)
    '<^.v>.vv>'
    
    >>> generate_treasure_map_row(20, True)
    '>v^^.*v.<><<<.v^>^>v'
    """
    
    map_row=""
    
    for i in range (width):
        if random.random() < 1/6:
            map_row += "."
        else:
            map_row += utils.MOVEMENT_SYMBOLS[random.randint(0,3)]
             
    if is3D and random.random()<1/2:
        symbol = utils.MOVEMENT_SYMBOLS_3D[random.randint(0,1)]
        random_index = random.randint(0,width-1)
        map_row = map_row[:random_index] +symbol+ map_row[1+random_index:]

    return map_row

def generate_treasure_map(width, height, is3D):
    """(int, int, boolean)->String
    Returns a map bounded by width and height, whose rows are randomly generated depending if is3D is True or False
    Where width and height are positive integers
    
    >>> random.seed(50056)
    >>>  generate_treasure_map(3, 3, False)
    '>^.v>.vv>'
    
    >>> random.seed(50056)
    >>>  generate_treasure_map(3, 3, True)
    '>^|..|>vv'
    
    >>>  generate_treasure_map(4, 3, True)
    '>.<<.*>..^><'
    """
    
    treasure_map = ""
    
    for i in range (height):
        treasure_map += generate_treasure_map_row(width,is3D)
    
    treasure_map = ">" + treasure_map[1:]
    return treasure_map

def generate_3D_treasure_map(width, height, depth):
    """(int, int, int)->String
    Returns a map bounded by width,height and depth, whose rows are randomly generated
    Where width, height and depth are positive integers
    
    >>> random.seed(50056)
    >>> generate_3D_treasure_map(3, 3, 3)
    '>^|..|>vv>.<>v*.^>>^>.><|<>'
    
    >>> random.seed(50056)
    >>> generate_3D_treasure_map(2, 2, 2)
    '>|>.>|>.'

    >>> random.seed(50056)
    >>> generate_3D_treasure_map(4, 2, 2)
    '>^.v.v|>>.<^>*>.'
    """
    
    treasure_map = ""
    
    for i in range (depth):
        previous_map = generate_treasure_map(width,height,True)
        treasure_map += previous_map
    
    return treasure_map

def follow_trail(treasure_map, starting_row, column_index, depth_index, width, height, depth, nb_tiles):
    """(String, int, int, int, int, int, int, int)->String
    Returns a string bounded by width, height, and depth with the movement symbols replaced by breadcrumb
    symbols nb_tiles times starting from starting_row, column_index and depth_index.
    Where width, height, depth, nb_tiles, starting_row, column_index and depth_index are positive integers.
    
    >>> follow_trail('>+....', 0, 0, 0, 3, 2, 1,100)
    Treasures collected: 1
    Symbols visited: 6
    'X+....'
    
    >>> follow_trail('>+..+.', 0, 0, 0, 3, 2, 1,6)
    Treasures collected: 2
    Symbols visited: 6
    'X+..+.'
    
    >>> follow_trail('>>v..v', 0, 0, 0, 3, 2, 1, 6)
    Treasures collected: 0
    Symbols visited: 6
    'XXX..X'
    """
    a =0
    b=0
    treasure_collected_counter = 0
    symbols_visited_counter = 1
    previous_map_string = treasure_map
    
    while a <= nb_tiles and b < height:
        if a>(width*height):
            break
        if a-(width*b) > width:
                b+=1
        if previous_map_string[column_index+a-1] == utils.TREASURE_SYMBOL:
                treasure_collected_counter+=1
        if previous_map_string[column_index+a-(width*b)-1] == utils.MOVEMENT_SYMBOLS:
                symbols_visited_counter += 1
        
        if a == 0:
            new_map_string = utils.change_char_in_map(previous_map_string, starting_row+b, column_index+a-(width*b), utils.BREADCRUMB_SYMBOL, width, height)
            previous_map_string = new_map_string
            
        else:
            if previous_map_string[a-1] != utils.EMPTY_SYMBOL and previous_map_string[a-1] != utils.TREASURE_SYMBOL:
                new_map_string = utils.change_char_in_map(previous_map_string, starting_row+b, column_index+a-(width*b)-1, utils.BREADCRUMB_SYMBOL, width, height)
                previous_map_string = new_map_string
            symbols_visited_counter += 1
        
        a+=1
    
    print("Treasures collected:", treasure_collected_counter)
    print("Symbols visited:", symbols_visited_counter-1)
   
    return new_map_string 

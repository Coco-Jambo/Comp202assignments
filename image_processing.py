#Réda Alidrisi-Omari
#261068776

import doctest

def is_valid_image(nested_list):
    """(list<list>)->boolean
    Retrurns True if nested_list contains integers between 0 and 255 and if each list is of the same length
    Returns False otherwise.
    
    >>> is_valid_image([[1, 2, 3], [4, 5, 6], [7, 8]])
    False
    >>> is_valid_image([["111x7", "200x2", "0x5"], [4, 5, 6], [7, 8]])
    False
    >>> is_valid_image([[1, 2], [4, 5], [7, 8]])
    True
    """
    
    is_valid = True
    previous_elmnt = nested_list[0]
    
    for elmnt in nested_list:    
        if len(elmnt) == len(previous_elmnt):
            previous_elmnt = elmnt
            for sub_elmnt in elmnt:
                if type(sub_elmnt) != int:
                    is_valid = False
                    break
                elif(sub_elmnt < 0 or sub_elmnt > 255):
                    is_valid = False
                    break
        else:
            is_valid = False
            break
    
    return is_valid


def is_valid_compressed_image(nested_list):
    """(list<list>)->boolean
    Returns True if nested_list contains lists that contain strings of the format AxB where
    A and B are integers between 0 and 255 and the sum of B values in each list is the same in all
    other lists in nested_list. Returns False otherwise.
    
    >>> is_valid_compressed_image([["25555x5", "200x2"], ["111x7"]])
    False
    >>> is_valid_compressed_image([["25x5", "200x4"], ["111x7", "200x2"], ["111x9"]])
    True
    >>> is_valid_compressed_image([[1, 2, 3], [4, 5, 6], [2, 5, 18]])
    False
    """
    
    is_valid = True
    b_sum = 0
    previous_sum = 0
    for elmnt in nested_list:
        previous_b = 0
        for sub_elmnt in elmnt:
            if type(sub_elmnt) == str and ("x" in sub_elmnt) and sub_elmnt.count("x") == 1:
                x_index = 0
                while x_index < len(sub_elmnt):
                    if sub_elmnt[x_index] == "x":
                        break
                    else:
                        x_index +=1
                
                if sub_elmnt[:x_index].isdecimal() and sub_elmnt[x_index+1:].isdecimal():
                    a = int(sub_elmnt[:x_index])
                    b = int(sub_elmnt[x_index+1:])
                    
                    if (a < 0 or a > 255) or (b < 0 or b > 255):
                        is_valid=False
                        break 
                    else:
                        b_sum = previous_b +b
                        previous_b = b_sum
                else:
                    is_valid=False
                    break 
            else:
                is_valid=False
                break
       
        if previous_sum == 0:
            previous_sum = b_sum
        
        if previous_sum != b_sum:
            is_valid=False
            break

    return is_valid


def load_regular_image(file_name):
    """(str)->list<list>
    Returns a nested list using the image matrix contained in the PGM file with name file_name.
    Raises an AssertionError if the file does not contain a valid PGM image matrix.
    
    >>> load_regular_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> image_matrix = load_regular_image("comp.pgm")
    >>> 24 == len(image_matrix[0])
    True
    >>> 7 == len(image_matrix)
    True
    """
    
    image_matrix = []
    image = open(file_name, "r")
    image_content = image.read()
    image.close()
    
    if "P2" not in image_content:
        raise AssertionError("The image is not in PGM format, it should contain P2 in its first line.") 
    
    else:
        image = open(file_name, "r")
        for line in image:
            row = []
            string_row = line.split()
            for element in string_row:
                if element.isdecimal():
                    row.append(int(element))
            if not row == []:
                image_matrix.append(row)
        
        if len(image_matrix)>1:
            width = int(image_matrix[0][0])
            height = int(image_matrix[0][1])
            image_matrix = image_matrix[2:]
            image.close()
        else:
            raise AssertionError("The file does not contain compatible characters (integers) or is empty")
        
        for i in range(len(image_matrix)):
            if width != len(image_matrix[i]):
                raise AssertionError("The PGM image matrix does not have the width indicated in the file")
        
        if height != len(image_matrix):
            raise AssertionError("The PGM image matrix does not have the height indicated in the file")
        
        if is_valid_image(image_matrix) == False:
            raise AssertionError("The image is not a valid PGM image matrix") 
    
    return image_matrix 


def load_compressed_image(file_name):
    """(str)->list<list>
    Returns a nested list using the image matrix contained in the compressed PGM file with name file_name.
    Raises an AssertionError if the file does not contain a valid compressed PGM image matrix.
    
    >>> load_compressed_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    >>> image_matrix = load_compressed_image("comp.pgm.compressed")
    >>> 7 == len(image_matrix)
    True
    """
    
    image_matrix = []
    image = open(file_name, "r")
    image_content = image.read()
    image.close()
    
    if "P2C" not in image_content:
        raise AssertionError("The image is not in compressed PGM format, it should contain P2C in its first line.") 
    
    else:
        image = open(file_name, "r")
        b_sum = 0
        previous_sum = 0
        for line in image:
            row = []
            string_row = line.split()
            previous_b = 0
            for element in string_row:
                if element == "P2C":
                    continue
                if element.isdecimal():
                    row.append(element)
                    continue
                if "x" not in element:
                    raise AssertionError("The pixel is not in the format AxB, does not contain an x") 
                if element.count("x") > 1:
                    raise AssertionError("More than one x in a pixel")
                
                x_index =0
                while x_index < len(element):
                    if element[x_index] == "x":
                        break
                    else:
                        x_index +=1
                    
                if not element[:x_index].isdecimal():
                    raise AssertionError("The pixel is not in the format AxB, A should be an integer between 0 and 255") 
                if not element[x_index+1:].isdecimal():
                    raise AssertionError("The pixel is not in the format AxB, B should be an integer between 0 and 255") 

                a = int(element[:x_index])
                b = int(element[x_index+1:])
                    
                if a < 0 or a > 255:
                    raise AssertionError("In the format AxB, A should be between 0 and 255") 
                if b < 0 or b > 255:
                    raise AssertionError("In the format AxB, B should be between 0 and 255") 
                
                b_sum = previous_b +b
                previous_b = b_sum
                row.append(element)
                
            if previous_sum == 0:
                previous_sum = b_sum
    
            if previous_sum != b_sum:
                raise AssertionError("The sum of the B values in the format AxB of each row should be equal")
        
            image_matrix.append(row)
        
        image_matrix = image_matrix[1:]
     
        if len(image_matrix) >1:
            width = int(image_matrix[0][0])
            height = int(image_matrix[0][1])
            image_matrix = image_matrix[2:]
            image.close()
        else:
            raise AssertionError("The file does not contain compatible characters (integers) or is empty")

        if width != previous_sum:
            raise AssertionError("The PGM image matrix does not have the width indicated in the file")
        
        if height != len(image_matrix):
            raise AssertionError("The PGM image matrix does not have the height indicated in the file")
        
        if is_valid_compressed_image(image_matrix) == False:
            raise AssertionError("The image is not a valid compressed PGM image matrix") 
    
    return image_matrix 


def load_image(file_name):
    """(str)->list<list>
    Returns a nested list using the image matrix contained in either a PGM file
    or a compressed PGM file with name file_name, depending if the first line of the file is "P2" or "P2C".
    Raises an AssertionError if the file is not in PGM or compressed PGM format.
    
    >>> load_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]

    >>> load_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    >>> test_image = open("test.pgm", "w")
    >>> test_image.write("This is an invalid file")
    23
    >>> test_image.close()
    >>> load_image("test.pgm")
    Traceback (most recent call last):
    AssertionError: The image file should be in a PGM or compressed PGM format, the first line of the file should be P2 or P2C
    """
    
    image_matrix = []
    image = open(file_name, "r")
    image_content = image.read()
    lines_list = image_content.split("\n")
    
    if lines_list[0] == "P2":
        image_matrix = load_regular_image(file_name)
    elif lines_list[0] == "P2C":
        image_matrix = load_compressed_image(file_name)
    else:
        raise AssertionError("The image file should be in a PGM or compressed PGM format, the first line of the file should be P2 or P2C")
    
    image.close()
    return image_matrix
    
    
def save_regular_image(image_matrix, file_name):
    """(list<list>, String)->None
    Saves a PGM file of the name file_name containing image_matrix.
    Raises an AssertionError if the image matrix is invalid

    >>> save_regular_image([[0]*5, [2]*5, [0]*5], "test.pgm")
    >>> fobj = open("test.pgm", 'r')
    >>> fobj.read()
    'P2\\n5 3\\n255\\n0 0 0 0 0\\n2 2 2 2 2\\n0 0 0 0 0\\n'
    >>> fobj.close()
    >>> image = [[0]*5, [2]*5, [0]*5]
    >>> save_regular_image(image, "test.pgm")
    >>> image2 = load_image("test.pgm")
    >>> image == image2
    True
    """
    
    if is_valid_image(image_matrix) == False:
        raise AssertionError("The PGM image matrix provided is invalid")
    else:
        image = open(file_name, "w") 
        image.write("P2\n") 
        image.write(str(len(image_matrix[0])) + " " + str(len(image_matrix)) + "\n")
        image.write("255\n")
        for row in image_matrix:
            line = ""
            for element in row:
                line += (str(element) + " ")
            image.write(line.strip(" ") + "\n")
        image.close()
    
    
def save_compressed_image(image_matrix, file_name):
    """(list<list>, String)->None
    Saves a compressed PGM file of the name file_name containing image_matrix.
    Raises an AssertionError if the image matrix is invalid

    >>> save_compressed_image([["1x5", "20x4"], ["11x9"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n9 2\\n255\\n1x5 20x4\\n11x9\\n'
    >>> fobj.close()
    >>> image = [["1x5", "20x4"], ["11x9"]]
    >>> save_compressed_image(image, "test.pgm")
    >>> image2 = load_compressed_image("test.pgm")
    >>> image == image2
    True
    
    >>> save_compressed_image([[2, "200x2"], ["111x7"]], "test.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: Elements of the image matrix should all be strings of the format AxB
    """
    
    b_sum = 0
    previous_b=0
    for element in image_matrix[0]:
        if type(element) != str:
            raise AssertionError("Elements of the image matrix should all be strings of the format AxB") 
        if "x" not in element:
            raise AssertionError("The pixel is not in the format AxB, does not contain an x") 
        if element.count("x") > 1:
            raise AssertionError("More than one x in a pixel")
            
        x_index = 0
        while x_index < len(element):
            if element[x_index] == "x":
                break
            else:
                x_index +=1
        
        a = int(element[:x_index])
        b = int(element[x_index+1:])
        
        if a < 0 or a > 255:
            raise AssertionError("In the format AxB, A should be between 0 and 255") 
        if b < 0 or b > 255:
            raise AssertionError("In the format AxB, B should be between 0 and 255")
        
        b_sum = previous_b +b
        previous_b = b_sum
    
    if is_valid_compressed_image(image_matrix) == False:
        raise AssertionError("The compressed PGM image matrix provided is invalid")
    
    image = open(file_name, "w") 
    image.write("P2C\n")
    image.write(str(b_sum) + " " + str(len(image_matrix)) + "\n")
    image.write("255\n")
    for row in image_matrix:
        line = ""
        for element in row:
            line += (str(element) + " ")
        image.write(line.strip(" ") + "\n")
    image.close()
    
    
def save_image(image_matrix, file_name):
    """(list<list>, String)->None
    Saves a file of the name file_name containing image_matrix.
    The file's format can be either a compressed PGM file or a PGM file,
    depending if the first sub element is an integer or a string.
    Raises an AssertionError if the file saved is not in PGM or compressed PGM format.
    
    >>> save_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    
    >>> save_image([[1]*5, [14]*5, [255]*5], "test.pgm")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> fobj.close()
    
    >>> save_image([["0xx5", "200x2"], ["111x7"]], "test.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: More than one x in a pixel
    """
    
    if type(image_matrix[0][0]) == int:
        save_regular_image(image_matrix, file_name)
    elif type(image_matrix[0][0]) == str:
        save_compressed_image(image_matrix, file_name)
    else:
        raise AssertionError("The file should be saved in either PGM or compressed PGM format")
    
    
def invert(image_matrix):
    """(list<list>)->list<list>
    Returns a new nested list which inverts all the subelements of image_matrix.
    Raises an AssertionError if image_matrix is not a valid PGM image matrix.
    
    >>> image = [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    >>> invert(image)
    [[255, 155, 105], [55, 55, 55], [0, 0, 0]]
    >>> image == [[0, 100, 150], [200, 200, 200], [255, 255, 255]]
    True
    
    >>> invert([[45, 78, 255], [210, 20, 2], [25, 255, 2]])
    [[210, 177, 0], [45, 235, 253], [230, 0, 253]]

    >>> invert([[45, 78, 255], [210, 20, 2], [25, 255, "255x3"]])
    Traceback (most recent call last):
    AssertionError: The PGM image matrix provided is invalid
    """
    
    inverted_matrix = []
    if is_valid_image(image_matrix) == False:
        raise AssertionError("The PGM image matrix provided is invalid")
    else:
        for element in image_matrix:
            row = []
            for subelement in element:
                row.append(255 - subelement)
            inverted_matrix.append(row)
            
    return inverted_matrix


def flip_horizontal(image_matrix):
    """(list<list>)->list<list>
    Returns a new nested list which reverses the order of the subelements of each element of image_matrix.
    Raises an AssertionError if image_matrix is not a valid PGM image matrix.

    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_horizontal(image)
    [[5, 4, 3, 2, 1], [10, 10, 5, 0, 0], [5, 5, 5, 5, 5]]
    >>> image == [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    True
    
    >>> flip_horizontal([[100, 200, 255, 200, 100], [255, 255, 0, 10, 10], [1, 2, 3, 4, 5]])
    [[100, 200, 255, 200, 100], [10, 10, 0, 255, 255], [5, 4, 3, 2, 1]]
    
    >>> flip_horizontal([[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5]])
    Traceback (most recent call last):
    AssertionError: The PGM image matrix provided is invalid
    """
    
    horizontally_flipped_matrix = []
    if is_valid_image(image_matrix) == False:
        raise AssertionError("The PGM image matrix provided is invalid")
    else:
        for element in image_matrix:
            horizontally_flipped_matrix.append(element[::-1])
            
    return horizontally_flipped_matrix
        
        
def flip_vertical(image_matrix):
    """(list<list>)->list<list>
    Returns a new nested list which reverses the order of the elements of image_matrix.
    Raises an AssertionError if image_matrix is not a valid PGM image matrix.

    >>> image = [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    >>> flip_vertical(image)
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 3, 4, 5]]
    >>> image == [[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]]
    True
    
    >>> flip_vertical([[100, 200, 255, 200, 100], [255, 255, 0, 10, 10], [1, 2, 3, 4,5]])
    [[1, 2, 3, 4, 5], [255, 255, 0, 10, 10], [100, 200, 255, 200, 100]]
    
    >>> flip_vertical([[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5]])
    Traceback (most recent call last):
    AssertionError: The PGM image matrix provided is invalid
    """
    
    vertically_flipped_matrix = []
    if is_valid_image(image_matrix) == False:
        raise AssertionError("The PGM image matrix provided is invalid")
    else:
        vertically_flipped_matrix = image_matrix[::-1]
            
    return vertically_flipped_matrix
    

def crop(image_matrix, first_row, first_col, nb_rows, nb_col):
    """(list<list>, int, int, int, int)->list<list>
    Returns a nested list that is a cropped version of image_matrix, where first_row represents the first row of the cropped image matrix,
    first_col the first column of the cropped image matrix, nb_rows the number of rows the image matrix has and
    nb_col the number of columns the image matrix has. Raises an AssertionError if image_matrix is not a valid PGM image matrix.
    
    >>> crop([[5, 5, 5], [5, 6, 6], [6, 6, 7]], 1, 1, 2, 2)
    [[6, 6], [6, 7]]
    
    >>> crop([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]], 0, 2, 2, 1)
    [[3], [6]]
    
    >>> crop([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]], 0, 0, 3, 1)
    [[1], [4], [8]]
    """
    
    cropped_image_matrix = []
    if is_valid_image(image_matrix) == False:
        raise AssertionError("The PGM image matrix provided is invalid")
    else:
        if first_row == 0:
            i=0
            while i <(len(image_matrix)):
                if i >= first_row and i < nb_rows:
                    cropped_row = []
                    for j in range (len(image_matrix[i])):
                        if j >= first_col and len(cropped_row) < nb_col:
                            cropped_row.append(image_matrix[i][j])
                    cropped_image_matrix.append(cropped_row)
                i+=1
        else:
            i=0
            while i <(len(image_matrix)):
                if first_row == 0:
                    nb_rows-=1
                if i >= first_row and i <= nb_rows:
                    cropped_row = []
                    for j in range (len(image_matrix[i])):
                        if j >= first_col and len(cropped_row) < nb_col:
                            cropped_row.append(image_matrix[i][j])
                    cropped_image_matrix.append(cropped_row)
                i+=1
    
    return cropped_image_matrix


def find_end_of_repetition(int_list, index, target_number):
    """(list<int>, int, int)->int
    Returns the last consecutive occurence of target_number starting from index in int_list.

    >>> find_end_of_repetition([5, 3, 5, 5, 5, -1, 0], 2, 5)
    4
    >>> find_end_of_repetition([6, 2, 3, 4, 5, 6, 7], 0, 6)
    0
    >>> find_end_of_repetition([6, 6, 3, 4, 5, 6, 7], 0, 6)
    1
    """
    
    last_index = 0
    for i in range(index, len(int_list)):
        if int_list[i] == target_number:
            last_index = i
        else:
            break
    
    return last_index
    
    
def compress(image_matrix):
    """(list<list>)->list<list>
    Returns a compressed version of image_matrix in the form AxB where A is the integer and B is the number of consecutive
    times it is listed. Raises an AssertionError if image_matrix is an invalid PGM image matrix.

    >>> compress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    [['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]
    
    >>> compress([[11, 11, 11, 11, 11], [1, 2, 3, 4, 5], [255, 255, 255, 0, 255]])
    [['11x5'], ['1x1', '2x1', '3x1', '4x1', '5x1'], ['255x3', '0x1', '255x1']]
    
    >>> compress([[11, 11, 255, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    [['11x2', '255x1', '11x2'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]
    
    >>> compress([[11, 11, 255, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 256]])
    Traceback (most recent call last):
    AssertionError: The PGM image matrix provided is invalid
    """
    
    if is_valid_image(image_matrix) == False:
        raise AssertionError("The PGM image matrix provided is invalid")
    else:
        compressed_image_matrix = []
        for row in image_matrix:
            compressed_row = []
            previous_number = -1
            for number in row:
                if previous_number == number:
                    continue
                else:
                    if row.index(number) != 0:
                        row = row[row.index(number):]
                    
                    last_index = find_end_of_repetition(row, row.index(number), number)
                    compressed_row.append(str(row[last_index]) + "x" + str(last_index+1))
                    previous_number = number
                    
            compressed_image_matrix.append(compressed_row)
    
    return compressed_image_matrix


def decompress(image_matrix):
    """(list<list>)->list<list>
    Returns a decompressed version of image_matrix where A is listed B times inside an element of the new image matrix.
    Raises an AssertionError if image_matrix is an invalid compressed PGM image matrix.

    >>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    >>> image = [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    >>> compressed_image = compress(image)
    >>> image2 = decompress(compressed_image)
    >>> image == image2
    True
    
    >>> decompress([['11x2', '255x1', '11x2'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 255, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]

    >>> decompress([['11x5'], ['1x1', '2x1', '3x1', '4x1', '5x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 2, 3, 4, 5], [255, 255, 255, 0, 255]]
    """
    
    if is_valid_compressed_image(image_matrix) == False:
        raise AssertionError("The compressed PGM image matrix provided is invalid")
    else:
        decompressed_image_matrix = []
        for row in image_matrix:
            decompressed_row = []
            for element in row:
                x_index =0
                while x_index < len(element):
                    if element[x_index] == "x":
                        break
                    else:
                        x_index +=1
                    
                a = int(element[:x_index])
                b = int(element[x_index+1:])
                for i in range(b):
                    decompressed_row.append(a)
            decompressed_image_matrix.append(decompressed_row)
    
    return decompressed_image_matrix
    

def process_command(inputs):
    """(string)->None
    Executes each command present in inputs in turn, where inputs always starts with the LOAD command in the form LOAD<x.pgm> or LOAD<x.pgm.compressed>,
    ends with the SAVE command in the form SAVE<x.pgm> or SAVE<x.pgm.compressed>, and the commands in between are space-separated.
    Raises an AssertionError if the commands in inputs are not either 'LOAD', 'SAVE', 'INV', 'FH', 'FV', 'CR', 'CP'or 'DC'.
    
    >>> process_command("LOAD<comp.pgm> CP DC INV SAVE<comp2.pgm>")
    >>> load_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> load_image("comp2.pgm")
    [[255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 204, 204, 204, 204, 204, 255, 136, 136, 136, 136, 136, 255, 68, 68, 68, 68, 68, 255, 0, 0, 0, 0, 255], [255, 204, 255, 255, 255, 255, 255, 136, 255, 255, 255, 136, 255, 68, 255, 68, 255, 68, 255, 0, 255, 255, 0, 255], [255, 204, 255, 255, 255, 255, 255, 136, 255, 255, 255, 136, 255, 68, 255, 68, 255, 68, 255, 0, 0, 0, 0, 255], [255, 204, 255, 255, 255, 255, 255, 136, 255, 255, 255, 136, 255, 68, 255, 68, 255, 68, 255, 0, 255, 255, 255, 255], [255, 204, 204, 204, 204, 204, 255, 136, 136, 136, 136, 136, 255, 68, 255, 68, 255, 68, 255, 0, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]]
    
    >>> process_command("LOAD<comp.pgm> CP SAVE<comp.pgm.compressed>")
    >>> load_compressed_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    
    >>> process_command("LOAD<comp.pgm> CR<1,1,2,2> SAVE<comp2.pgm>")
    >>> load_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> load_image("comp2.pgm")
    [[51, 51], [51, 0]]

    >>> process_command("LOAD<comp.pgm> STOP DO NOT DO ANYTHING!!!<comp2.pgm>")
    Traceback (most recent call last):
    AssertionError: The command string contains unrecognized characters
    """
    
    command_list = inputs.split()
    for command in command_list:
        if "LOAD" in command:
            file_name = command[4:].strip("<>")
            image_matrix = load_image(file_name)
        elif "INV" in command:
            image_matrix = invert(image_matrix)
        elif "FH" in command:
            image_matrix = flip_horizontal(image_matrix)
        elif "FV" in command:
            image_matrix = flip_vertical(image_matrix)
        elif "CR" in command:
            numbers = command.strip("CR<>").split(",")
            frist_row = int(numbers[0])
            first_col = int(numbers[1])
            nb_row = int(numbers[2])
            nb_col = int(numbers[3])
            image_matrix = crop(image_matrix, frist_row, first_col, nb_row, nb_col)
        elif "CP" in command:
            image_matrix = compress(image_matrix)
        elif "DC" in command:
            image_matrix = decompress(image_matrix)
        elif "SAVE" in command:
            file_name = command[4:].strip("<>")
            save_image(image_matrix, file_name)
        else:
            raise AssertionError("The command string contains unrecognized characters")
    
if __name__ == "__main__":
    doctest.testmod()
    
    
    
    
    
    
    
    





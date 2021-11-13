"""Generates random 9 character long strings and validates if the Matrix representation
   could be a valid Hill Cipher key
"""

import numpy as np
import random as rd

def main():
    f = open('keys.txt', 'w')
    valid_keys = set()
    while True:
        key_string_normal = ''
        for i in range(9):
            key_string_normal += chr(rd.randint(65,90))
        if key_string_normal in valid_keys:
            print('----DUPLICATE FOUND----')
            continue
        
        temp_matrix_normal = key_to_matrix(key_string_normal)
        if check_determinant(temp_matrix_normal):
            print(f'Valid KEY {key_string_normal}')
            valid_keys.update(key_string_normal)
            f.write(key_string_normal+'\n')
        else:
            print(f'Invalid KEY {key_string_normal}')




def check_determinant(key):
    """Function tacken from Dhruv Manilawala.
       Checks to see that the greatest common divisor between the determinant of the 
       key and 256 is equal to 1. If the GCD between the numbers is not 1, this throws an error
       since the key is unusable.
       
       Parameters:
       key -- a 3x3 matrix that is the encryption key for this algorithm
    """
    det = round(np.linalg.det(key))

    if det < 0:
        det = det % 256
    return (greatest_common_divisor(det, 256) == 1)

def greatest_common_divisor(a: int, b: int) -> int:
    """Function tacken from Dhruv Manilawala.
       This function finds the greatest common divisor between two integers

       Parameters:
       a -- an integer
       b -- an integer

       Return:
       the greatest common divisor between a and b
    """
    return b if a == 0 else greatest_common_divisor(b % a, a)

def key_to_matrix(s):
    """Takes a string of length 9 or greater and converts it to a 3x3 matrix or ASCII values.
       If the length of the string is less than 9, throws an error.
       If the length of the string is greater than or equal to 9, use the first 9 characters

       Parameters:
       s -- a String of length 9 or greater

       Return:
       the 3x3 matrix of ASCII values based on the parameter s
    """
    if(len(s) < 9):
        raise ValueError(f'Invalid KEY string , it must be exactly 9 characters')
    elif(len(s) > 9):
        print(f'KEY string is too long, taking the first 9 characters and chopping the rest')
    # first row
    a_0_0 = ord(s[0]) # ord() converts a character to an ASCII value
    a_0_1 = ord(s[1])
    a_0_2 = ord(s[2])
    # second row
    a_1_0 = ord(s[3])
    a_1_1 = ord(s[4])
    a_1_2 = ord(s[5])
    # third row
    a_2_0 = ord(s[6])
    a_2_1 = ord(s[7])
    a_2_2 = ord(s[8])

    return np.array([
                    [a_0_0, a_0_1, a_0_2], 
                    [a_1_0, a_1_1, a_1_2],
                    [a_2_0, a_2_1, a_2_2]])

if __name__ == "__main__":
    main()
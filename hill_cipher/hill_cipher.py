"""Some code was taken from Dhruv Manilawala, username dhruvmanila, on Github
   Anytime this code mentions that code was taken from him, it refers to this Github repository
   Repository: https://github.com/TheAlgorithms/Python/blob/master/ciphers/hill_cipher.py

   This code encrypts and decrypts text based on the Hill Cipher Algorithm
"""

import numpy as np

key_string = 'YNNRJQAKE'
message = "Nolan Winsman Example Text"
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','K','R','S','T','U','V','W','X','Y','Z'] # not used

# lambda function taken from Dhruv Manilawala
# it rounds all the values to an integer to remove any decimals
to_int = np.vectorize(lambda x: round(x)) 

def encrypt(key, vectors):
    """Encrypts a list of 3x1 vectors using the Hill Cipher Algorithm.
       Each vector is multiplied by the encryption key.
       Then, the result is modded by 256.
       256 being the number of ASCII characters.
       
       Parameters:
       key -- a 3x3 matrix that is the encryption key for this algorithm
       vectors -- a list of 3x1 matricies
       
       Return:
       a list of vectors encrypted based on the parameters
       Each number inside the vectors is an ASCII code.
       Since these vectors are encrypted, it's essentially garbage data without the decryption.
    """
    encypted_vectors = []
    for v in vectors:
        temp = np.matmul(key, v) # multiply the key to the 3x1 matrix
        temp = np.mod(temp, 256) # mods the entire vector by 256
        encypted_vectors.append(temp) # adds encrypted vector to list
    
    return encypted_vectors

def decrypt(key, vectors):
    """Decrypts a list of 3x1 vectors using the Hill Cipher Algorithm.
       Each vector is multiplied by the decryption key.
       Then, the result is modded by 256.
       256 being the number of ASCII characters.
       
       Parameters:
       key -- a 3x3 matrix that is the decryption key for this algorithm
       vectors -- a list of 3x1 matricies that should be encrpyted by the encrypt() function
       
       Return:
       a list of vectors decrypted based on the parameters.
       Each number inside the vectors is an ASCII code
    """
    decrypted_vectors = [] # list that will hold the decrypted vectors
    for v in vectors:
        temp = np.matmul(key, v) # multiply the key to the 3x1 matrix
        temp = np.mod(temp, 256) # mods the entire vector by 256
        decrypted_vectors.append(temp) # adds decrypted vector to list
    
    return decrypted_vectors

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

def check_determinant(key) -> None:
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

    req_l = 256
    if greatest_common_divisor(det, 256) != 1:
        # incompatable key, throws an error
        raise ValueError(
            f"determinant modular {req_l} of encryption key({det}) is not co prime "
            f"w.r.t {req_l}.\nTry another key."
        )

def make_decrypt_key(key):
    """Function is heavily inspired from Dhruv Manilawala.
       This function calculates the inverse of a 3x3 matrix

       Parameters:
       key -- 3x3 matrix that's inverse is calculated in this function

       Return:
       the inverse of parameter key
    """
    det = round(np.linalg.det(key))
    if det < 0:
        det = det % 256
    det_inv = None
    for i in range(256):
        if (det * i) % 256 == 1:
            det_inv = i
            break
    inv_key = (
        det_inv
        * np.linalg.det(key)
        * np.linalg.inv(key)
    )
    return to_int(np.mod(inv_key, 256))

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
        raise ValueError(f'Invalid KEY string {key_string}, it must be exactly 9 characters')
    elif(len(s) > 9):
        print(f'KEY string {key_string} is too long, taking the first 9 characters and chopping the rest')
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

def message_to_vectors(s):
    """Takes a string and converts the characters to a bunch of 3x1 matricies.
       If the length of the string is not divisible by 3, it adds '!' to the string until it is.
       
       An example would be the string NOLAN converts to:
       | N | | A |          | 78 | | 65 |
       | O | | N |  ------> | 79 | | 78 |
       | L | | ! |          | 76 | | 33 |
       Two 3x1 matricies holding ASCII values of the string "NOLAN"

       Parameters:
       s -- a string of any length

       Return:
       a list of 3x1 matricies holding the ASCII values for the parameter
    """
    vectors = []
    # this loop adds ! to the string s until s is divisible by 3 so that it can evenly split into 3x1 vectors
    while len(s) % 3 != 0:
        s += '!'
    while len(s) >= 3: # while the string has at least 3 characters
        a_0 = ord(s[0])
        a_1 = ord(s[1])
        a_2 = ord(s[2])

        a = np.array([[a_0], [a_1], [a_2]])
        
        vectors.append(a)
        s = s[3:] # cuts off the first 3 characters of s

    return vectors

def print_matrix(A):
    """This function was taken from an Anonymous user on Stack Overflow linked below.
       https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python

       Prints a 3x3 matrix in a more legible manner

       Parameters:
       A -- a 3x3 matrix
    """
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in A]))

def print_vectors(vectors, dimension):
    """Prints a list of vectors in a more legible manner.
       All the vectors must be of the same dimension
       
       Parameters:
       vectors -- a list of vectors that must all have the same dimension
       dimension -- the dimension of all the vectors
    """
    print('--------------------')
    for i in range(dimension):
        for v in vectors:
            value = v[i][0]
            print(f'{value}\t', end='')
        print('')
    print('--------------------')

def vectors_to_string(vectors, dimension):
    """Converts the ASCII values inside the vectors to a string
       
       An example would be the vectors below convert to:
       | 78 | | 65 |
       | 79 | | 78 | ------> "NOLAN!"
       | 76 | | 33 |
       
       Parameters:
       vectors -- a list of vectors that must all have the same dimension
       dimension -- the dimension of all the vectors

       Return:
       returns a string based on the ASCII values inside the vectors
    """
    s = ''
    for v in vectors:
        for i in range(dimension):
            s += chr(v[i][0])
    return s

def main():
    print('-----HILL CIPHER ALGORITHM-----')
    print(f'key "{key_string}" Converts to matrix:')
    key = key_to_matrix(key_string)
    check_determinant(key)
    print_matrix(key)
    print(f'Message "{message}" converts to vectors:')
    code = message_to_vectors(message)
    print_vectors(code, 3)
    encrypted_vectors = encrypt(key, code)
    print(f'Encrypted message "{message}" converts to vectors:')
    print_vectors(encrypted_vectors, 3)
    print(f'Encrypted message "{message}" converts to vectors with text:')
    encrypted_text = vectors_to_string(encrypted_vectors, 3)
    print(f'Encrypted message converts to the text: "{encrypted_text}"')
    encrypted_vectors = message_to_vectors(encrypted_text) # technically redundant
    decryption_key = make_decrypt_key(key) # this gets the inverse of key
    print(f'key "{key_string}" Converts to matrix:')
    print_matrix(decryption_key)
    decrypted_vectors = decrypt(decryption_key, encrypted_vectors)
    print(f'Message "{encrypted_text}" decrypts to vectors:')
    print_vectors(decrypted_vectors, 3)
    print(f'Decrypted message of "{encrypted_text}" is:')
    decrypted_text = vectors_to_string(decrypted_vectors, 3)
    print(f'Decrypted message is: "{decrypted_text}"')



if __name__ == "__main__":
    main()
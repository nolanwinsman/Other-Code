import numpy as np

key_string = 'GYBNQKURP' # any 9 letter string
message = "Nolan Winsman Example Text"

def main():
    print(f'key "{key_string}" Converts to matrix:')
    key = key_to_matrix(key_string)[0]
    print_matrix(key)
    print(f'Message "{message}" converts to vectors:')
    code = message_to_vectors(message)
    print_vectors(code, 3)
    test = np.mod(code[0], 256)
    test = encrypt(key, code)
    print(f'Encrypted message "{message}" converts to vectors:')
    print_vectors(test, 3)
    print(f'Encrypted message "{message}" converts to vectors with text:')
    print_vectors_to_string(test, 3)
    encrypted_text = vectors_to_string(test, 3)
    print(f'Encrypted message converts to the text: "{encrypted_text}"')



def encrypt(key, vectors):
    encypted_vectors = []
    for v in vectors:
        temp = np.matmul(key, v)
        temp = np.mod(temp, 256)
        encypted_vectors.append(temp)
    
    return encypted_vectors



def key_to_matrix(s):
    s
    matricies = []
    while len(s) > 8: # while the string has at least 9 characters
        # first row
        a_0_0 = ord(s[0])
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

        a = np.array([
                    [a_0_0, a_0_1, a_0_2], 
                    [a_1_0, a_1_1, a_1_2],
                    [a_2_0, a_2_1, a_2_2]])
        
        matricies.append(a)
        s = s[9:-1] # cuts off the first 9 characters of s
    return matricies

def message_to_vectors(s):
    s
    vectors = []
    while len(s) >= 3: # while the string has at least 9 characters
        a_0 = ord(s[0])
        a_1 = ord(s[1])
        a_2 = ord(s[2])

        a = np.array([[a_0], [a_1], [a_2]])
        
        vectors.append(a)
        s = s[3:-1] # cuts off the first 3 characters of s


    return vectors

def print_matrix(A):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in A]))

def print_vectors(vectors, dimension):
    print('--------------------')
    for i in range(dimension):
        for v in vectors:
            value = v[i][0]
            print(f'{value}\t', end='')
        print('')
    print('--------------------')

def print_vectors_to_string(vectors, dimension):
    print('--------------------')
    for i in range(dimension):
        for v in vectors:
            letter = chr(v[i][0])
            print(f'{letter}\t', end='')
        print('')
    print('--------------------')

def vectors_to_string(vectors, dimension):
    s = ''
    for v in vectors:
        for i in range(dimension):
            s += chr(v[i][0])
    return s


if __name__ == "__main__":
    main()
#write a input function that will converts string to hexadecimal numbers.

# text= input("Enter plain text: ")
from BitVector import BitVector
import numpy as np
import time

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

def process_text(text, chunk_size):
    if len(text) == chunk_size:
        return [text]
    elif len(text) < chunk_size:
        padding = chunk_size - len(text)
        padded_text = text + ' ' * padding
        return [padded_text]
    else:
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        chunks[-1] = process_text(chunks[-1], chunk_size)
        return chunks

def process_key(key, chunk_size):
    if len(key) == chunk_size:
        # Key size is already 128 bits
        return key
    elif len(key) < chunk_size:
        # Pad the key to 128 bits
        padding = chunk_size - len(key)
        padded_key = key + '0' * padding
        return padded_key
    else:
        # tranck the key into 128-bit blocks
        key= key[:chunk_size]
        return key
        

def string_to_hex_array(input_string):
    input_string = ''.join(input_string)
    hex_array = []
    for char in input_string:
        hex_value = hex(ord(char))[2:].upper()  # Convert character to hexadecimal and remove the '0x' prefix
        hex_array.append(hex_value)
    return hex_array


def string_to_hex_matrix(input_string, cols, rows):
    hex_matrix =  [[0 for i in range(cols)] for j in range(rows)]
    hex_array = string_to_hex_array(input_string)


    for i in range(4):
        for j in range(4):
            hex_matrix[i][j] = (hex_array[i * 4 + j])
    return hex_matrix



# round constants in hex
round_constants = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

#function of key expansion
def key_expansion(key_matrix):
    for i in range(4, 44):
        if i % 4 == 0:
            rc= [round_constants[(int)(i/4) -1],0,0,0]
            temp = key_matrix[i - 1]
            temp =  temp[1:] + temp[:1]
            for j in range(4):
                b = BitVector(hexstring=temp[j])
                int_val = b.intValue()
                s = Sbox[int_val]
                s = BitVector(intVal=s, size=8).getHexStringFromBitVector().upper()
                temp[j] = s
            temp= [hex(int(x, 16) ^ y)[2:].upper() for x, y in zip(temp, rc)]
            temp = [hex(int(x, 16) ^ int(y, 16))[2:].upper() for x, y in zip(key_matrix[i-4], temp)]
           # temp = [x ^ y for x, y in zip(hex(key_matrix[i-4]), hex(temp))]
            key_matrix[i]= temp
        else:
           temp = [hex(int(x, 16) ^ int(y, 16))[2:].upper() for x, y in zip(key_matrix[i-1], key_matrix[i-4])]
           key_matrix[i] = temp
    return key_matrix

# function of add round key
def add_round_key(plain_text, round_key):
    for i in range(4):
        for j in range(4):
            plain_text[i][j] = hex(int(plain_text[i][j], 16) ^ int(round_key[i][j], 16))[2:].upper()
    return plain_text

#function of sub bytes
def sub_bytes(plain_text):
    for i in range(4):
        for j in range(4):
            b = BitVector(hexstring=plain_text[i][j])
            int_val = b.intValue()
            s = Sbox[int_val]
            s = BitVector(intVal=s, size=8).getHexStringFromBitVector().upper()
            plain_text[i][j] = s
    return plain_text

#function of shift rows
def circular_left_shift_matrix(matrix):
    shifted_matrix = np.empty_like(matrix)
    
    for i, row in enumerate(matrix):
        shift = i
        shifted_row = np.roll(row, -shift)
        shifted_matrix[i] = shifted_row
    
    return shifted_matrix

#function of mix columns
def mix_columns(plain_text):
    AES_modulus = BitVector(bitstring='100011011')
    mix_columns= np.empty_like(plain_text)
    for i in range(4):
        for j in range(4):
            bv = BitVector(intVal=0, size=8)
            for k in range(4):
                bv = bv ^  (Mixer[i][k].gf_multiply_modular(BitVector(intVal=int(plain_text[k][j], 16), size=8), AES_modulus, 8))
            mix_columns[i][j] = bv.getHexStringFromBitVector().upper()    
    return mix_columns

def encryption(plain_text, key_matrix):
    plain_text= np.array(plain_text)
    plain_text = plain_text.transpose()
    for i in range(10):
        round_key = np.array(key_matrix[i * 4:(i + 1) * 4])
        round_key = round_key.transpose()
        plain_text = add_round_key(plain_text, round_key)
        # print("Round after add round key ", i, " is: ", plain_text)
        plain_text = sub_bytes(plain_text)
        # print("Round after add sub bytes", i, " is: ", plain_text)
        plain_text = circular_left_shift_matrix(plain_text)
        # print("Round after add shift rows", i, " is: ", plain_text)
        if i != 9:
            plain_text = mix_columns(plain_text)
            # print("Round after add mix columns", i, " is: ", plain_text)
    round_key= np.array(key_matrix[40:44])
    round_key= round_key.transpose()
    plain_text = add_round_key(plain_text, round_key)
    return plain_text


#function of inverse shift rows
def circular_right_shift_matrix(matrix):
    shifted_matrix = np.empty_like(matrix)
    
    for i, row in enumerate(matrix):
        shift = i
        shifted_row = np.roll(row, shift)
        shifted_matrix[i] = shifted_row
    
    return shifted_matrix

#function of inverse sub bytes
def inverse_sub_bytes(cipher_text):
    for i in range(4):
        for j in range(4):
            b = BitVector(hexstring=cipher_text[i][j])
            int_val = b.intValue()
            s = InvSbox[int_val]
            s = BitVector(intVal=s, size=8).getHexStringFromBitVector().upper()
            cipher_text[i][j] = s
    return cipher_text

#function of inverse mix columns
def inverse_mix_columns(cipher_text):
    AES_modulus = BitVector(bitstring='100011011')
    mix_columns= np.empty_like(cipher_text)
    for i in range(4):
        for j in range(4):
            bv = BitVector(intVal=0, size=8)
            for k in range(4):
                bv = bv ^  (InvMixer[i][k].gf_multiply_modular(BitVector(intVal=int(cipher_text[k][j], 16), size=8), AES_modulus, 8))
            mix_columns[i][j] = bv.getHexStringFromBitVector().upper()    
    return mix_columns

def decryption(cipher_text, key_matrix):
    cipher_text= np.array(cipher_text)
    cipher_text = cipher_text.transpose()
    round_key= np.array(key_matrix[40:44])
    round_key= round_key.transpose()
    cipher_text= add_round_key(cipher_text, round_key)
    for i in range(10):
        cipher_text = circular_right_shift_matrix(cipher_text)
        cipher_text = inverse_sub_bytes(cipher_text)
        round_key = np.array(key_matrix[36 - i * 4:40 - i * 4])
        round_key = round_key.transpose()
        cipher_text = add_round_key(cipher_text, round_key)
        if i != 9:
            cipher_text = inverse_mix_columns(cipher_text)
    return cipher_text



#input text and key

text= "Can They Do This to us?"


# print("Plain Text:")
# print("In ASCII: ", text)
# print("In HEX: ", end=" ")
# hex_arr= string_to_hex_array(text)
# for i in hex_arr:
#     print(i, end="")
# print("\n\n")

key= "BUET CSE18 Batch sjdas 1232 eweoiwneion #$"


# key= process_key(key, 16)
# print("\n\nKey:")
# print("In ASCII: ", key)
# print("In HEX: ", end=" ")
# hex_arr= string_to_hex_array(key)
# for i in hex_arr:
#     print(i, end="")
# print("\n\n")


sum_time_decryption = 0
decrypted= []
decrypted_hex= []

def cipher_text(plain_text, key_matrix):
    encrypted= []
    encrypted_hex= []
    sum_time_encryption = 0
    text_chunks= []
    text_chunks= process_text(plain_text, 16)
    key= process_key(key_matrix, 16)
    hex_key= string_to_hex_matrix(key, 4, 44)
    start_time_key = time.time()
    key_expansion(hex_key)
    end_time_key = time.time()
    for i in range(len(text_chunks)):
        hex_text = string_to_hex_matrix(text_chunks[i], 4, 4)
        
        start_time_encryption = time.time()
        encrypted_text= encryption(hex_text, hex_key)
        end_time_encryption = time.time()
        sum_time_encryption += (end_time_encryption - start_time_encryption)

        # print the encrypted text in column major order and every element should be of length 2 if not then add 0 in front of it
        new_encrypted= encrypted_text.transpose()
        new_encrypted= new_encrypted.flatten()
        new_encrypted= [x.zfill(2) for x in new_encrypted]
        new_encrypted= ''.join(new_encrypted)
        encrypted_hex.append(new_encrypted)
        # get the ascii value of the encrypted text which is in hex and print it
        encrypted_ascii= [chr(int(new_encrypted[i:i+2], 16)) for i in range(0, len(new_encrypted), 2)]
        encrypted= encrypted + encrypted_ascii
    encrypted= ''.join(encrypted)
    encrypted_hex= ''.join(encrypted_hex)
    return encrypted, encrypted_hex, sum_time_encryption

def decrypt_text(encrypted_text, key_matrix):
    decrypted= []
    decrypted_hex= []
    sum_time_decryption = 0
    text_chunks= []
    text_chunks= process_text(encrypted_text, 32)
    key= process_key(key_matrix, 16)
    hex_key= string_to_hex_matrix(key, 4, 44)
    start_time_key = time.time()
    key_expansion(hex_key)
    end_time_key = time.time()
    for i in range(len(text_chunks)):
        input_string = ''.join(text_chunks[i])
        chunks = [input_string[i:i+2] for i in range(0, len(input_string), 2)]
        hex_text = np.array(chunks).reshape(4, 4)
        
        start_time_decryption = time.time()
        decrypted_text= decryption(hex_text, hex_key)
        end_time_decryption = time.time()
        sum_time_decryption += (end_time_decryption - start_time_decryption)

        # print the encrypted text in column major order and every element should be of length 2 if not then add 0 in front of it
        new_decrypted= decrypted_text.transpose()
        new_decrypted= new_decrypted.flatten()
        new_decrypted= [x.zfill(2) for x in new_decrypted]
        new_decrypted= ''.join(new_decrypted)
        decrypted_hex.append(new_decrypted)
        # get the ascii value of the encrypted text which is in hex and print it
        decrypted_ascii= [chr(int(new_decrypted[i:i+2], 16)) for i in range(0, len(new_decrypted), 2)]
        decrypted= decrypted + decrypted_ascii
    decrypted= ''.join(decrypted)
    decrypted= decrypted.rstrip()
    decrypted_hex= ''.join(decrypted_hex)
    return decrypted, decrypted_hex, sum_time_decryption

[encrypted, encrypted_hex, sum_time_encryption] = cipher_text(text, key)
print("\n\nCipher Text:")
print("In HEX: ", encrypted_hex)
print("In ASCII: ", encrypted)


[decrypted, decrypted_hex, sum_time_decryption] = decrypt_text(encrypted_hex, key)
print("\n\nDeciphered Text:")
print("In HEX: ", decrypted_hex)
print("In ASCII: ", decrypted)

key= process_key(key, 16)
hex_key= string_to_hex_matrix(key, 4, 44)
start_time_key = time.time()
key_expansion(hex_key)
end_time_key = time.time()

# print("\n\nExecution time details:")
# print("Key Scheduling : ", end_time_key - start_time_key, " seconds")
# print("Encryption Time : ", sum_time_encryption, " seconds")
# print("Decryption Time : ", sum_time_decryption, " seconds")






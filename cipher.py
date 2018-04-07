import sys
from DES import DES_Cipher
from AES import AES_Cipher

# to run:
# python cipher.py <cipher name> < key > <enc/dec> <inputFile> <outputFile>
def main():
    cipher_name = sys.argv[1] # cipher name
    key = sys.argv[2] # key
    mode = sys.argv[3] # enc/dec
    input_file = sys.argv[4] # input file
    output_file = sys.argv[5] # output file

    if cipher_name == 'DES':
        desCipher = DES_Cipher()
        desCipher.set_key(key)
        if mode == 'ENC':
            # open the files
            inputFile = open(input_file, 'r')
            outputFile = open(output_file, 'w')
            # read the plaintext
            plaintext = inputFile.read()

            # encrypt the plaintext
            ciphertext = desCipher.encrypt(plaintext)

            # write to the file
            outputFile.write(ciphertext)

            inputFile.close()
            outputFile.close()
        elif mode == 'DEC':
            # open the files
            inputFile = open(input_file, 'r')
            outputFile = open(output_file, 'w')

            # read the ciphertext
            ciphertext = inputFile.read()

            # decrypt the ciphertext and remove padding
            plaintext = desCipher.decrypt(ciphertext)

            # write to the file
            outputFile.write(plaintext)

            inputFile.close()
            outputFile.close()
    elif cipher_name == 'AES':
        aesCipher = AES_Cipher()
        aesCipher.set_key(key)
        if mode == 'ENC':
            inputFile = open(input_file, 'r')
            outputFile = open(output_file, 'w')
            # read the plaintext
            plaintext = inputFile.read()

            # encrypt the plaintext
            ciphertext = aesCipher.encrypt(plaintext)

            # write to the file
            outputFile.write(ciphertext)

            inputFile.close()
            outputFile.close()
        elif mode == 'DEC':
            # open the files
            inputFile = open(input_file, 'r')
            outputFile = open(output_file, 'w')

            # read the plaintext
            ciphertext = inputFile.read()

            # decrypt the ciphertext
            plaintext = aesCipher.decrypt(ciphertext)
            # write to the file
            outputFile.write(plaintext)

            inputFile.close()
            outputFile.close()

if __name__ == '__main__':
    main()

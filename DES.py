from CipherInterface import CipherInterface
from Crypto.Cipher import DES

class DES_Cipher(CipherInterface):
    def set_key(self, key):
        #convert hex string to byte array
        self.key = key.decode('hex')

        # print self.key
        self.des = DES.new(self.key, DES.MODE_ECB)
        return True

    def encrypt(self, plaintext):
        self.plaintext_len = len(plaintext)
        #make sure the plaintext is divisible by 8, else pad the text with 0's
        self.plaintext = plaintext
        if ((len(plaintext) % 8) != 0):
            self.plaintext = self.pad_text(plaintext)

        # since DES only encrypts 8 byte blocks at a time...
        text_index = 0
        block_arr = []

        # divide the plaintext into blocks of 8 bytes and store into the block_arr
        while text_index < len(self.plaintext):
            block = self.plaintext[text_index:text_index+8]
            text_index += 8
            block_arr.append(block)

        self.ciphertext = ''
        for blocks in block_arr:
            self.ciphertext += self.des.encrypt(blocks)
        return self.ciphertext

    def decrypt(self, ciphertext):
        self.plaintext = self.des.decrypt(ciphertext)
        self.plaintext = self.unpad_text(self.plaintext)
        return self.plaintext

    # for the encrypt function
    def pad_text(self, plaintext):
        # pad the plaintext until it can be divided into a block of 8 bytes
        while ((len(plaintext) % 8) != 0):
            plaintext += '0'
        return plaintext

    # for the decrypt function
    def unpad_text(self, plaintext):
        #record the plaintext length
        plaintext = list(plaintext)
        i = len(plaintext) - 1
        while plaintext[i] == '0':
            plaintext.pop()
            i -= 1
        return ''.join(plaintext)

from CipherInterface import CipherInterface
from Crypto.Cipher import AES

class AES_Cipher(CipherInterface):
    def set_key(self, key):
        #convert hex string to byte array
        self.aes_key = key
        # Use 128 bit key or 16 bytes
        self.key_size = 16
        self.aes = AES.new(self.aes_key, AES.MODE_ECB)
        return True

    def encrypt(self, plaintext):
        # block of 16 bytes at a time for decrypting
        self.plaintext = plaintext
        self.plaintext_len = len(self.plaintext)
        if ((len(plaintext) % 8) != 0):
            self.plaintext = self.pad_text(plaintext)

        # since AES only encrypts 16 byte blocks at a time...
        text_index = 0
        block_arr = []

        # divide the plaintext into blocks of 8 bytes and store into the block_arr
        while text_index < len(self.plaintext):
            block = self.plaintext[text_index:text_index+16]
            text_index += 16
            block_arr.append(block)

        self.ciphertext = ''
        for blocks in block_arr:
            self.ciphertext += self.aes.encrypt(blocks)
        return self.ciphertext

    def decrypt(self, ciphertext):
        self.plaintext = self.aes.decrypt(ciphertext)
        self.plaintext = self.unpad_text(self.plaintext)
        return self.plaintext

    # for the encrypt function
    def pad_text(self, plaintext):
        self.plaintext_len = len(plaintext)
        # pad the plaintext until it can be divided into a block of 16 bytes
        while ((len(plaintext) % 16) != 0):
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

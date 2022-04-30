
from Crypto import Random
from Crypto.Cipher import AES
import os
import hashlib
import os.path
from os import listdir
from os.path import isfile, join
import time


class Encryptor:
    def __init__(self, key):
        self.key = key

    '''Padding is a way to take data that may or may not be a multiple of 
       the block size for a cipher and extend it out so that it is.
    '''
    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        clear()
        print("Encrypting file....", end='')
        self.key = hashlib.shake_128(input("File password: ").encode("utf-8")).hexdigest(16)
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)
        print("File Encrypted!", end='\n\n')

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        clear()
        print("Decrypting file....", end='')
        self.key = hashlib.shake_128(input("File password: ").encode("utf-8")).hexdigest(16)
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)
        print("File Decrypted!", end='\n\n')

    def getAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if (fname != 'script.py' and fname != 'data.txt.enc'):
                    dirs.append(dirName + "\\" + fname)
        return dirs

    def encrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.encrypt_file(file_name)

    def decrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.decrypt_file(file_name)


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('clear')

if os.path.isfile('data.txt.enc'):
    while True:
        password = hashlib.shake_128(input("Enter password: ").encode("utf-8")).hexdigest(16)
        p = ''
        with open("data.txt.enc", "rb") as f:
            p = enc.decrypt(f.readlines()[0], enc.key).decode('utf-8')
            p = [p]
        if p[0] == password:
            p[0] = hashlib.shake_128(p[0].encode("utf-8")).hexdigest(16)
            print(p[0], len(p[0]), "\n", hashlib.algorithms_available)
            enc.key = p[0]
            break
        # password mismatch code here

    clear()
    while True:
        choice = int(input(
            "1. Encrypt file.\n"
            "2. Decrypt file.\n"
            "3. Exit.\n"
            "Choice: "))
        clear()
        if choice == 1:
            enc.encrypt_file(str(input("File to encrypt: ")))
        elif choice == 2:
            enc.decrypt_file(str(input("File to decrypt: ")))
        elif choice == 3:
            exit()
        else:
            print("Select a valid option!")

else:
    while True:
        clear()
        password = hashlib.shake_128(input("Setting up stuff. \nEnter a password that will be used for decryption: ").encode("utf-8")).hexdigest(16)
        repassword = hashlib.shake_128(input("Confirm password: ").encode("utf-8")).hexdigest(16)
        if password == repassword:
            break
        else:
            print("Passwords Mismatched!")
    f = open("data.txt", "w+")
    f.write(password)
    f.close()
    enc.encrypt_file("data.txt")
    print("Please restart the program to complete the setup")
    time.sleep(5)

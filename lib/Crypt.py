from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from lib.TripleDES import triple_des
import rsa
import os
import hashlib


class Crypt:
    def __init__(self, key = ""):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)
        
    def triplehash(self, passw):
    	has = hashlib.md5(passw.encode()).hexdigest()
    	new = ""
    	for i, j in enumerate(has):
    		if i % 4 == 0:
    			continue
    		else:
    			new += j
    	return new

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_rsa(self, message, pubkey='lib/output/public.pem'):
        f = open(pubkey, 'rb')
        self.key = RSA.importKey(f.read())
        messege = rsa.encrypt(message, self.key)
        return message
    
    def decrypt_rsa(self, message, prikey='lib/output/private.pem'):
    	f = open(prikey, 'rb')
    	self.key = RSA.importKey(f.read())
    	messege = self.key.decrypt(message)
    	return message
	
    def encrypt_file(self, file_name):
    	try:
   			with open(file_name, 'rb') as fo:
   				plaintext = fo.read()
    	except FileNotFoundError:
    		return
    	if len(plaintext) < 245:
    		keyF = input("Public Key file location for RSA [default - lib/output/public.pem]: ")
    		if keyF == '':
    			enc = self.encrypt_rsa(plaintext)
    		else:
    			enc = self.encrypt_rsa(plaintext, keyF)
    	else:
    		print("File too large, RSA not used!")
    		enc = plaintext
        
    	passW = input(f"Set password for [{file_name}]: ")
    	self.key = hashlib.shake_128(passW.encode("utf-8")).hexdigest(16)
    	enc = self.encrypt(enc, self.key)
        
    	self.key = self.triplehash(passW)
    	self.triple = triple_des(self.key)
    	enc = self.triple.encrypt(enc)
        
    	newF = file_name + ".enc"
    	with open(newF, 'wb') as fo:
    		fo.write(enc)
    	print("\nFile Encrypted!")
    	return newF

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
    	with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
            
    	passW = input("File password: ")
        	
    	self.key = self.triplehash(passW)
    	self.triple = triple_des(self.key)
    	ciphertext = self.triple.decrypt(ciphertext)
        
    	self.key = hashlib.shake_128(passW.encode("utf-8")).hexdigest(16)
    	dec = self.decrypt(ciphertext, self.key)
    	
    	keyF = input("Private Key file location for RSA [default - lib/output/private.pem]: ")
    	if keyF == '':
        	keyF = "lib/output/private.pem"
    	try:
    		dec1 = self.decrypt_rsa(dec, keyF)
    	except ValueError:
        	print("Not encrypted using RSA, ignored...")
        	dec1 = dec
        
    	op_file = file_name[:-4]
    	
    	with open(op_file, 'wb') as fo:
            #fo.write(dec1[dec1.index(b'\x00')+1:])
            fo.write(dec1)
    	os.remove(file_name)
    	print("File fully Decrypted!!!")
    	print(f"Output available at: {op_file}")

    def getAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                dirs.append(dirName + "/" + fname)
        return dirs

    def encrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.encrypt_file(file_name)

    def decrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.decrypt_file(file_name)

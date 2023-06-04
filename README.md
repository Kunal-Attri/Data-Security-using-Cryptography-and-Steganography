# SecureIT - Data Security using Cryptography and Steganography
### Demo: [Youtube](#main)
### Run in GitPod
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/kunal-attri/Data-Security-using-Cryptography-and-Steganography/blobmmaster/main.py)


- This is a [Python](https://python.org/) based tool to encrypt files and important data into a very secure form.
- It uses Cryptography (RSA, AES and TripleDES) and Steganography (Image Steganography and Video Steganography)


## Requirements (installable via pip)
- [rsa](https://pypi.org/project/rsa/)
- [pycrypto](https://pypi.org/project/pycrypto/)
- [numpy](https://pypi.org/project/numpy/)
- [imageio](https://pypi.org/project/imageio/)
- [multipledispatch](https://pypi.org/project/multipledispatch/)
- [Pillow](https://pypi.org/project/Pillow/)
- [opencv-python](https://pypi.org/project/opencv-python/)
- [pyDes](https://pypi.org/project/pyDes/)


## What I used?
1. [pycrypto](https://docs.python.org/3/library/crypto.html) - for Cryptography based encryption - It is used to encrypt and decrypt data into secured unreadable form. 
2. [opencv2](https://opencv.org/) - for Steganography - It is used for image and video manipulation. We used it for embedding encrypted data into images/videos.
3. [rsa](https://stuvel.eu/python-rsa-doc/usage.html) - for RSA based encryption - RSA is a asymmetric encryption method, used for encrypting data.


## How to run the program?
1. **Download this GitHub repository**
	- Either Clone the repository
		```
		git clone https://github.com/Kunal-Attri/Data-Security-using-Cryptography-and-Steganography.git
		```
	- Or download and extract the zip archive of the repository.

2. **Download & Install requirements**
	- Ensure that you have Python 3 installed.
	- Open terminal in the Repository folder on your local machine.
	- Run the following command to install requirements.
		```
		pip install -r requirements.txt
 		```
3. **Run the Program**
	```
	python main.py
	```
	*Expected Interface:*
	<br><img src="lib/images/main_screen.png?raw=true">
4. **Generate RSA Keys**
   - If running first time, you need to generate RSA Keys.
   - Generate it using option no 5.
5. **Ready to Secure data**
   - Now, you can secure your data files into either images or videos.


## References
- [Image Cryptography - IJACSA Vol 7, No 6, 2016](http://www.ijarcs.info/index.php/Ijarcs/article/view/2771)
- [B.Schneier "Applied Cryptography", Second Edition: Protocols, Algorithms adnd Source Code in C, Jan 1996](https://archive.org/download/AppliedCryptographyBruceSchneier/Applied%20Cryptography%20%28Bruce%20Schneier%29.pdf)
- [Steganography - A Data Hiding Technique](https://www.researchgate.net/publication/49587597_Steganography-_A_Data_Hiding_Technique)
- [Data Encryption and Decryption by Using Triple DES and Performance Analysis of Crypto System](https://www.ijser.in/archives/v2i11/SjIwMTM0MDM=.pdf)
- [RSA Public Key Cryptography](https://www.researchgate.net/publication/318729097_RSA_Public_Key_Cryptography_Algorithm_-_A_Review)

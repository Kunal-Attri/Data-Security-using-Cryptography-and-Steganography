from tripledes import triple_des

import hashlib


def triplehash(passw):
	has = hashlib.md5(passw.encode()).hexdigest()
	new = ""
	for i, j in enumerate(has):
		if i % 4 == 0:
			continue
		else:
			new += j
	return new

a = triple_des(triplehash("Khan"))

data = "I am Kunal"

cryp = a.encrypt(data)
print(cryp)

b = a.decrypt(cryp)
print(b.decode())


import sys
import hashlib

def hashfile(file):

	# Arbitrary buffer size of 64 kb to read files
	BUF_SIZE = 65536

	sha256 = hashlib.sha256()

	with open(file, 'rb') as f:
		while True:
			data = f.read(BUF_SIZE)

			# data = 0 when we reach EOF
			if not data:
				break
	
			# Updating the SHA256 hash of the file
			sha256.update(data)

	# hexdigest() gives a hexadecimal representation of the hashed value of 
    	# all the data passed to the sha256 function with update()
	return sha256.hexdigest()

f1_hash = hashfile(sys.argv[1])
print(f"Hash: {f1_hash}")



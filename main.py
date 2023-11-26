import sys
import hashlib
# from hashlib import sha256


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
	# return sha256.hexdigest()
	return sha256.digest()
	# return int.from_bytes(sha256.digest(), byteorder='big')


# f1_hash = hashfile(sys.argv[1])
# print(f"Hash: {f1_hash}")


# def hash_file2(message):
# 	message = bytes(message, 'utf-8')
# 	return int.from_bytes(sha512(message).digest(), byteorder='big')




def sim_check(x, y):

	# if len(x) != 1:
	# 	print("invalid")
	# elif len(y) != 1:
	# 	print("invalid")
	
	match = []

	for i in x:
		for j in y:
			if i == j:
				match.append(i)

	print(str(len(match)) + " matches found!")
	print(match)

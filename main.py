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

	# digest() gives a bytes representation of the hashed value of 
    # all the data passed to the sha256 function with update()
	return sha256.digest()


def sim_check2(c, s):
	# if len(x) != 1:
	# 	print("invalid")
	# elif len(y) != 1:
	# 	print("invalid")
	
	client_matches = []
	server_matches = []

	for i in range(len(c)):
		for j in range(len(s)):
			if c[i] == s[j]:
				client_matches.append(i)
				server_matches.append(j)

	client_matches = list(set(client_matches))
	server_matches = list(set(server_matches))

	return [client_matches, server_matches]



def sim_check(x, y):

	# if len(x) != 1:
	# 	print("invalid")
	# elif len(y) != 1:
	# 	print("invalid")
	
	match = []

	for i in range(len(x)):
		for j in range(len(y)):
			if x[i] == y[j] and x[i] not in match:
				match.append

	for i in x:
		for j in y:
			if (i == j) and (i not in match):
				match.append(i)

	print(str(len(match)) + " matches found!")
	print(match)

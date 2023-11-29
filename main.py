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

	# digest() gives a bytes representation of the hashed value of 
    # all the data passed to the sha256 function with update()
	return sha256.digest()




def sim_check2(c, s):

	if len(c) != 5:
		print("invalid")
	elif len(s) != 5:
		print("invalid")
	
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
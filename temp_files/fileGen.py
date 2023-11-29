import random

size = ''
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

while not size.isnumeric():
    size = input('How big would you like your file to be (mb)? ')

size = int(size)

path = input('Where would you like to create the file? ')

open(path, 'w').write('')

for mb in range(size):
    open(path, 'a').write(''.join(random.choices(characters, k=1000000)))

print('Done!')
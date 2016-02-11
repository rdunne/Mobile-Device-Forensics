# Richard dunne
#  Mobile Device Forensics - Lab Sheet 2

# load your modules , hashlib does not by default suport SHA3
# install from https://pypi.python.org/pypi/pysha3/
# version python 3.4
import sys
import hashlib
from sha3 import sha3_256, sha3_512
import string

# This is a program to get the hash checksum of a file.
# Ask user for name of file
str1 = input("Enter full path to file:")
BLOCKSIZE = 65536

# now process the input  into the different  hash Algorithms
hasher = hashlib.sha1()
with open(str1, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
# print to screen result:
print("SHA1 hash checksum is:", hasher.hexdigest())

hasher = hashlib.sha256()
with open(str1, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
		# print to screen result:
print("SHA256 hash checksum is:", hasher.hexdigest())

hasher = hashlib.sha512()
with open(str1, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
		# print to screen result:
print("SHA512 hash checksum is:", hasher.hexdigest())

hasher = hashlib.sha3_256()
with open(str1, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
		# print to screen result:
print("SHA3_256 hash checksum is:", hasher.hexdigest())

hasher = hashlib.sha3_512()
with open(str1, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
		# print to screen result:
print("SHA3_512 hash checksum is:", hasher.hexdigest())

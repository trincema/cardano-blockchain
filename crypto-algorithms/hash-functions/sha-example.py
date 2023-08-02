# Python 3 code to demonstrate
# SHA hash algorithms.

"""
SHA, ( Secure Hash Algorithms ) are set of cryptographic hash functions defined by the language to be used
for various applications such as password security etc. Some variants of it are supported by Python in the
“hashlib” library. These can be found using “algorithms_guaranteed” function of hashlib.
"""

import hashlib
import sys

# Redirect all print() output to a text file
orig_stdout = sys.stdout
f = open('sha-example-out.txt', 'w')
sys.stdout = f

# prints all available algorithms
print ("The available algorithms are : ", end ="")
print (hashlib.algorithms_guaranteed)

print()
  
# initializing string
str = "hash me!"
  
# encoding "hash me!" using encode()
# then sending to SHA256()
result = hashlib.sha256(str.encode())
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())
print(result.digest())
print(result.digest_size)
  
print ()
  
# encoding "hash me!" using encode()
# then sending to SHA384()
result = hashlib.sha384(str.encode())
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())
print(result.digest())
print(result.digest_size)
  
print ()
  
# encoding "hash me!" using encode()
# then sending to SHA224()
result = hashlib.sha224(str.encode())
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())
print(result.digest())
print(result.digest_size)
  
print ()
  
# encoding "hash me!" using encode()
# then sending to SHA512()
result = hashlib.sha512(str.encode())
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())
print(result.digest())
print(result.digest_size)
  
print ()
  
# encoding "hash me!" using encode()
# then sending to SHA1()
result = hashlib.sha1(str.encode())
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
print(result.digest())
print(result.digest_size)
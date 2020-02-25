'''programmed by m1m3'''
import hashlib

def sha1_hash(value):
    sha1_hash = hashlib.sha1()
    sha1_hash.update(value.encode('utf-8'))
    return sha1_hash.hexdigest()


def sha224_hash(value):
    sha224_hash = hashlib.sha224()
    sha224_hash.update(value.encode('utf-8'))
    return sha224_hash.hexdigest()


def sha256_hash(value):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(value.encode('utf-8'))
    return sha256_hash.hexdigest()


def sha384_hash(value):
    sha384_hash = hashlib.sha384()
    sha384_hash.update(value.encode('utf-8'))
    return sha384_hash.hexdigest()


def sha512_hash(value):
    sha512_hash = hashlib.sha512()
    sha512_hash.update(value.encode('utf-8'))
    return sha512_hash.hexdigest()

def md5_hash(value):
    md5_hash = hashlib.md5()
    md5_hash.update(value.encode('utf-8'))
    return md5_hash.hexdigest()

def encode(algorithm, text):
    if algorithm == "1":
        print(f"Successfully Encoded!\n\nEncoded Hash = sha1({sha1_hash(text)})")
    elif algorithm == "2":
        print(f"Successfully Encoded!\n\nEncoded Hash = sha224({sha224_hash(text)})")
    elif algorithm == "3":
        print(f"Successfully Encoded!\n\nEncoded Hash = sha256({sha256_hash(text)})")
    elif algorithm == "4":
        print(f"Successfully Encoded!\n\nEncoded Hash = sha384({sha384_hash(text)})")
    elif algorithm == "5":
        print(f"Successfully Encoded!\n\nEncoded Hash = sha512({sha512_hash(text)})")
    elif algorithm == "6":
        print(f"Successfully Encoded!\n\nEncoded Hash = md5({md5_hash(text)})")

def decode(algorithm, wordlist, hash):
    wordlist = open(wordlist, "r")
    if algorithm == "1":
        method = sha1_hash
    elif algorithm == "2":
        method = sha224_hash
    elif algorithm == "3":
        method = sha256_hash
    elif algorithm == "4":
        method = sha384_hash
    elif algorithm == "5":
        method = sha512_hash
    elif algorithm == "6":
        method = md5_hash
    print(f"Trying to decode  {hash}")
    for word in wordlist:
        if method(word[:len(word)-1]) == hash:
            print(f"\n[+] Successfully decoded: {hash}\n\n[+] Decode Text = {word}")

print()
print("Welcome to the Hashing and Cracking Program!")
print()
print("1. Encode \n2. Decode")
print()
choice = input("Enter you Choice: ")
print()

if choice == "1":
    print("1. sha1 \n2. sha224 \n3. sha256 \n4. sha384 \n5. sha512 \n6. md5")
    print()
    algorithm = input("Enter your Choice: ")
    print()
    text = input("Enter the text to Encode: ")
    print()
    encode(algorithm, text)

elif choice == "2":
    print("1. sha1 \n2. sha224 \n3. sha256 \n4. sha384 \n5. sha512 \n6. md5")
    print()
    algorithm = input("Enter your Choice: ")
    print()
    hash = input("Enter the hash: ")
    print()
    wordlist = input("Specify the path of Wordlist: ") 
    print()
    decode(algorithm, wordlist, hash)
else:
    print("Please Enter a Correct Choice... Exiting the Program!")
    exit()
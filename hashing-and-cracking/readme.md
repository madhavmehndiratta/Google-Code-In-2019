# Hashing And Cracking
A python script to encode or decode a given text.

# Introduction #
Hash functions are used all over the internet in order to securely store passwords, find duplicate records, quickly store and retrieve data, and more. No matter the input, the output of a hash function always has the same size. Encryption can be decrypted but, hashing can not be DE-Hashed(There is no such thing as dehashing). As we can't De-hash string we need to crack them. This program helps to accomplish this task.
# Usage #
```
$ python3 main.py

Welcome to the Hashing and Cracking Program!

1. Encode 
2. Decode
```
Choose 1 for encode and 2 for decode.

### For Encoding: ###
```
Enter you Choice: 1

1. sha1 
2. sha224 
3. sha256 
4. sha384 
5. sha512 
6. md5
```
Choose the algorithm in which you want to encode.

```
Enter your Choice: 6

Enter the text to Encode: test

Successfully Encoded!

Encoded Hash = md5(098f6bcd4621d373cade4e832627b4f6)
```

### For Decoding: ###
```
Enter you Choice: 2

1. sha1 
2. sha224 
3. sha256 
4. sha384 
5. sha512 
6. md5
```
Specify the hashing algorithm.

```
Enter your Choice: 6

Enter the hash: 098f6bcd4621d373cade4e832627b4f6

Specify the path of Wordlist: wordlist.txt

Trying to decode  098f6bcd4621d373cade4e832627b4f6

[+] Successfully decoded: 098f6bcd4621d373cade4e832627b4f6

[+] Decode Text = test
```
NOTE - You need to have a wordlist which contains the original word for cracking the hash.
# Tutorial #
[![asciicast](https://asciinema.org/a/pWs3dBXzP3OktVzqrC3QjepU4.png)](https://asciinema.org/a/pWs3dBXzP3OktVzqrC3QjepU4)


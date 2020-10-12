import sys
from Crypto.Cipher import AES
import base64
import os

def encryption(privateInfo,key):
    BLOCK_SIZE = 16 # 128
    # 128 bit
    #make key 16 characters long padding to the right
    key = key.ljust(16,' ')

    # IV = 16 * '\x00'
    # mode = AES.MODE_CBC
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    # print 'encryption key: ', secret

    cipher = AES.new(key, AES.MODE_CBC,16 * '\x00')

    encoded = EncodeAES(cipher, privateInfo)
    # print 'Encrypted strings', encoded
    return encoded


def main():
    plaintext = "This is top secret."
    c = open("ciphertext.txt","r")
    ciphertext = c.readline() 
    c.close()
    # every word in words.txt
    f = open("words.txt","r")
    words = f.readlines()
    f.close()
    
    # searching through each word to find matching key
    for i in range(len(words)):
        # words[i].pop(len(words[i])-2)
        # print(words[i])
        # print i
        if (len(words[i][:-1]) >= 16):
            continue
        if ciphertext == encryption(plaintext,words[i][:-1]):
            print 'key is: ', words[i]
            return
    print "Couldn't find matching Key"


main()


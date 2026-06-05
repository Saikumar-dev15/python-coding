import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)                                                                 #it will convert string to list
key = chars.copy()                                                                  #to create a encryption key
random.shuffle(key)

print(f"chars: {chars}")
print(f"key : {key}")

#Encrypt
plain_text = input("Enter a message to encrypt:  ")
cipher_text = " "

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]                                    #it will find index letter in index  and give encrypt char          
    
print(f"encrypted message: {cipher_text}")
print(f"original message:  {plain_text}")
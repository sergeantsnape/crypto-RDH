import os
import requests
from PIL import Image 
from io import BytesIO
from Crypto.Cipher import AES 
from dataHiding import decode, encode 


PATH = "img/"

def pad(data): 
    return data + b"\x00"*(16-len(data)%16)  
 
def convert_to_RGB(data): 
    r, g, b = tuple(map(lambda d: [data[i] for i in range(0,len(data)) if i % 3 == d], [0, 1, 2])) 
    pixels = tuple(zip(r,g,b)) 
    return pixels 
     
def process_image(fileName,key,msg): 
    im = Image.open(fileName) 
    
    decoded_data=''
    im = encode(fileName,msg)
        

    data = im.convert("RGB").tobytes()  
    
    original = len(data)  
    key=str(key)
    secrete_key=key[0:32]
    IV = key[0:16]


    new = convert_to_RGB(aes_cbc_encrypt(secrete_key, pad(data),IV)[:original]) 

     
    
    im2 = Image.new(im.mode, im.size) 
    im2.putdata(new)
    im2.save(PATH+'encrypted'+'.png','png')

    im = Image.open("img/encrypted.png") 
    data = im.convert("RGB").tobytes() 
    original = len(data)

    new_dec = convert_to_RGB(aes_cbc_decrypt(secrete_key, pad(data),IV)[:original]) 
    im3 = Image.new(im.mode,im.size)
    im3.putdata(new_dec)

    im3.save(PATH+'decrypted'+'.png','png')
    
 
    decoded_data=decode("img\decrypted.png")

    print(decoded_data)

def aes_cbc_encrypt(key, data,IV, mode=AES.MODE_CBC): 
    aes = AES.new(key.encode("utf8"), mode, IV.encode("utf8")) 
    new_data = aes.encrypt(data) 
    return new_data 
 
def aes_cbc_decrypt(key, data,IV, mode=AES.MODE_CBC):
    aes = AES.new(key.encode("utf8"), mode, IV.encode("utf8")) 
    new_data = aes.decrypt(data)
    return new_data

text='aaabbb123'


'MD5伪加密--------------------------------------'
import hashlib
def get_md5(text):
    hash_md5=hashlib.md5()#其他方法通用
    hash_md5.update(text.encode('utf-8'))
    return hash_md5.hexdigest()
print('MD5:',get_md5(text))


"SHA1基于MD5，加密后的数据更长更安全更慢--------------------------------------"
def get_sha1(text):
    hash_sha1=hashlib.sha1()
    hash_sha1.update(text.encode('utf-8'))
    return hash_sha1.hexdigest()
print('sha1:',get_sha1(text))


'base64伪加密--------------------------------------'
import base64
def get_base64(text):
    return base64.b64encode(text.encode('utf-8'))
encoded=get_base64(text)
print('base64加密:',encoded)

def decode_base64(encoded):
    return base64.b64decode(encoded)
print('base64解密:',decode_base64(encoded))


'采用AES对称加密算法--------------------------------------'
import base64
from Crypto.Cipher import AES #将文件的小写c改为大写

aes_key='aes_key_aaaaaaaa'    # 秘钥 aes_key必须是16位

def add_to_16(value):# str不是16的倍数那就补足为16的倍数
    while len(value) % 16 != 0:
        value += '\0'  #自定义占位符
    return value.encode('utf-8') # 返回bytes

def get_aes(aes_key,text):#加密方法
    # 初始化加密器
    aes = AES.new(aes_key.encode(), AES.MODE_ECB)
    #先进行aes加密
    encrypt_aes = aes.encrypt(add_to_16(text))# 执行加密并转码返回bytes
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8').strip()#自己加的的strip， 后面会有一个换行符
    return encrypted_text
encrypted_text=get_aes(aes_key,text)
print('aes加密:',encrypted_text)

#解密方法
def decode_aes(aes_key,encrypted_text):
    # 初始化加密器
    aes = AES.new(aes_key.encode('utf-8'), AES.MODE_ECB)
    #优先逆向解密base64成bytes
    base64_decrypted = base64.decodebytes(encrypted_text.encode(encoding='utf-8'))
    decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8') # 执行解密密并转码返回str
    return decrypted_text.replace('\0','') #删除占位符
print('aes解密:',decode_aes(aes_key,encrypted_text))


'RSA---------------------------------------------'
import rsa
#生成公钥私钥
# pubkey, privkey = rsa.newkeys(1024)
# pubkey=pubkey.save_pkcs1().decode('utf-8')
# privkey=privkey.save_pkcs1().decode('utf-8')
# print("公钥:\n"+pubkey)
# print("私钥:\n"+privkey)
pubkey= '''-----BEGIN RSA PUBLIC KEY-----
MIGJAoGBAJ1Q+J39PjLrN0a5Qx0bN89bZrg1489IiS33XXxD+ojYm8V8yo1N3s4i
64UP7oAd10HA352s0+SnYSN6MbuC2v2V13AZeCZQZG3D1PXx0xyrd0kHwA7Bnngt
6fD7ECEijiWYRm2TuobiOH5uQXYLsGLzRdWa1mHkkJsMJMHK2ssnAgMBAAE=
-----END RSA PUBLIC KEY-----'''
privkey='''-----BEGIN RSA PRIVATE KEY-----
MIICYQIBAAKBgQCdUPid/T4y6zdGuUMdGzfPW2a4NePPSIkt9118Q/qI2JvFfMqN
Td7OIuuFD+6AHddBwN+drNPkp2EjejG7gtr9lddwGXgmUGRtw9T18dMcq3dJB8AO
wZ54Lenw+xAhIo4lmEZtk7qG4jh+bkF2C7Bi80XVmtZh5JCbDCTBytrLJwIDAQAB
AoGAZ9Fx4UGo9I2KEyBcDC9UK4HUTikySC9EaJNgnIt4ISth0XjDa3FCYqNk7pFP
AjmvPvN8H2BZDgLv9ivDWKhmzYELSAhRhBJ454wsxsa8zBo457UHStAabF3/3Ier
lGppWvcFQ9txYipfg9N6R29hkjc9aMuGDqpa0HuRU3mwU8ECRQD08IPx+RaEWruT
1FgH275xNIEoKx1dzSVAJ02bLw5/rCiTKKv/kbeCii6W6jxkZrWymqWvOgA85DEL
9v2fq/GiWOdj9wI9AKRriYCsGbYphILpps6z38bJZchd2e7CY/bEH7UnyYsHrnHZ
MYszNxZb7kiSEyxJTzkD9U665CALnz6mUQJEH1825yUqNyWP5O1LoSYKDGHXMRfk
mQEPhloCXJ/4UW3xfHe3H/K/+F5OfVHfDlUBbLDWC813/lST2550+aCCQHL2oB0C
PQCD0CKAIXjLbSVqvl6YP+QavcL3iyX4H6d8YWb6GFefOh1D8FejvP9g0XqKe3Eb
g/obP20eHP5eInMcCsECRQDkAEgRIE1m4Bg0LBy67GAEzgKc2hCluTjUwWqS+uo5
Oq4jYFZ82JyZyF3omtZ7aZMzTRVEKp4oyoBrRChMdic/bKAgVw==
-----END RSA PRIVATE KEY-----'''

#公钥加密
def rsaEncrypt(str):
    crypto = rsa.encrypt(str.encode("utf-8"),rsa.PublicKey.load_pkcs1(pubkey.encode('utf-8')))
    return base64.b64encode(crypto).decode()

rsaEncrypt=rsaEncrypt(text)
print('rsa加密:',rsaEncrypt)

#私钥解密
def rsaDecrypt(str, privkey):
    content = rsa.decrypt(base64.b64decode(str.encode('utf-8')), rsa.PrivateKey.load_pkcs1(privkey.encode('utf-8')))
    return content.decode("utf-8")
print('rsa解密:',rsaDecrypt(rsaEncrypt,privkey))

# sign 私钥签名认证、再用公钥验证签名
def create_sign(text):
    signature = rsa.sign(text.encode('utf-8'), rsa.PrivateKey.load_pkcs1(privkey.encode('utf-8')), 'SHA-256')
    return base64.b64encode(signature).decode()
sign=create_sign(text)
print('sign签名:'+sign)

def verify_sign(text,sign):
    try:
        if  rsa.verify(text.encode('utf-8'),base64.b64decode(sign.encode('utf-8')), rsa.PublicKey.load_pkcs1(pubkey.encode('utf-8'))):
            return True
        else:
            return False
    except:
        return False
print('sign验证结果:',verify_sign('text',sign))

'哈希算法集---------------------------------------------'
from passlib.context import CryptContext
from passlib import hash# schemes参数值算法在:passlib.hash

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_hash(text):#哈希加密
    return pwd_context.hash(text)
hash_encrypt=get_hash(text)
print('哈希加密:'+hash_encrypt)

def verify_hash(text,hash_encrypt):
    verity_password_res=pwd_context.verify(text,hash_encrypt)#验证接收用户密码与数据库加密用户密码
    return verity_password_res
print('哈希验证:',verify_hash(text,hash_encrypt))
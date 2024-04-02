from versleutel import encrypteer, decrypteer


print(encrypteer("hello",1))
print(decrypteer("ifmmp",1))
print(decrypteer(encrypteer("test",5),5))
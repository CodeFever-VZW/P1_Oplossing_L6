def verschuif(tekst, verschuiving):
    verschoven_tekst = ""
    for karakter in tekst.lower():
        if karakter.isalpha():
            code = ord(karakter) + verschuiving
            if code > ord('z'):
                code -= 26
            elif code < ord('a'):
                code += 26
            verschoven_tekst += chr(code)
        else:
            verschoven_tekst += karakter
    return verschoven_tekst


def encrypteer(tekst, verschuiving):
    return verschuif(tekst, verschuiving)

def decrypteer(tekst, verschuiving):
    return verschuif(tekst, -verschuiving)
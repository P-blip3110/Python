def cesar_cipher(str, key):
    cipher = ''
    for i in str:
        if i.isalpha():
            cipher += chr(ord(i) + key)
        else:
            cipher += i
    return cipher

    pass

print (cesar_cipher('Cloud', 4))
print (cesar_cipher('Mountain bat haha that is very funny hope all good at you end. Horse are well fed..', 4))
print (cesar_cipher('Giraffe', 10))
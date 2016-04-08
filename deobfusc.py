#!/usr/bin/python3

#############################################
# Auteur    :   Yassir Karroum 
#               [ukarroum17@gmail.com] 
#               [https://github.com/ukarroum]

# Description   : Un petit script qui déobfusc un code JS sans connaissance
#                 de l'encodage utilisé il support pour le moment six encodages : hexadecimal
#               decimal, octal, Unicode, Base64, HTML reference characters
#
#               Tout cela est fait de manière statique
#############################################

def hex2str(code):
    
    while "&#x" in code: 
        pos = code.find("&#x")
        code = code[:pos] + chr(int(code[pos + 3:pos + 5], 16)) + code[pos + 5:] #Suppos que le caractere sera codé sur deux chiffres hexa.
       
    return code

print(hex2str("&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29"))

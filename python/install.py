#!/usr/bin/env python3

"""Install programme for passwd.py implementing E64-BCRYPT"""

import os
import bcrypt
from string import Template

SALT = b'$2a$12$Dlr9CE.XiyEQv0T4nNZyO.'
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

seed = input("Please write a rememberable passphrase to generate E64-BCRYPT salt:\n")
hashpw = bcrypt.hashpw(seed.encode('UTF-8'),SALT)

install_salt = (hashpw[:8] + hashpw[40:60] + b".").decode("ascii")

with open(PATH+"passwd.py","r") as f:
    passwdpy = f.read()

try: 
    passwdpy = Template(passwdpy).substitute(SALT=install_salt)
    with open(PATH+"passwd.py","w") as f:
        f.write(passwdpy)
except ValueError:
    print("Error: passwd.py already has an initialized salt!")
    print("If you want to re-install it, replace the content of SALT by $SALT")

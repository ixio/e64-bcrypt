import argparse
import hashlib
import getpass

# TODO: Check if generated passwd is secure (has one from 0-9,a-z,A-Z and rest)
# TODO: If not remake pass by adding passwd.update("*")

class Chars:
    def __init__(self):
        self.bounds = [(35,38),42,(48,58),(64,90),(97,122),124]

    def __iter__(self):
        return self

    def __next__(self):
        if self.bounds:
            h, *t = self.bounds
            if type(h) == int:
                self.bounds = t
                return chr(h)
            a, b = h
            if a == b:
                self.bounds = t
            else:
                self.bounds = [(a+1,b)]+t 
            return chr(a)
        raise StopIteration

chars = []
for c in Chars():
    chars.append(c)

def trad_num(n):
    (d, m) = divmod(n,len(chars))
    if d > 0:
        return trad_num(d) + chars[m]
    return chars[m]

def trad(s):
    return trad_num(int("".join([str(c) for c in s])))

passwd = hashlib.sha512()

parser = argparse.ArgumentParser(description="Output a strong password")
parser.add_argument("name",type=str)
parser.add_argument("-n",type=int,default=8)
args = parser.parse_args()

passwd.update(args.name.encode("utf-8"))

master_passwd = getpass.getpass(prompt="Master password:")

passwd.update(master_passwd.encode("utf-8"))

print(trad(passwd.digest())[:args.n])

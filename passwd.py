import argparse
import hashlib
import getpass

class Chars:
    def __init__(self):
        self.bounds = [(35,37),42,(48,58),(64,72),(74,78),80,(82,90),(97,107),(109,122)]

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

def is_secure(s):
    types = [0,0,0,0]
    for c in s:
        if ord(c) >= 48 and ord(c) <= 58:
            types[0] += 1
        elif ord(c) >= 65 and ord(c) <= 90:
            types[1] += 1
        elif ord(c) >= 97 and ord(c) <= 122:
            types[2] += 1
        else:
            types[3] += 1
    res = True
    for counter in types:
        res &= counter > 0
    return res

passwd = hashlib.sha512()

parser = argparse.ArgumentParser(description="Output a strong password")
parser.add_argument("name",type=str)
parser.add_argument("-n",type=int,default=8)
args = parser.parse_args()

passwd.update(args.name.encode("utf-8"))
master_passwd = getpass.getpass(prompt="Master password:")
passwd.update(master_passwd.encode("utf-8"))

res = trad(passwd.digest())[:args.n]
while not is_secure(res):
    passwd.update("*".encode("utf-8"))
    res = trad(passwd.digest())[:args.n]
print(res)


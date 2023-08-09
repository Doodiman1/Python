#!/usr/bin/env python3

import re
import hashlib
import os

def get_cert(content):
    search = re.search(r"(-+BEGIN OPENSSH PRIVATE KEY-+\n)(.*\n)*(-+END OPENSSH PRIVATE KEY-+\n)", content, re.MULTILINE)
    cert = search.group()
    return cert
    
def hash_compare(cert):
    thm_hash = "3166226048d6ad776370dc105d40d9f8"
    md5 = hashlib.md5(cert.encode())
    if md5.hexdigest() == thm_hash:
        return "Hash Found"
    else:
        return "Hash NotFound"

def main():
    os.chdir("./keys")
    keys = os.listdir()

    #print(keys)

    for f in keys:
        with open(f, 'r') as file:
            content = file.read()
            key = get_cert(content)
            result =  hash_compare(key)
            if result == "Hash Found":
                print(f"Hash Found: {f}")
    
if __name__ == '__main__':
    main()


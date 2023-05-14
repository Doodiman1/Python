#!/usr/bin/env python3 

import os

files = os.listdir()
movFiles = [file for file in files if file.endswith(".MOV")]
for file in movFiles:
    os.remove(file)

print(movFiles)


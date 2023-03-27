#!/usr/bin/env python

def hexdump(source, length=16, show=True):
 
    HEX_FILTER = ''.join(
        [(len(repr(chr(i))) == 3) and chr(i) or '.'for i in range(256)]
        )

    if isinstance(source, bytes):
        source = source.decode()

    results = list()
    for i in range(0, len(source), length):
        word = str(source[i:i+length])

        printable = word.translate(HEX_FILTER)
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hexwidth = length*3
        results.append(f'{i:04x} {hexa:<{hexwidth}} {printable}')

    if show:
        for line in results:
            print(line)
    else:
        return results 

hexdump('Hello Banananans')

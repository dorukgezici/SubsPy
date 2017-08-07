#!/usr/bin/env python3
import os, sys, hashlib
import requests

LANGUAGES = "http://sandbox.thesubdb.com/?action=languages"
SUBDB_API = "http://api.thesubdb.com/?action=download&language=en&hash="

try:
    f_name = sys.argv[1]
except IndexError as error:
    print("Give the filename as argumant.", error)

def get_hash(name):
        readsize = 64 * 1024
        with open(name, 'rb') as f:
            size = os.path.getsize(name)
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()

f_hash = get_hash(f_name)
url = SUBDB_API + f_hash
headers = {"user-agent": "SubDB/1.0 (DGsub/0.1; http://github.com/dorukgezici)"}

r = requests.get(url, headers=headers)
sub_name = f_name[::-1].split(sep=".", maxsplit=1)[1][::-1] + ".srt"
subtitle = r.text

if subtitle is "":
	print("Subtitle not found!")
else:
	f = open(sub_name, "x")
	f.write(str(subtitle))
	f.close()

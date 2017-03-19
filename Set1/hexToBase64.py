#!/usr/local/bin/python3.5

import sys
import base64
import binascii

""" 
Read input from argument
Convert hex to ascii
Convert ascii to base64
Convert bytes-like object to string
"""

def hexToBase64():
	if (len(sys.argv) != 1):
		return
	hex_str = str(sys.argv[1])
	ascii_str = binascii.unhexlify(hex_str)
	base64_str = base64.b64encode(ascii_str).decode("utf-8")

	print (base64_str)

hexToBase64()
#!/usr/local/bin/python3.5

# 1. Textplain to Hex
# 2. XOR by repeating key
# 3. Hex to Textplain

import sys

def XOR(input):
	hexStr = []
	# Transfer key to hex
	for key in 'ICE':
		hexStr.append(format(ord(key)))

	count = 0
	result = ""
	for c in input:
		result += "{0:02x}".format(int(format(ord(c))) ^ int(hexStr[count]),"x")
		if count >= 2:
			count = 0
		else:
			count += 1
	return result



str1 = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
print (XOR(str1))
#!/usr/local/bin/python3.5

import sys

'''
Check input
Convert hex to binary
XOR two arrays
Convert binary to hex
'''

def fixedXOR():
	if (len(sys.argv) != 3):
		return
	if (len(sys.argv[1]) != len(sys.argv[2])):
		print (len(sys.argv[1]) + " " + len(sys.argv[2]))
		return
	hex_str1 = str(sys.argv[1])
	hex_str2 = str(sys.argv[2])
	bi_str1 = ""
	bi_str2 = ""
	result = ""
	n = 0

	while (n < len(hex_str1)):
		bi_str1 += "{0:04b}".format(int(hex_str1[n],16))
		bi_str2 += "{0:04b}".format(int(hex_str2[n],16))
		n += 1

	n = 0
	while (n < len(bi_str1)):
		if (bi_str1[int(n)] == bi_str2[int(n)]):
			result += "0"
		else:
			result += "1"
		n += 1

	result = hex(int(result, 2))
	print (result)


fixedXOR()
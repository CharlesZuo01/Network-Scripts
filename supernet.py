#!/usr/bin/python

'''
This script will find the supernet for IP addresses inputted as sysarg.  
For example, calling this script with arguments 10.0.0.1 and 10.0.1.1 will return 10.0.0.0/23
'''

import sys

def decimal(x, mask):  
	dec = ''
	for i in range(0,4):
		octet = x[i*8:(i + 1) * 8]
		print octet
		dec = dec + str(int(octet, 2)) + '.' 
	dec = dec[:len(dec)-1] 
	return dec + '/' + str(mask)

def binary(x):  #takes number and converts to 8 bit number
	result =  bin(x)[2:]
	while len(result) < 8:
		result = '0' + result
	return result

ips = []
for i in range(1, len(sys.argv)):
	ips.append(str(sys.argv[i]))


addr = []
for i in ips:
	st = ''
	while len(st) <32 :
		for x in i.split('.'):
			st += binary(int(x))
		addr.append(st)
		break

mask = 35
current = 0
for i in range(0, len(addr)-1):
	current = 0
	for h in range(0,32):
		if addr[i][h] == addr[i+1][h]:  #create var that matches the current address and then compare that to next iteration of loop
			current += 1
		else:
			if i == 0:
				mask = current
			else:
				if current < mask:	
					mask = current
			break

netbits = addr[0][:mask]
while len(netbits) < 32:
	netbits = netbits + '0'
print netbits

print(decimal(netbits, mask))

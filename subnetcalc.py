#!/usr/bin/python

'''
This script takes a address and mask and gives you the subnet range, network, and broadcast addresses
Enter a subnet as x.x.x.x/mask (no spaces) or as x.x.x.x y.y.y.y
This does not work for /31 and /32 masks but you shouldn't need this.
There's no error checking for entering a wrong subnet mask or IP, so please be careful

Used functions because I will eventually add these to a class.
'''

def getIP():   #asks user for ip address and subnet, will return the ip address split into octets and subnet mask.
	
	#Global vars mask is subnet mask as int, IP is ip address octets in list format with elements as int.
	global mask 
	mask = 0
	global IP
	IP = []
	global netmask
	netmask = ''
	st = ''

	print 'Theres no error checking for entering a wrong subnet mask or IP address, please be careful.'
	ipinput = raw_input("Please enter your IP address: ")
	maskinput = raw_input("Please enter your subnet mask: ")
	IP = ipinput.split('.')
	IP = [int(i) for i in IP]
	if len(str(maskinput)) < 3:
		mask = int(maskinput)
	else:
		binmask = maskinput.split('.')
		binmask = [int(i) for i in binmask]
		for i in binary(binmask):
			if i == '1':
				mask += 1

	if mask == 32:
		print 'You have a /32 IP address, which is a host address.  Your IP and subnet mask are {}'.format(userinput)
		exit()
	elif mask == 31:
		slash31()

def binary(x):  #takes IP address octet as a list and converts to 32 bit binary number, i.e 10.10.1.1 to 00001010000010100000000100000001
	netbits = ''
	for i in x:
		octet =  bin(i)[2:]
		while len(octet) < 8:
			octet = '0' + octet
		netbits = netbits + octet
	return netbits	

def netbroadadd(x): #takes a 32 bit binary number as a str, and given the network mask, returns the network address and host address
	# print x[:mask]
	networkad = x[:mask]
	broadad = networkad
	while len(networkad) < 31:
		networkad = networkad + '0'
	netstart = networkad + '1'	
	networkad = networkad + '0'
	while len(broadad) < 31:
		broadad = broadad + '1'
	netend = broadad + '0'
	broadad = broadad + '1'

	return [networkad, broadad, netstart, netend]


def decimal(x):  #converts 32 bit number back to IP address
	dec = ''
	for i in range(0,4):
		octet = x[i*8:(i + 1) * 8]
		dec = dec + str(int(octet, 2)) + '.' 
	dec = dec[:len(dec)-1] 
	return dec 

def slash31(): 
	print 'This is a slash /31 address, use it cautiously outside of non P2P networks.  The address range is {} to {}.  Your netmask is 255.255.255.254'.format(decimal(netbroadadd(binary(IP))[0]), decimal(netbroadadd(binary(IP))[1]))
	exit()
 	

def getnetmask():  #Converts netmask /x format to a.b.c.d
	global netmask
	for i in range (0, mask):
		netmask = netmask + '1'
	while len(netmask) < 32:
		netmask = netmask + '0'
	return netmask


getIP()
print 'Your network is {}/{}'.format(decimal(netbroadadd(binary(IP))[0]), mask)
print 'Netmask: {}'.format(decimal(getnetmask()))
print 'Network address: {}'.format(decimal(netbroadadd(binary(IP))[0]))
print 'Broadcast address: {}'.format(decimal(netbroadadd(binary(IP))[1]))
print 'Usable IP range is {} to {}'.format(decimal(netbroadadd(binary(IP))[2]), decimal(netbroadadd(binary(IP))[3]))


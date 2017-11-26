'''
This script takes a multicast IP address and finds the multicast mac address.  Takes multicast IP, converts
to binary string, then takes the hex value of every 4 chars in that string to find the mac
'''

line = '0000000100000000010111100' . #Beginning of mac address in binary format.

ipinput = raw_input("Please enter your IP address: ")

IP = ipinput.split('.')
IP = [int(i) for i in IP[1:]] . #we don't care about the first octet because we only take last 23 bits of IP address to find mac

mcast = ''
macaddr = ''

for i in IP:
	octet =  bin(i)[2:]
	while (len(octet) < 8):
		octet = '0' + octet
	#print octet
	mcast += octet
	#print mcast
	#print len(mcast)

mcast = mcast[1:] #mcast is 24 bit number but mac address conversion only takes last 23 bits.
line += mcast
mac = [line[i:i+4] for i in range(0, len(line), 4)]

for i in mac:
	macaddr += hex(int(i, 2))[2:]

print macaddr




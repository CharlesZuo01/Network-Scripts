
line = '0000000100000000010111100'

ipinput = raw_input("Please enter your IP address: ")

IP = ipinput.split('.')
IP = [int(i) for i in IP[1:]]

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




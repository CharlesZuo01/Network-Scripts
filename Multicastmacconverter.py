'''
This script takes a multicast IP address and finds the multicast mac address.  Takes multicast IP, converts
to binary string, then takes the hex value of every 4 chars in that string to find the mac
'''

print "There's no error checking, please be careful and enter IP addresses correctly"

first25 = '0000000100000000010111100' #First 25 bits of multicast mac address 

first = [] #stores the first octet of multicast range, e.g 224,225, 226, etc... used to provide collision addresses
second = 0 #second octet, will +/- 128 used to provide collision addresses

ipinput = raw_input("Please enter your IP address: ")
IP = ipinput.split('.')
firstoctet = IP[0]
IP = [int(i) for i in IP[1:]]

for i in range(224,240):
	first.append(i)

first.remove(int(firstoctet))

if IP[0] <= 128:
	second = IP[0] + 128
else:
	second = IP[0] - 128

mcast = ''
macaddr = ''
#print IP

for i in IP:
	octet =  bin(i)[2:]
	while (len(octet) < 8):
		octet = '0' + octet
	mcast += octet

mcast = mcast[1:] #mcast is 24 bit number but mac address conversion only takes last 23 bits.

first25 += mcast
mac = [first25[i:i+4] for i in range(0, len(first25), 4)]
for i in mac:
	macaddr += hex(int(i, 2))[2:]

print 'Here is your MAC address:  ', macaddr
print 'Here are the multicast addresses with the same mac address'
for i in first:
	print str(i) + '.' + str(second) + '.' + str(IP[1]) + '.' + str(IP[2])
	print str(i) + '.' + str(IP[0]) + '.' + str(IP[1]) + '.' + str(IP[2])






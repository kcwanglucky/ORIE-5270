import bitstring

def isSubnormal(a):
	b = bitstring.pack('>d', a)
	sbits = b[0:1]
	ebits = b[1:12]
	mbits = b[12:]
	minExp = bitstring.BitArray(bin='00000000000')
	
	zero = 0 
	pack_zero = bitstring.pack('>d', zero)
	mbits_zero = pack_zero[12:]

	if ebits.bin == minExp.bin and mbits.bin != mbits_zero.bin :
		return True
	else:
		return False

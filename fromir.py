# This is the file to generate IF filr from binary for RMIR to edit.
import sys    
import numbers
# Iteration over all arguments:
hfile = open(sys.argv[1],'r')
ofile = open(sys.argv[2],'wb')
newFileByteArray  = bytearray(0x400)
o = 0
for line in hfile:
	if line[0:1] != '0':
		break
	j = 0;
	while (j < 16):
		data = line[7 + j * 4: 7 + j * 4 + 2]
		newFileByteArray[o] = int(data,16)
		o = o + 1
		j = j + 1
	
ofile.write(newFileByteArray)
ofile.close()
hfile.close()
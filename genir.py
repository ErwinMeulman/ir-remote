# This is the file to generate IF filr from binary for RMIR to edit.
import sys    
import numbers
# Iteration over all arguments:
hfile = open(sys.argv[1],'rb')
chunk = bytearray(hfile.read(1024));
fmt = '{:04X}' * 1
fmtdata = '{:02X}' * 1
hfile.close()
i = 0;
while True:
	address = fmt.format(i)
	textline = address + ':  '
	j = 0;
	while (j < 16):
		textline += fmtdata.format(chunk[i  + j])
		textline += '  '
		j = j + 1
	print(textline)
	i += 16
	if (i == 0x400):	
		break;
print('\r')
print('[Notes]')
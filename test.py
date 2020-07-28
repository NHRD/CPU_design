MOV = 0
ADD = 1
SUB = 2
AND = 3
OR  = 4
SL  = 5
SR  = 6
SRA = 7
LDL = 8
LDH = 9
CMP = 10
JE  = 11
JMP = 12
LD  = 13
ST  = 14
HLT = 15

#register address at decimal.
REG0 = 0
REG1 = 1
REG2 = 2
REG3 = 3
REG4 = 4
REG5 = 5
REG6 = 6
REG7 = 7

ival = 0



def mov(ra, rb):
    return int(bin(MOV << 11), 2) | int(bin(ra << 8), 2) | int(bin(rb << 5), 2)

def add(ra, rb):
    return int(bin(ADD << 11), 2) | int(bin(ra << 8), 2) | int(bin(rb << 5), 2)

def ldh(ra, ival):
	return int(bin(LDH << 11), 2) | int(bin(ra << 8), 2) | (ival & int(bin(0xff), 2))

def op_code(ir):
	return  int(bin(ir >> 11), 2)

def hlt():
	return int(bin(HLT << 11), 2)

result = bin(ldh(REG0, ival))
result = bin(mov(REG0, REG2))
result = bin(add(REG0, REG2))
halt = hlt()
result = int(op_code(halt), 2)

print(result)
#print(len(result[2:]))
#print(result[2:])

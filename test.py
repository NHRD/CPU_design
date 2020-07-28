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

def sub(ra, rb):
    return int(bin(SUB << 11), 2) | int(bin(ra << 8), 2) | int(bin(rb << 5), 2)

def And(ra, rb):
    return int(bin(AND << 11), 2) | int(bin(ra << 8), 2) | int(bin(rb << 5), 2)

def Or(ra, rb):
    return int(bin(OR << 11), 2) | int(bin(ra << 8), 2) | int(bin(rb << 5), 2)

def sl(ra):
	return int(bin(SL << 11), 2) | int(bin(ra << 8), 2)

def sr(ra):
	return int(bin(SR << 11), 2) | int(bin(ra << 8), 2)

def sra(ra):
	return int(bin(SRA << 11), 2) | int(bin(ra << 8), 2)

def ldl(ra, ival):
	return int(bin(LDL << 11), 2) | int(bin(ra << 8), 2) | (ival & int(bin(0x00ff), 2))

def ldh(ra, ival):
	return int(bin(LDH << 11), 2) | int(bin(ra << 8), 2) | (ival & int(bin(0x00ff), 2))

def Cmp(ra, rb):
	return int(bin(CMP << 11), 2) | int(bin(ra << 8), 2) | int(bin(rb << 5), 2)

def je(addr):
	return int(bin(JE << 11), 2) | (int(bin(addr), 2) & int(bin(0x00ff), 2))

def jmp(addr):
	return int(bin(JMP << 11), 2) | (int(bin(addr), 2) & int(bin(0x00ff), 2))

def ld(ra, addr):
	return int(bin(LD << 11), 2) | int(bin(ra << 8), 2) | (int(bin(addr), 2) & int(bin(0x00ff), 2))

def st(ra, addr):
	return int(bin(ST << 11), 2) | int(bin(ra << 8), 2) | (int(bin(addr), 2) & int(bin(0x00ff), 2))

def hlt():
	return int(bin(HLT << 11), 2)

def op_code(ir):
	return  int(bin(ir >> 11), 2)

def op_regA(ir):
	return int(bin(ir >> 8), 2) & int(bin(0x0007), 2)

def op_regB(ir):
	return int(bin(ir >> 5), 2) & int(bin(0x0007), 2)

def op_data(ir):
	return int(bin(ir), 2) & int(bin(0x00ff), 2)

def op_addr(ir):
    return int(bin(ir), 2) & int(bin(0x00ff), 2)



result = bin(ldh(3, 0))
print(result)
print(bin(4800))

0b100101100000000
1001011000000
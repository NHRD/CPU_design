#instruction set
#instruction numbers are decimal, need to be converted to binary
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

#memory
reg = [0 for i in range(8)]
rom = [0 for i in range(256)]
ram = [0 for i in range(256)]

def assembler():
    #assembly code for sum of 1 to 10
    rom[0]   =   ldh(REG0, 0)
    rom[1]   =   ldl(REG0, 0)
    rom[2]   =   ldh(REG1, 0)
    rom[3]   =   ldl(REG1, 1)
    rom[4]   =   ldh(REG2, 0)
    rom[5]   =   ldl(REG2, 0)
    rom[6]   =   ldh(REG3, 0)
    rom[7]   =   ldl(REG3, 10)
    rom[8]   =   add(REG2, REG1)
    rom[9]   =   add(REG0, REG2)
    rom[10]  =   st(REG0, 64)
    rom[11]  =   Cmp(REG2, REG3)
    rom[12]  =   je(14)
    rom[13]  =   jmp(8)
    rom[14]  =   hlt()
    return 0

#main function
def main():

    pc = 0       #program counter.
    ir = 0     #instruction register.
    flag_eq = 0  #comparison flag.

    assembler()

    while(op_code(ir)!= HLT):

        ir = rom[pc] #rom position
        print("{} {} {} {} {} {}" .format(pc, hex(ir)[2:], reg[0], reg[1], reg[2], reg[3]))
    
        pc = pc + 1

        if op_code(ir)== MOV:
            reg[op_regA(ir)] = reg[op_regB(ir)]

        elif op_code(ir)== ADD:
            reg[op_regA(ir)] = reg[op_regA(ir)] + reg[op_regB(ir)]

        elif op_code(ir)== SUB:
            reg[op_regA(ir)] = reg[op_regA(ir)] - reg[op_regB(ir)]

        elif op_code(ir)== AND:
            reg[op_regA(ir)] = reg[op_regA(ir)] & reg[op_regB(ir)]

        elif op_code(ir)== OR:
            reg[op_regA(ir)] = reg[op_regA(ir)] | reg[op_regB(ir)]

        elif op_code(ir)== SL:
            reg[op_regA(ir)] = int(bin(reg[op_regA(ir)] << 1), 2)

        elif op_code(ir)== SR:
            reg[op_regA(ir)] = int(bin(reg[op_regA(ir)] >> 1), 2)

        elif op_code(ir)== SRA:
            reg[op_regA(ir)] = (reg[op_regA(ir)] & int(bin(0x8000), 2)) | int(bin(reg[op_regA(ir)] >> 1), 2)

        elif op_code(ir)== LDL:
            reg[op_regA(ir)] = (reg[op_regA(ir)] & int(bin(0xff00), 2)) | (op_data(ir) & int(bin(0xff00), 2))

        elif op_code(ir)== LDH:
            reg[op_regA(ir)] = int(bin(op_data(ir) << 8), 2) | (reg[op_regA(ir)] & int(bin(0x00ff), 2))

        elif op_code(ir)== CMP:
            if(reg[op_regA(ir)] == reg[op_regB(ir)]):
                flag_eq = 1
            else:
                flag_eq = 0

        elif op_code(ir)== JE:
            if flag_eq == 1:
                pc = op_addr(ir)

        elif op_code(ir)== JMP:
            pc = op_addr(ir)
        
        elif op_code(ir)== LD:
            reg[op_regA(ir)] = ram[op_addr(ir)]

        elif op_code(ir)== ST:
            ram[op_addr(ir)] = reg[op_regA(ir)]

    print("ram[64] = {} \n]" .format(ram[64]))
    return 0


#definitions of functions
#inputs to functions and return values are all int type.
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

#if __name__ == "__main__":

main()
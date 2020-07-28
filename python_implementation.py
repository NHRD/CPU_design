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
reg = []
rom = []
ram = []

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

    while(int(op_code(ir), 2) != HLT):

        ir = rom[pc] #rom position
        print("{} {} {} {} {} {} \n" .format(pc, ir, reg[0], reg[1], reg[2], reg[3]))
    
        pc = pc + 1

        if int(op_code(ir), 2) == MOV:
            reg[op_regA(ir)] = reg[op_regB(ir)]
            break

        elif int(op_code(ir), 2) == ADD:
            reg[op_regA(ir)] = reg[op_regA(ir)] + reg[op_regB(ir)]
            break

        elif int(op_code(ir), 2) == SUB:
            reg[op_regA(ir)] = reg[op_regA(ir)] - reg[op_regB(ir)]
            break

        elif int(op_code(ir), 2) == AND:
            reg[op_regA(ir)] = reg[op_regA(ir)] & reg[op_regB(ir)]
            break

        elif int(op_code(ir), 2) == OR:
            reg[op_regA(ir)] = reg[op_regA(ir)] | reg[op_regB(ir)]
            break

        elif int(op_code(ir), 2) == SL:
            reg[op_regA(ir)] = reg[op_regA(ir)] << 1
            break

        elif int(op_code(ir), 2) == SR:
            reg[op_regA(ir)] = reg[op_regA(ir)] >> 1
            break

        elif int(op_code(ir), 2) == SRA:
            reg[op_regA(ir)] = (reg[op_regA(ir)]) and (bin(int("8000", 16)) or (reg[op_regA(ir)] >> 1))
            break

        elif int(op_code(ir), 2) == LDL:
            reg[op_regA(ir)] = (reg[op_regA(ir)]) and (bin(int("ff00", 16)) or (op_data(ir) and bin(int("ff00", 16))))
            break

        elif int(op_code(ir), 2) == LDH:
            reg[op_regA(ir)] = (op_data(ir) << 8) or (reg[op_regA(ir)] and bin(int("00ff", 16)))
            break

        elif int(op_code(ir), 2) == CMP:
            if(reg[op_regA(ir)] == reg[op_regB(ir)]):
                flag_eq = 1
            else:
                flag_eq = 0
            break

        elif int(op_code(ir), 2) == JE:
            if(flag_eq == 1):
                pc = op_addr(ir)
            break

        elif int(op_code(ir), 2) == JMP:
            pc = op_addr(ir)
            break
        
        elif int(op_code(ir), 2) == LD:
            reg[op_regA(ir)] = ram[op_addr(ir)]
            break

        elif int(op_code(ir), 2) == ST:
            ram[op_addr(ir)] = reg[op_regA(ir)]
            break

        else:
            break

    printf("ram[64] = {} \n]" .format(ram[64]))
    return 0


#definitions of functions
#return values are all int type.
def mov(ra, rb):
    return int(bin(MOV << 11), 2) | int(bin(ra << 8), 2) | int(bin(rb << 5), 2)

def add(ra, rb):
    return int(bin(ADD << 11), 2) | int(bin(ra << 8), 2) | int(bin(rb << 5), 2)

def sub(ra, rb):
    return bin(SUB << 11) or bin(ra << 8) or bin(rb << 5)

def And(ra, rb):
    return bin(AND << 11) or bin(ra << 8) or bin(rb << 5)

def Or(ra, rb):
    return bin(OR << 11) or bin(ra << 8) or bin(rb << 5)

def sl(ra):
	return bin(SL << 11) or bin(ra << 8)

def sr(ra):
	return bin(SR << 11) or bin(ra << 8)

def sra(ra):
	return bin(SRA << 11) or bin(ra << 8)

def ldl(ra, ival):
	return bin(LDL << 11) or bin(ra << 8) or (bin(ival) and bin(0xff))

def ldh(ra, ival):
	return int(bin(LDH << 11), 2) | int(bin(ra << 8), 2) | (ival & int(bin(0xff), 2))

def Cmp(ra, rb):
	return bin(CMP << 11) or bin(ra << 8) or bin(rb << 5)

def je(addr):
	return bin(JE << 11) or (bin(addr) and bin(int("ff", 16)))

def jmp(addr):
	return bin(JMP << 11) or (bin(addr) and bin(int("ff", 16)))

def ld(ra, addr):
	return bin(LD << 11) or bin(ra << 8) or (bin(addr) and bin(int("ff", 16)))

def st(ra, addr):
	return bin(ST << 11) or bin(ra << 8) or (bin(addr) and bin(int("ff", 16)))

def hlt():
	return int(bin(HLT << 11), 2)

def op_code(ir):
	return  int(bin(ir >> 11), 2)

def op_regA(ir):
	return bin(ir >> 8) and bin(int("07", 16))

def op_regB(ir):
	return bin(ir >> 5) and bin(int("07", 16))

def op_data(ir):
	return ir and bin(int("ff", 16))

def op_addr(ir):
	return ir and bin(int("ff", 16))

main()
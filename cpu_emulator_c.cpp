#include <stdio.h>

//instruction set
#define MOV 0
#define ADD 1
#define SUB 2
#define AND 3
#define OR  4
#define SL  5
#define SR  6
#define SRA 7
#define LDL 8
#define LDH 9
#define CMP 10
#define JE  11
#define JMP 12
#define LD  13
#define ST  14
#define HLT 15

//general purpose registers
#define REG0 0
#define REG1 1
#define REG2 2
#define REG3 3
#define REG4 4
#define REG5 5
#define REG6 6
#define REG7 7

//memory address
short reg[8];
short rom[256];
short ram[256];

//assembler block
void assembler(void);

short mov(short, short);
short add(short, short);
short sub(short, short);
short And(short, short);
short Or(short, short);
short sl(short);
short sr(short);
short sra(short);
short ldl(short, short);
short ldh(short, short);
short cmp(short, short);
short je(short);
short jmp(short);
short ld(short, short);
short st(short, short);
short hlt(void);
short op_code(short);
short op_regA(short);
short op_regB(short);
short op_data(short);
short op_addr(short);

void main(void) {

    short pc;       //program counter.
    short ir;       //instruction register.
    short flag_eq;  //comparison flag.

    assembler();

    //reset value of program counter and comparison flag.
    pc = 0;
    flag_eq = 0;

    do{
        ir = rom[pc]; //rom position
        printf("%5d %5x %5d %5d %5d %5d \n",
        pc, ir, reg[0], reg[1], reg[2], reg[3]);
    
    pc = pc + 1;

    switch(op_code(ir)){

        case    MOV :   reg[op_regA(ir)] = reg[op_regB(ir)];
                        break;
        case    ADD :   reg[op_regA(ir)] = reg[op_regA(ir)] + reg[op_regB(ir)];
                        break;
        case    SUB :   reg[op_regA(ir)] = reg[op_regA(ir)] - reg[op_regB(ir)];
                        break;
        case    AND :   reg[op_regA(ir)] = reg[op_regA(ir)] & reg[op_regB(ir)];
                        break;
        case    OR  :   reg[op_regA(ir)] = reg[op_regA(ir)] | reg[op_regB(ir)];
                        break;
        case    SL  :   reg[op_regA(ir)] = reg[op_regA(ir)] << 1;
                        break;
        case    SR  :   reg[op_regA(ir)] = reg[op_regA(ir)] >> 1;
                        break;
        case    SRA :   reg[op_regA(ir)] = (reg[op_regA(ir)] & 0x8000) | (reg[op_regA(ir)] >> 1);
                        break;
        case    LDL :   reg[op_regA(ir)] = (reg[op_regA(ir)] & 0xff00) | (reg[op_data(ir)] & 0x00ff);
                        break;
        case    LDH :   reg[op_regA(ir)] = (reg[op_regA(ir)] << 8) | (reg[op_data(ir)] & 0x00ff);
                        break;
        case    CMP :   if(reg[op_regA(ir)] == reg[op_regB(ir)]) {
                            flag_eq = 1;
                        }else{
                            flag_eq = 0;
                        };
                        break;
        case    JE  :   if(flag_eq == 1) pc = op_addr(ir);
                        break;
        case    JMP :   pc = op_addr(ir);
                        break;
        case    LD  :   reg[op_regA(ir)] = ram[op_addr(ir)];
                        break;
        case    ST  :   ram[op_addr(ir)] = reg[op_regA(ir)];
                        break;
        default     :   break;

        }
    } while(op_code(ir) != HLT);
    printf("ram[64 = %d \n]", ram[64]);
}

void assembler(void) {
    
}
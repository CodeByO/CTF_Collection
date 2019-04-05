#!/usr/bin/python

from pwn import u32, p32

def ILLEGAL():
  print 'Illegal Instruction!'
  exit()

def VM(code):
  LEN = len(code)
  PC = 0

  while PC < LEN:
    code1 = u32(code[PC:PC+4])
    PC += 4
    t = (code1 >> 16)&0xff
    if t == 1 or t == 4:
      code2 = u32(code[PC:PC+4], sign="signed")
      a5 = code2
      PC += 4
    
    OP = code1 >> 24
    OP_TYPE = t
    a3 = (code1 >> 8) & 0xff
    a4 = code1 & 0xff

    print '[%3x] '%(PC - 4),     

    if OP == 0:
      if OP_TYPE:
        print 'ADD r%d, 0x%x'%(a3, code2)
      else:
        print 'ADD r%d, r%d'%(a3, a4)
        
    elif OP == 1:
      if OP_TYPE:
        print 'SUB r%d, 0x%x'%(a3, code2)
      else:
        print 'SUB r%d, r%d'%(a3, a4)
       
    elif OP == 2:
      if OP_TYPE:
        print 'XOR r%d, 0x%x'%(a3, code2)
      else:
        print 'XOR r%d, r%d'%(a3, a4)
    elif OP == 3:
      if OP_TYPE:
        print 'OR r%d, 0x%x'%(a3, code2)
      else:
        print 'OR r%d, r%d'%(a3, a4)
    elif OP == 4:
      if OP_TYPE:
        print 'AND r%d, 0x%x'%(a3, code2)
      else:
        print 'AND r%d, r%d'%(a3, a4)
    elif OP == 5:
      if OP_TYPE:
        print 'MUL r%d, 0x%x'%(a3, code2)
      else:
        print 'MUL r%d, r%d'%(a3, a4)
    elif OP == 6:
      if OP_TYPE:
        print 'DIV r%d, 0x%x'%(a3, code2)
      else:
        print 'DIV r%d, r%d'%(a3, a4)

    elif OP == 7:
      if not OP_TYPE:
        print 'INC r%d'%(a3)
      else:
        ILLEGAL()

    elif OP == 8:
      if not OP_TYPE:
        print 'DEC r%d'%(a3)
      else:
        ILLEGAL()

    elif OP == 9:
      if not OP_TYPE:
        print 'NOT r%d'%(a3)
      else:
        ILLEGAL()

    elif OP == 10:
      if OP_TYPE:
        print 'CMP r%d, 0x%x'%(a3, code2)
      else:
        print 'CMP r%d, r%d'%(a3, a4)

    elif OP == 11:
      if OP_TYPE:
        print 'JE 0x%x'%(PC-4 + a5)
      else:
        ILLEGAL()

    elif OP == 12:
      if OP_TYPE:
        print 'JNE 0x%x'%(PC-4+a5)
      else:
        ILLEGAL()

    elif OP == 13:
      if OP_TYPE:
        print 'JMP 0x%x'%(a5)
      else:
        ILLEGAL()

    elif OP == 14:
      if OP_TYPE:
        print 'CALL 0x%x'%(PC-4+a5)
      else:
        print 'CALL 0x%x'%(PC-4+a3)

    elif OP == 15:
      print 'RET'

    elif OP == 16:
      if OP_TYPE == 5:
        print 'PUSHB 0x%x'%(a3)
      elif OP_TYPE == 1:
        print 'PUSH 0x%x'%(a5)
      elif OP_TYPE == 0:
        print 'PUSH r%d'%(a3)
      else:
        ILLEGAL()

    elif OP == 17:
      if not OP_TYPE:
        print 'POP r%d'%(a3)
      else:
        ILLEGAL()

    elif OP == 18:
      if OP_TYPE:
        print 'SHR r%d, 0x%x'%(a3, code2)
      else:
        print 'SHR r%d, r%d'%(a3, a4)
     
    elif OP == 19:
      if OP_TYPE:
        print 'SHL r%d, 0x%x'%(a3, code2)
      else:
        print 'SHL r%d, r%d'%(a3, a4)

    elif OP == 20:
      if OP_TYPE == 1:
        print 'MOV r%d, 0x%x'%(a3, a5)
      elif OP_TYPE == 2:
        print 'MOV r%d, [stack+r%d]'%(a3, a4)
      elif OP_TYPE == 3:
        print 'MOV [stack+r%d], r%d'%(a3, a4)
      elif OP_TYPE == 4:
        print 'MOV [stack+r%d], 0x%x'%(a3, a5)
      elif OP_TYPE == 0:
        print 'MOV r%d, r%d'%(a3, a4)
      else:
        ILLEGAL()

    elif OP == 21:
      print 'SYSCALL r0'

    elif OP == 22:
      print 'NOP'
      PC -= 3
    else:
      ILLEGAL()

if __name__ == '__main__':
  VM(open("./bbbig.bin").read())


'''
class Disasm():

  def _init_(self, code):
    
    return

  def run(
'''


#print('Fetch instruction '+in[1].lower()+'from address '+in[0].lower(),end='\n')
#print('DECODE: Operation is '+', First Operand is '+', immediate Second Operand is '+', Destination Register is '+'.',end='\n')
#print('Read Registers: ')
#print(' = ')
#print(end='\n')
#print('EXECUTE: '+' in ',end='\n');
#print('MEMORY: No memory operation',end='\n');
#print('WRITEBACK: write '+' to ',end='\n');

reg = 0;
instr = [];
b = [];
opcode = [];
cond = [];
middle = [];
pointer = 0;


def decode():
  print();

if __name__ == '__main__':
  f = open("test.mem","r");
  if f == null:
    print("File does not exist.")
    exit(1);
  for l in f:
    instr.append(l.replace('\n',''));
  for l in instr:
    b.append(bin(int(l[7:],16))[2:])
  for l in b:
    cond.append(l[0:4]);
    middle.append(l[4:7]);
    opcode.append(l[7:11]);
  print(cond);
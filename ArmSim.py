while(True)
  in= input().lstrip().rstrip().split(' ')
  b = bin(int(in[1][2:],16))[2:]
  print('Fetch instruction '+in[1].lower()+'from address '+in[0].lower(),end='\n')
  print('DECODE: Operation is '+', First Operand is '+', immediate Second Operand is '+', Destination Register is '+'.',end='\n')
  print('Read Registers: ')
  print(' = ')
  print(end='\n')
  print('EXECUTE: '+' in ',end='\n');
  print('MEMORY: No memory operation',end='\n');
  print('WRITEBACK: write '+' to ',end='\n');
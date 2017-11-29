
#print('Fetch instruction '+in[1].lower()+'from address '+in[0].lower(),end='\n')
#print('DECODE: Operation is '+', First Operand is '+', immediate Second Operand is '+', Destination Register is '+'.',end='\n')
#print('Read Registers: ')
#print(' = ')
#print(end='\n')
#print('EXECUTE: '+' in ',end='\n');
#print('MEMORY: No memory operation',end='\n');
#print('WRITEBACK: write '+' to ',end='\n');

reg = [0]*16;
instr = [];
b = [];
opcode = [];
cond = [];
middle = [];
memory = [i for i in range(2048)]
Z = 0;
V = 0;
C = 0;
N = 0;
def decode():
	lel = b[reg[15]]
	condstring = ""
	mainstring = ""
	firstop = ""
	secondop = ""
	destinationreg = ""
	num  = str(lel)
	if (num[:4]=="0000"):
		condstring = "EQ"
	elif (num[:4]=="0001"):
		condstring = "NE"
	elif (num[:4]=="0100"):
		condstring = "MI"
	elif (num[:4]=="0101"):
		condstring = "PL"
	elif (num[:4]=="1010"):
		condstring = "GE"
	elif (num[:4]=="1011"):
		condstring = "LT"
	elif (num[:4]=="1100"):
		condstring = "GT"
	elif (num[:4]=="1101"):
		condstring = "LE"
	if(num[4:6]=="00"):
		if(num[7:10]=="0000"):
			mainstring = "AND"

		elif(num[7:10]=="0010"):
			mainstring = "SUB"
		elif(num[7:10]=="0100"):
			mainstring = "ADD"
		elif(num[7:10]=="1010"):
			mainstring = "CMP"
		elif(num[7:10]=="1011"):
			mainstring = "CMN"
		elif(num[7:10]=="1100"):
			mainstring = "ORR"
		elif(num[7:10]=="1101"):
			mainstring = "MOV"
		elif(num[7:10]=="1111"):
			mainstring = "MVN"
		firstop = "R"+str(int(lel[12:16],2))
		if(num[6]=="0"):
			secondop = "R" + str(int(lel[20:],2))
			print("Operation is "+mainstring+condstring+", First Operand is "+firstop+", immediate Second Operand is "+secondop)
		else:
			secondop = str(int(lel[20:],2))
			print("Operation is "+mainstring+condstring+", First Operand is "+firstop+",  Second Operand is "+secondop)
		destinationreg = "R" + str(int(lel[16:20],2))
		print("Destination Register is "+destinationreg)
	elif(num[4:6]=="01"):
		firstop = "R"+str(int(lel[12:16],2))
		secondop = "R"+str(int(lel[16:20],2))
		if(num[11]=="0"):
			mainstring = "STR"
			print("Operation is "+mainstring+condstring+", First operand(base address) is "+firstop+", Source register is "+secondop)
		elif(num[11]=="1"):
			mainstring = "LDR"
			print("Operation is "+mainstring+condstring+", First operand(base address) is "+firstop+", Destination register is "+secondop)
		offset = str(int(lel[20:],2))
		print("Offset is "+offset)
	elif(num[4:6]=="10"):
		mainstring = "B"
		print("Operation is "+mainstring+condstring)


if __name__ == '__main__':
  f = open("test.mem","r");
  if f == None:
    print("File does not exist.")
    exit(1);
  for l in f:
    instr.append(l.replace('\n',''));
  for l in instr:
    b.append(bin(int(l[l.find(' ')+1:],16))[2:])
  for l in b:
    cond.append(l[0:4]);
    middle.append(l[4:7]);
    opcode.append(l[7:11]);
  while(True):
    print("Fetch instruction "+instr[reg[15]][instr[reg[15]].find(" "):]+" from address "+instr[reg[15]][0:instr[reg[15]].find(" ")]);
  print(instr);
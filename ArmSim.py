
#print('Fetch instruction '+in[1].lower()+'from address '+in[0].lower(),end='\n')
#print('DECODE: Operation is '+', First Operand is '+', immediate Second Operand is '+', Destination Register is '+'.',end='\n')
#print('Read Registers: ')
#print(' = ')
#print(end='\n')
#print('EXECUTE: '+' in ',end='\n');
#print('MEMORY: No memory operation',end='\n');
#print('WRITEBACK: write '+' to ',end='\n');

reg = [0]*16;
global flag;
nxt=0;
instr = [];
b = [];
opcode = [];
cond = [];
middle = [];
memory = [0]*2048
global Z,N

def twos_comp(val, bits):
    if (val & (1 << (bits - 1))) != 0: 
        val = val - (1 << bits)       
    return val   


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
		if(num[7:11]=="0000"):
			mainstring = "AND"

		elif(num[7:11]=="0010"):
			mainstring = "SUB"
		elif(num[7:11]=="0100"):
			mainstring = "ADD"
		elif(num[7:11]=="1010"):
			mainstring = "CMP"
		elif(num[7:11]=="1011"):
			mainstring = "CMN"
		elif(num[7:11]=="1100"):
			mainstring = "ORR"
		elif(num[7:11]=="1101"):
			mainstring = "MOV"
		elif(num[7:11]=="1111"):
			mainstring = "MVN"
		destinationreg = "R" + str(int(lel[16:20],2))
		firstop = "R"+str(int(lel[12:16],2))
		if(num[6]=="0"):
			secondop = "R" + str(int(lel[20:],2))
			print("DECODE : Operation is "+mainstring+condstring+", First Operand is "+firstop+",Second Operand is "+secondop+", Destination Register "+destinationreg)
			print("DECODE: Read Registers "+firstop+" = " + str(reg[int(lel[12:16],2)])+", "+secondop+" = "+str(reg[int(lel[20:],2)]))
		else:
			secondop = str(int(lel[20:],2))
			print("DECODE: Operation is "+mainstring+condstring+", First Operand is "+firstop+", immediate Second Operand is "+secondop+", Destination Register "+destinationreg)
			print("DECODE: Read Registers "+firstop+" = " + str(reg[int(lel[12:16],2)]))
		
	elif(num[4:6]=="01"):
		firstop = "R"+str(int(lel[12:16],2))
		secondop = "R"+str(int(lel[16:20],2))
		offset = str(int(lel[20:],2))
		if(num[11]=="0"):
			mainstring = "STR"
			print("DECODE: Operation is "+mainstring+condstring+", First operand(base address) is "+firstop+", Offset is "+offset+", Source Register "+secondop)
			print("DECODE: Read Registers "+firstop+" = " + str(int(lel[12:16],2))+", "+secondop+" = "+str(reg[int(lel[16:20],2)]))
		elif(num[11]=="1"):
			mainstring = "LDR"
			print("DECODE: Operation is "+mainstring+condstring+", First operand(base address) is "+firstop+", Offset is "+offset+", Source Register "+secondop)
			print("DECODE: Read Registers "+firstop+" = " + str(int(lel[12:16],2))+", "+secondop+" = "+str(reg[int(lel[16:20],2)]))

	elif(num[4:6]=="10"):
		mainstring = "B"
		print("DECODE: Operation is "+mainstring+condstring)


def execute(N,Z,flag,nxt):
	lel = b[reg[15]]
	cond=0
	nxt=0;
	condstring = "";mainstring = "";firstop = "";secondop = "";destinationreg = ""
	num  = str(lel)
	if (num[:4]=="0000"):
		#"EQ"
		cond = 1;
	elif (num[:4]=="0001"):
		#"NE"
		cond=2;
	elif (num[:4]=="0100"):
		#"MI"
		cond=3;
	elif (num[:4]=="0101"):
		#"PL"
		cond=4;
	elif (num[:4]=="1010"):
		#"GE"
		cond=5;
	elif (num[:4]=="1011"):
		#"LT"
		cond=6
	elif (num[:4]=="1100"):
		#"GT"
		cond=7
	elif (num[:4]=="1101"):
		#"LE"
		cond = 8;
	perform=0
	if(num[4:6]=="00"):
		
		firstop = int(lel[12:16],2)
		destinationreg = int(lel[16:20],2)
		if(num[6]=="0"):
			
			secondop = int(lel[20:],2)
		else:
			secondop = int(lel[20:],2)
		
		if(num[7:11]=="0000"):
			#mainstring = "AND"
			if(cond>0):
				if(cond==1 and Z==1):
					perform = 1;
				elif (cond==2 and Z==0):
					perform = 1;
				elif(cond==3 and N==1):
					perform = 1
				elif(cond==4 and N==0):
					perform = 1
				elif(cond==5 and (N==0 or Z==1)):
					perform=1;
				elif(cond==6 and (N==1)):
					perform=1;
				elif(cond==7 and N==0):
					perform=1;
				elif(cond==8 and (N==1 or Z==1)):
					perform=1;
			if(perform==1 or cond==0):
				if(num[6]=='0'):
					print("EXECUTE:  Bitwise AND of "+ str(reg[firstop])+" and "+str(reg[secondop]))
					r[destinationreg] = reg[firstop]&reg[secondop]
					
				else:
					print("EXECUTE:  Bitwise AND of "+ str(reg[firstop])+" and "+str(secondopas))
					r[destinationreg] = reg[firstop]&secondop
					

			
		elif(num[7:11]=="0010"):
			#SUB
			if(cond>0):
				if(cond==1 and Z==1):
					perform = 1;
				elif (cond==2 and Z==0):
					perform = 1;
				elif(cond==3 and N==1):
					perform = 1
				elif(cond==4 and N==0):
					perform = 1
				elif(cond==5 and (N==0 or Z==1)):
					perform=1;
				elif(cond==6 and (N==1)):
					perform=1;
				elif(cond==7 and N==0):
					perform=1;
				elif(cond==8 and (N==1 or Z==1)):
					perform=1;
			if(perform==1 or cond==0):
				if(num[6]=='0'):
					print("EXECUTE:  Subtract "+ str(reg[firstop])+" and "+str(reg[secondop]))
					reg[destinationreg] = reg[firstop]-reg[secondop]
					
				else:
					print("EXECUTE:  Subtract "+ str(reg[firstop])+" and "+str(secondop))
					reg[destinationreg] = reg[firstop]-secondop
					

		elif(num[7:11]=="0100"):
			#"ADD"
			if(cond>0):
				if(cond==1 and Z==1):
					perform = 1;
				elif (cond==2 and Z==0):
					perform = 1;
				elif(cond==3 and N==1):
					perform = 1
				elif(cond==4 and N==0):
					perform = 1
				elif(cond==5 and (N==0 or Z==1)):
					perform=1;
				elif(cond==6 and (N==1)):
					perform=1;
				elif(cond==7 and N==0):
					perform=1;
				elif(cond==8 and (N==1 or Z==1)):
					perform=1;
			if(perform==1 or cond==0):
				
				if(num[6]=='0'):
					print("EXECUTE: Add "+ str(reg[firstop])+" and "+str(reg[secondop]))
					reg[destinationreg] = reg[firstop]+reg[secondop]
					
				else:
					print("EXECUTE: Add "+ str(reg[firstop])+" and "+str(secondop))
					reg[destinationreg] = reg[firstop]+secondop
					
		elif(num[7:11]=="1010"):
			#"CMP"
			if(num[6]=='0'):
				val = reg[firstop] - reg[secondop];
			else:
				val = reg[firstop] - secondop;

			if(cond>0):
				if(cond==1 and Z==1):
					perform = 1;
				elif (cond==2 and Z==0):
					perform = 1;
				elif(cond==3 and N==1):
					perform = 1
				elif(cond==4 and N==0):
					perform = 1
				elif(cond==5 and (N==0 or Z==1)):
					perform=1;
				elif(cond==6 and (N==1)):
					perform=1;
				elif(cond==7 and N==0):
					perform=1;
				elif(cond==8 and (N==1 or Z==1)):
					perform=1;
			if(perform==1 or cond==0):
				if(val==0):
					Z=1
				elif(val<0):
					N=1	
				if(num[6]=='0'):
					print("EXECUTE: Compare "+ str(reg[firstop])+" and "+str(reg[secondop]))
				else:
					print("EXECUTE: Compare "+ str(reg[firstop])+" and "+str(secondop))

		elif(num[7:11]=="1011"):
			#"CMN"
			if(num[6]=='0'):
				val = reg[firstop] + reg[secondop];
			else:
				val = reg[firstop] + secondop;
			val = firstop + secondop;
			if(cond>0):
				if(cond==1 and Z==1):
					perform = 1;
				elif (cond==2 and Z==0):
					perform = 1;
				elif(cond==3 and N==1):
					perform = 1
				elif(cond==4 and N==0):
					perform = 1
				elif(cond==5 and (N==0 or Z==1)):
					perform=1;
				elif(cond==6 and (N==1)):
					perform=1;
				elif(cond==7 and N==0):
					perform=1;
				elif(cond==8 and (N==1 or Z==1)):
					perform=1;
			if(perform==1 or cond==0):
				if(val==0):
					Z=1
				elif(val<0):
					N=1	
				if(num[6]=='0'):
					print("EXECUTE: Negated Compare "+ str(reg[firstop])+" and "+str(-1*reg[secondop]))
				else:
					print("EXECUTE: Negated Compare "+ str(reg[firstop])+" and "+str(-1*secondop))

		elif(num[7:11]=="1100"):
			#"ORR"
			if(cond>0):
				if(cond==1 and Z==1):
					perform = 1;
				elif (cond==2 and Z==0):
					perform = 1;
				elif(cond==3 and N==1):
					perform = 1
				elif(cond==4 and N==0):
					perform = 1
				elif(cond==5 and (N==0 or Z==1)):
					perform=1;
				elif(cond==6 and (N==1)):
					perform=1;
				elif(cond==7 and N==0):
					perform=1;
				elif(cond==8 and (N==1 or Z==1)):
					perform=1;
			if(perform==1 or cond==0):
				if(num[6]=='0'):
					print("EXECUTE: Logical OR of "+ str(reg[firstop])+" and "+str(reg[secondop]))
					r[destinationreg] = reg[firstop]|reg[secondop]
					
				else:
					print("EXECUTE: Logical OR of "+ str(reg[firstop])+" and "+str(secondop))
					r[destinationreg] = reg[firstop]|secondop
					

		elif(num[7:11]=="1101"):
			#"MOV"
			if(cond>0):
				if(cond==1 and Z==1):
					perform = 1;
				elif (cond==2 and Z==0):
					perform = 1;
				elif(cond==3 and N==1):
					perform = 1
				elif(cond==4 and N==0):
					perform = 1
				elif(cond==5 and (N==0 or Z==1)):
					perform=1;
				elif(cond==6 and (N==1)):
					perform=1;
				elif(cond==7 and N==0):
					perform=1;
				elif(cond==8 and (N==1 or Z==1)):
					perform=1;
			if(perform==1 or cond==0):
				if(num[6]=='0'):
					print("EXECUTE: MOV "+ "R"+str(secondop)+" to "+"R"+str(destinationreg))
					reg[destinationreg] = reg[secondop]
					
				else:
					print("EXECUTE: MOV "+ str(secondop)+" to "+"R"+str(destinationreg))
					reg[destinationreg] = secondop
					

		elif(num[7:11]=="1111"):
			#"MVN"
			if(cond>0):
				if(cond==1 and Z==1):
					perform = 1;
				elif (cond==2 and Z==0):
					perform = 1;
				elif(cond==3 and N==1):
					perform = 1
				elif(cond==4 and N==0):
					perform = 1
				elif(cond==5 and (N==0 or Z==1)):
					perform=1;
				elif(cond==6 and (N==1)):
					perform=1;
				elif(cond==7 and N==0):
					perform=1;
				elif(cond==8 and (N==1 or Z==1)):
					perform=1;
			if(perform==1 or cond==0):
				if(num[6]=='0'):
					print("EXECUTE: MOV Negated "+ "-R"+str(secondop)+" to "+"R"+str(reg[firstop]))
					r[destinationreg] = -1*reg[secondop]
					
				else:
					print("EXECUTE: MOV Negated "+ str(-1*secondop)+" to "+"R"+str(reg[firstop]))
					r[destinationreg] = -1*secondop
					
		
	
	elif(num[4:6]=="01"):
		firstop = int(lel[12:16],2)
		secondop = int(lel[16:20],2)
		offset = int(lel[20:],2)
		if(num[11]=="0"):
			#"STR"
			if(cond>0):
				if(cond==1 and Z==1):
					perform = 1;
				elif (cond==2 and Z==0):
					perform = 1;
				elif(cond==3 and N==1):
					perform = 1
				elif(cond==4 and N==0):
					perform = 1
				elif(cond==5 and (N==0 or Z==1)):
					perform=1;
				elif(cond==6 and (N==1)):
					perform=1;
				elif(cond==7 and N==0):
					perform=1;
				elif(cond==8 and (N==1 or Z==1)):
					perform=1;
			if(perform==1 or cond==0):
				
					if(num[8]=='0'):
						print("EXECUTE: Store "+ "R"+str(secondop)+" to memory address")
						memory[reg[firstop]-offset] = reg[secondop] 
					else:
						print("EXECUTE: Store "+ "R"+str(secondop)+" to memory address")
						memory[reg[firstop]+offset] = reg[secondop] 
				

			
		elif(num[11]=="1"):
			#"LDR"	
			if(cond>0):
				if(cond==1 and Z==1):
					perform = 1;
				elif (cond==2 and Z==0):
					perform = 1;
				elif(cond==3 and N==1):
					perform = 1
				elif(cond==4 and N==0):
					perform = 1
				elif(cond==5 and (N==0 or Z==1)):
					perform=1;
				elif(cond==6 and (N==1)):
					perform=1;
				elif(cond==7 and N==0):
					perform=1;
				elif(cond==8 and (N==1 or Z==1)):
					perform=1;
			if(perform==1 or cond==0):
				
					if(num[8]=='0'):
						print("EXECUTE: Load to "+ "R"+str(secondop)+" from memory address")
						nxt = memory[reg[firstop]-offset]
					else:
						print("EXECUTE: Load to "+ "R"+str(secondop)+" from memory address")
						nxt = memory[reg[firstop]+offset]
				
				
					if(secondop==15):
						flag=1;
					else:
						flag=0;
						reg[secondop] = nxt;
						nxt=0;
			
		


	elif(num[4:6]=="10"):
		#"B"
		if(cond>0):
			if(cond==1 and Z==1):
				perform = 1;
			elif (cond==2 and Z==0):
				perform = 1;
			elif(cond==3 and N==1):
				perform = 1
			elif(cond==4 and N==0):
				perform = 1
			elif(cond==5 and (N==0 or Z==1)):
				perform=1;
			elif(cond==6 and (N==1)):
				perform=1;
			elif(cond==7 and N==0):
				perform=1;
			elif(cond==8 and (N==1 or Z==1)):
				perform=1;
		if(perform==1 or cond==0):
			addr = twos_comp(int(lel[8:],2), len(lel[8:])) + 2
			print("EXECUTE: Branch to instruction address "+ str(addr))
			
			nxt = addr;
			flag=1
	return N,Z,flag,nxt

		




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
	Z=0;
	N=0;
	flag=0;
	
	while(True):
		instruction=instr[reg[15]]
		print("FETCH: Fetch instruction "+instr[reg[15]][instr[reg[15]].find(" "):]+" from address "+instr[reg[15]][0:instr[reg[15]].find(" ")])
		decode();
		N,Z,flag,val=execute(N,Z,flag,nxt);

		if(flag==0):
			reg[15]+=1
		else:
			reg[15]=reg[15]+ val;
			flag=0
		print("\n")
		

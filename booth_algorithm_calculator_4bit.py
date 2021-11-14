#List to record all steps in this list
steps_recorder=[];

#complement
def complement(a:int)->int:
    if(a==0):
        return 1;
    else:
        return 0;

#Full adder only input (1,0) , Output as tuple format(Sum,Carry-out)
def FullAdder(A, B, C)-> tuple:
    # Calculating value of sum
    Sum = C ^ (A ^ B);
    # Calculating value of C-Out
    C_Out = (A&B)|(B&C)|(A&C)
    # printing the values
    return (Sum,C_Out);
    
#Full substractor only input (1,0) , Output as tuple format(Diff,Borrow-out)
def FullSubstractor(X:int, Y:int, Z:int)-> tuple:
    # Calculating value of diff
    Diff = Z ^ (X ^ Y);
    # Calculating value of B-Out
    B_Out = (complement(X)&Z)|(complement(X)&Y)|(Y&Z)
    # printing the values
    return (Diff,B_Out);

#Adds two 4 bit bin numbers , Input (bit_count,tuple_Of_Abits,tuple_of_Bbits) , Output list of Sum bits (lsb in last index)
def FourBitAdder(A_bits:tuple,B_bits:tuple)-> list:
    
    output=[0,0,0,0];
    i=int(3);
    prev_c_out=int(0);
    while(i>=0):
        temp=FullAdder(A_bits[i],B_bits[i],prev_c_out);
        output[i]=temp[0];
        prev_c_out=temp[1];
        i=i-1;     
    return output;

#Four bit substractor , Input (tuple_Of_Abits,tuple_of_Bbits) , Output list of Sum bits (lsb in last index)
def FourBitSubstractor(A_bits:tuple,B_bits:tuple)-> list:

    output=[0,0,0,0];
    i=int(3);
    prev_b_out=int(0);
    while(i>=0):
        temp=FullSubstractor(A_bits[i],B_bits[i],prev_b_out);
        output[i]=temp[0];
        prev_b_out=temp[1];
        i=i-1; 
    return output;
   
#ArithmeticRightShift function
def ArithmeticRightShift(Acc:list,Q_reg:list,Q_1:int) -> list:
    out_list=[0,0,0,0,0,0,0,0,0];
    
    #Right shift
    out_list[0]=Acc[0];
    out_list[1]=Acc[0];
    out_list[2]=Acc[1];
    out_list[3]=Acc[2];
    out_list[4]=Acc[3];
    out_list[5]=Q_reg[0];
    out_list[6]=Q_reg[1];
    out_list[7]=Q_reg[2];
    out_list[8]=Q_reg[3];
    
    return out_list;

#Return 2's complement of a binary pattern of a list
def TwosComplement (inputList : list)->list:
    
    compList=[0,0,0,0];
    i=int(0);
    while(i<4):
        compList[i]=complement(inputList[i]);
        i+=1;
    
    outList=FourBitAdder((compList),(0,0,0,1));
    return outList;
 
#Integer to 4 bit binary , Input (inputNum) , Output list of 4 bits (lsb in last index)
def DecimalToBinary(inputVal:int)->list:
    if(inputVal<0):
        return [0,0,0,0];
    #Convert to binary
    input_Val_in_bin=bin(inputVal);
    #Remove '0b' from strings
    input_Val_in_bin=input_Val_in_bin.replace("0b", "");
    inValBinList=[int(char) for char in input_Val_in_bin];
    
    outList=[0,0,0,0];
    i=3;
    j=int(len(inValBinList)-1);

    while i>=0:
        if(j>=0):
            outList[i]=inValBinList[j];
        else:
            outList[i]=0;
        i=i-1;
        j=j-1;
    return outList

#Holds value of a step at given index
def Record_Step (step_num:int(), ACC_register_tuple : list(), Q_register_tuple:list(), Q_1:int, currentCount:int, currentStepString:str): 
        steps_recorder.append([step_num,ACC_register_tuple,Q_register_tuple,Q_1,currentCount,currentStepString]);

# Split string into characters,Input [0,1,2,3] -> Output ['0','1','2','3']
def ListToCharArray(word : list) -> list:
    return [str(char) for char in word];

# Format a list to string in specific way, Input ['0','1','2','3'] -> Output to string in format :- '0 [Space] 1 [Space] 2 [Space] 3 [Space]'
def CustomFormatter(inputList:list)->str:
  
    tabbedList=[];

    for i in inputList:
        tabbedList.append(i);
        tabbedList.append(' ');

    newStr = ""
    # traverse in the string 
    for x in tabbedList:
        newStr += x 
    # return string 
    return newStr

#Gives a padding value for a given string
def TextToPadding(inputStr: str())->str():

    strLen=len(inputStr);
    outStr='';
    if(strLen<12):
        #37
        outStr=' '*35
        pass
    elif(strLen>12 and strLen<35):
        #22
        outStr=' '*21
        pass
    elif(strLen>35):
        #1
        outStr=''
        pass
    return outStr;

#Draws chart
def DrawChart(inputList:list):
    
    print(" "*4," _____________________________________________________________________________________")
    print(" "*4,"|           |           |     |     |                                                 |")
    print(" "*4,"|     A     |     Q     |  Q1 |  C  |                     Steps                       |")
    print(" "*4,"|___________|___________|_____|_____|_________________________________________________|")

    listSize=len(inputList);

    i=int(0);
    while i<listSize:

        currRow=inputList[i];
        currA_List=currRow[1];
        currQ_List=currRow[2];
        
        currA=CustomFormatter(ListToCharArray(currA_List));
        currQ=CustomFormatter(ListToCharArray(currQ_List));
        currQ_1=currRow[3];
        curr_Count=currRow[4];
        curr_step=currRow[5];
        s=TextToPadding(curr_step);

        print(" "*4,"|           |           |     |     |                                                 |");
        print(" "*4,"| ",currA,"| ",currQ,"| ",currQ_1," | ",curr_Count," | ",curr_step,s,"|");
        print(" "*4,"|___________|___________|_____|_____|_________________________________________________|");
        i+=1;

#PROGRAM START!!!!!!!!

bitCount = int(4);
prep_M=[0,0,0,0];
prep_Q=[0,0,0,0];

print("\nProgram to multiply two numbers using Booth's Multiplication Algorithm with flowchart display and steps.")
print("Initial value of Count=4. A and Q are using 4 bits.\n")

input_M=int(input("Enter Multiplicand(in Decimal) : "));
input_Q=int(input("Enter Multiplier(in Decimal) : "));

##Check if inputs are positive or negative, If positive turn into binary ,if negative turn into binary and 2's complement them.

#if M is positive
if (input_M>=0):

    prep_M=DecimalToBinary(input_M);
    
elif (input_M<0):#if M is negative
    
    a=-input_M;#turn into +ve
    b=DecimalToBinary(a);
    prep_M=TwosComplement(b);

    pass;

#if Q is positive
if (input_Q>=0):
    
    prep_Q=DecimalToBinary(input_Q);
elif (input_Q<0):#if Q is negative

    a=-input_Q;#turn into +ve
    b=DecimalToBinary(a);
    prep_Q=TwosComplement(b);

#print(prep_M,prep_Q);

#Initialization step

accumulator_register = [0,0,0,0];
Q_register = [0,0,0,0];
Q_1=int(0);
#M=[0,1,1,1];    # Multiplicand
#Q=[0,0,1,1];    # Multiplier
M=prep_M;
Q=prep_Q;
Count=4;    # Change later

Q_register=Q;

Record_Step(0,accumulator_register,Q_register,Q_1,Count,"Initialize");

while Count!=0:

    #1st part
    #Get Q0 and Q_1
    Q_0=Q_register[-1];

    if (Q_0==Q_1):
        #do nothing
        pass
    elif (Q_0==1 and Q_1==0):
        #do A=A-M
        accumulator_register=FourBitSubstractor(tuple(accumulator_register),tuple(M));
        Record_Step(0,accumulator_register,Q_register,Q_1,Count,"Q0 Q1 = 1 0 ,Hence A=A-M");
    elif (Q_0==0 and Q_1==1):
        #do A=A+M
        accumulator_register=FourBitAdder(tuple(accumulator_register),tuple(M));
        Record_Step(0,accumulator_register,Q_register,Q_1,Count,"Q0 Q1 = 0 1 ,Hence A=A+M");

    # 2nd part

    #Get Right Shift of A,Q,Q_1
    
    out=ArithmeticRightShift(accumulator_register,Q_register,Q_1);
    accumulator_register=out[0:4];
    Q_register=out[4:8];
    Q_1=out[8];
   
    Count=Count-1;
    Record_Step(0,accumulator_register,Q_register,Q_1,Count,"Arithmetic Right Shift A Q Q1 , Count=Count-1");

#Loop end

#Draw the chart with results
DrawChart(steps_recorder);

print("\n\nResult in A Q is : [ ",CustomFormatter(ListToCharArray(accumulator_register))," ",CustomFormatter(ListToCharArray(Q_register)),"]",sep="");

print("\nProgram end")
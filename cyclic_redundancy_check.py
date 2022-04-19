# CYCLIC REDUNDANCY CHECK
# Function performing XOR operation
def xor_Operation(A,B):
        result=""
        if(A[0]=='0'):
            return A[1:]
        else:
           for i in range(0,len(B)):
            if A[i]==B[i]:
             result+='0'
            else:
             result+='1'
           return result[1:]

# Function performing MODULO-2 Binary Division 
def mod2_binaryDivision(dividend_Val,divisor_Val):
    j=len(divisor_Val)
    temp_dividend=dividend_Val[0:j]
    while(j<len(dividend_Val)):
            temp_dividend=xor_Operation(temp_dividend,divisor_Val)+dividend_Val[j]
            j+=1
    final_Output = xor_Operation(temp_dividend,divisor_Val)
    return final_Output
    
input_Data=input("THE MESSAGE BITS: ")
generator_Bits=input("THE GENERATOR BITS: ")

#Transmitter side
print("AT THE TRANSMITTER SIDE")
redundant_Bits='0'*(len(generator_Bits)-1)
appended_Data=input_Data+redundant_Bits  #Appending Zeros
print("THE APPENDED DATA BITS ARE: ",appended_Data)
remainder=mod2_binaryDivision(appended_Data,generator_Bits)
transmitted_Data=input_Data+remainder
print("THE REMAINDER DATA BITS ARE ",remainder)
print("THE ENCODED DATA: ",transmitted_Data)

#Receiver side
print("AT THE RECEIVER SIDE")
received_Data=transmitted_Data
print("THE RECEIVED DATA:",received_Data)
error_Check=mod2_binaryDivision(received_Data,generator_Bits)
print("THE REMAINDER VALUE: ",error_Check)

# Checking for error in the transmission media
flag=False
for k in range(0,len(error_Check)):
    if error_Check[k]=='1':
        flag=True
        print("\nERROR DETECTED IN RECEIVER SIDE.\n")
        break
if flag==False:
    print("\nNO ERROR DETECTED IN RECEIVER SIDE.\n")